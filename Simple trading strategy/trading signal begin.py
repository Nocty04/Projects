import pandas as pd
import numpy as np
from ibapi.client import Contract, EClient
from ibapi.common import TickerId, TagValueList
from ibapi.contract import ContractDetails
from ibapi.wrapper import EWrapper
from threading import Thread
from datetime import datetime, timedelta
import csv
import time
import queue
import matplotlib.pyplot as plt


host = "127.0.0.1"
port = 7497
client_id = 1

p_queue = queue.Queue()
class IbkrClient(EClient, EWrapper):
    def __init__(self, host, port, client_id ):
        EClient.__init__(self, self)
        self.connect(host, port, client_id )
        self.data = []

        thread = Thread(target=self.run, daemon=True)
        thread.start()

    def error(self, req_id, code, msg, misc):
        if code == 10089:
            print("Market data requires additional subscription. Please check your IBKR subscriptions.")
        elif code in [2146, 2106, 2104]:
            print(msg)
        else:
            print(f"Error: {code} {msg}")

    def nextValidId(self, orderId):
        super().nextValidId(orderId)
        self.orderId = orderId
        print(f"orderid:{orderId}")

        time.sleep(3)
        self.start_requests()

    def start_requests(self):
        self.stk_contract()
    def stk_contract(self):
        stock = Contract()
        stock.symbol = "SPY"
        stock.secType = "STK"
        stock.exchange = "SMART"
        stock.currency = "USD"

        print(stock)
        self.reqHistStkData(stock)

    def reqHistStkData(self, stock):
        reqId = 10000

        self.reqHistoricalData(
            reqId=reqId,
            contract=stock,
            endDateTime="",
            durationStr="5 Y",
            barSizeSetting="1 day",
            whatToShow="TRADES",
            useRTH=0,
            formatDate=1,
            keepUpToDate=False,
            chartOptions=[]
        )

    def historicalData(self, req_id, bar):
        bar_data = {
            "Close" : bar.close,
            "date" : bar.date
        }
        self.data.append(bar_data)

    def historicalDataEnd(self, req_id, start, end):
        print("Historical data received completely.")
        # Once all data is received, set the event
        df = pd.DataFrame(self.data)
        df["date"] = pd.to_datetime(df["date"])  # Convert date to datetime
        df.set_index("date", inplace=True)
        p_queue.put(df)  # Push the dataframe into the queue



def beginner_startegy(df):
    df["42d"] = np.round(df["Close"].rolling(window=42).mean(), 2)
    df["252d"] = np.round(df["Close"].rolling(window=252).mean(), 2)
    df["delta"] = df["42d"] - df["252d"]
    time.sleep(1)

    results = []

    for SD in range(1, 50):
        df["regime"] = 0
        df.loc[df["delta"] > SD, "regime"] = 1
        df.loc[df["delta"] < -SD, "regime"] = -1

        df["market"] = np.log(df["Close"] / df["Close"].shift(1))
        df["strategy"] = df["regime"].shift(1) * df["market"]

        result = df["strategy"].cumsum().apply(np.exp).iloc[-1]

        results.append((SD, result))

    results_df = pd.DataFrame(results, columns =["SD", "result"])
    best = results_df.loc[results_df["result"].idxmax()]

    best_SD = best["SD"]
    print(f"best SD Is {best_SD}")
    df["regime"] = 0
    df.loc[df["delta"] > best_SD, "regime"] = 1
    df.loc[df["delta"] < -best_SD, "regime"] = -1

    df["market"] = np.log(df["Close"] / df["Close"].shift(1))
    df["strategy"] = df["regime"].shift(1) * df["market"]

    df["marketReturn"] = df["market"].cumsum().apply(np.exp)
    df["stratReturn"] = df["strategy"].cumsum().apply(np.exp)

    sharpe = calculate_sharpe_ratio(df["strategy"])
    print(f"sharp is {sharpe}")

    fig, ax = plt.subplots(1, 3, figsize=(12, 6))

    ax[0].plot(df[["Close", "42d", "252d", "delta"]])
    ax[0].grid(True)

    ax[1].plot(df["regime"])
    ax[1].grid(True)

    ax[2].plot(df[["marketReturn", "stratReturn"]])
    ax[2].grid(True)

    plt.show()

def calculate_sharpe_ratio(returns, i=0.0, period=252):
    excess_returns = returns - i
    excessMean = excess_returns.mean()
    excessStd = excess_returns.std()

    sharpe_ratio = (excessMean/excessStd) * np.sqrt(period)
    return sharpe_ratio

if __name__ == "__main__":
    client = IbkrClient(host, port, client_id)
    df = pd.DataFrame(p_queue.get())
    beginner_startegy(df)

