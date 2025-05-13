from ibapi.client import EClient
from ibapi.contract import ContractDetails
from ibapi.wrapper import EWrapper
from ibapi.client import Contract
from ibapi.client import Order, ScannerSubscription
from ibapi.tag_value import TagValue

import queue
import pandas as pd
import time, datetime
from threading import Thread
from lightweight_charts import Chart

stock_symbol = "TSM"

default_host = "127.0.0.1"
default_client_id = 1
data_queue = queue.Queue()

# innitializing class with the two classes as the parameters ECLIENT wich sends requests ; EWrapper wich receives

class IBClient(EClient, EWrapper):
    def __init__(self, host, port, client_id):
        EClient.__init__(self, self)
        self.connect(host, port, client_id)

        thread = Thread(target=self.run)
        thread.start()

    def error(self, req_id, code, msg, misc):
        if code in [2104, 2106, 2158]:
            print(msg)
        else:
            print(f"Error {code}: {msg}")

    def nextValidId(self, orderId: int):
        super().nextValidId(orderId)
        self.order_id = orderId
        print(f"next valid id is {self.order_id}")

    def historicalData(self, req_id, bar):
        t = datetime.datetime.fromtimestamp(int(bar.date))

        data = {"date": t,
                "open": bar.open,
                "high": bar.high,
                "low": bar.low,
                "close": bar.close,
                "volume": int(bar.volume)}

        data_queue.put(data)

    def historicalDataEnd(self, req_id, start, end):
        print(f"end of data: start:{start}, end:{end}")
        update_chart()

def on_horizontal_line_move(chart, line):
    print(f"Horizontal line moved to:{line.price}")

def update_chart():
    try:
        bars = []
        while True:
            data = data_queue.get_nowait()
            bars.append(data)
    except queue.Empty:
        print("Empty queue")
    finally:
        df = pd.DataFrame(bars)
        print(df)

        if not df.empty:
            chart.set(df)

            line = chart.create_line(name="SMA50")
            line.set(pd.DataFrame({"time": df["date"], f"SMA50": df["close"].rolling(window=50).mean()}).dropna())

            chart.spinner(False)


def get_bar_data(symbol, timeframe):
    contract = Contract()
    contract.symbol = symbol
    contract.secType = "STK"
    contract.exchange = "SMART"
    contract.currency = "USD"
    to_show = "TRADES"

    chart.spinner(True)

    client.reqHistoricalData(2, contract, "", "30 D", timeframe, to_show, 0, 2, False, [])
    time.sleep(1)

    chart.watermark(symbol)


def on_timeframe_selection(chart):
    print("selected timeframe")
    print(chart.topbar["symbol"].value, chart.topbar["timeframe"].value)
    get_bar_data(chart.topbar["symbol"].value, chart.topbar["timeframe"].value)


def on_search(chart, searched_string):
    get_bar_data(searched_string, chart.topbar["timeframe"].value)
    chart.topbar["symbol"].set(searched_string)


def place_order(key):
    symbol = chart.topbar["symbol"].value

    contract = Contract()
    contract.symbol = symbol
    contract.secType = "STK"
    contract.exchange = "SMART"
    contract.currency = "USD"

    order = Order()
    order.orderType = "MKT"
    order.totalQuantity = on_orderQuantity(chart)

    client.reqIds(-1)
    time.sleep(2)

    if key == "O":
        print("Buy order")
        order.action = "BUY"

    if key == "P":
        print("sell order")
        order.action = "SELL"

    if client.order_id:
        print("got order id, placing buy order")
        client.placeOrder(client.order_id, contract, order)


def on_orderQuantity(chart):
    return chart.topbar["quantity"].value


def take_screenshot(key):
    img = chart.screenshot()
    t = time.time()
    with open(f"screenshot-{t}.png", "wb") as f:
        f.write(img)


def do_scan(scan_code):
    # 10% gainers
    scannerSubscription = ScannerSubscription()
    scannerSubscription.instrument = "STK"
    scannerSubscription.locationCode = "STK.US.MAJOR"
    scannerSubscription.scanCode = scan_code

    tag_values = []
    tag_values.append(TagValue("optVolumeAbove", "1000"))
    tag_values.append(TagValue("avgVolumeAbove", "10000"))

    client.reqScannerSubscription(7002, scannerSubscription, [], tag_values)

    display_scan()

    client.cancelScannerSubscription(7002)


def display_scan():
    def on_row_click(row):
        chart.topbar["symbol"].set(row["symbol"])
        get_bar_data(row["symbol"], "5 mins")

    table = chart.create_table(
        width=0.4,
        height=0.5,
        headings=("symbol", "value"),
        widths=(0.7, 0.3),
        alignments=("left", "center"),
        position="left",
        func=on_row_click
    )

    try:
        while True:
            data = data_queue.get_nowait()
            table.new_row(data["symbol"], "")
    except queue.Empty:
        print("Empty Queue")
    finally:
        print("done!")


if __name__ == "__main__":
    client = IBClient(default_host, 7497, default_client_id)

    time.sleep(1)
    chart = Chart(toolbox=True, width=1000, inner_width=0.6, inner_height=1)
    chart.legend(True)

    chart.topbar.textbox("symbol", stock_symbol)
    chart.topbar.switcher("timeframe", ("5 mins", "10 mins", "15 mins", "30 D"), default="5 mins",
                          func=on_timeframe_selection)
    chart.topbar.switcher("quantity", ("1", "10", "25", "50", "100", "200", "500"), default="1", func=on_orderQuantity)

    chart.events.search += on_search

    chart.hotkey("shift", "O", place_order)
    chart.hotkey("shift", "P", place_order)

    chart.topbar.button("screenshot", "Screenshot", func=take_screenshot)

    get_bar_data(stock_symbol, "5 mins")

    chart.show(block=True)
