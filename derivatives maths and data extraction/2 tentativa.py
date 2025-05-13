from ibapi.client import Contract, EClient
from ibapi.common import TickerId, TagValueList
from ibapi.contract import ContractDetails
from ibapi.wrapper import EWrapper
from threading import Thread
from datetime import datetime, timedelta
import csv
import time
import pandas as pd

d_host = "127.0.0.1"
port = 7497
d_client_id = 1

class IBKRClient(EClient,EWrapper):
    #initializes all variables storage, connects to IBKR and starts a thread
    def __init__(self, host, port, client_id):
        EClient.__init__(self, self)
        self.connect(host, port, client_id)

        self.contracts = []
        self.futures = []
        self.expirations = []
        self.stock = []
        self.metadata = {}
        self.allSecData = []

        thread = Thread(target=self.run, daemon = True)
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
        self.generate_setexpirations(self.expirations)

        self.stk_contract()
        time.sleep(1)
        #self.reqHistStkData()
        time.sleep(1)
        #self.Opt_params(self.expirations)
        time.sleep(1)
        #self.reqHistOptData(self.contracts)
        time.sleep(1)
        self.Fut_contract(self.expirations)
        time.sleep(1)
        self.reqHistFutData(self.futures)

    def generate_setexpirations(self, expirations):
        start_date = datetime.strptime("20250101","%Y%m%d")
        end_date = datetime.strptime("20251230","%Y%m%d")
        while start_date <= end_date:
            print(start_date.strftime("%Y%m%d"))
            expirations.append(start_date.strftime("%Y%m%d"))
            start_date += timedelta(days=1)



    def generate_expirations(self, expirations):
        # timedelta today - 1 2
        today = datetime.today()
        past = today - timedelta(days=2)
        print(today)
        print(past)
        start_date = datetime.strptime(str(past.strftime("%Y%m%d")), "%Y%m%d")
        end_date = datetime.strptime(str(today.strftime("%Y%m%d")),"%Y%m%d")
        step = timedelta(days=1)

        while start_date <= end_date:
            expirations.append(start_date.strftime("%Y%m%d"))
            start_date += step

    def stk_contract(self):
        stock = Contract()
        stock.symbol = "SPY"
        stock.secType = "STK"
        stock.exchange ="SMART"
        stock.currency = "USD"

        print(stock)
        self.stock.append(stock)

    def reqHistStkData(self):
        reqId = 10000
        self.metadata[reqId] = {
            "secType": "STK"
        }

        self.reqHistoricalData(
            reqId=reqId,
            contract=self.stock[0],
            endDateTime="",
            durationStr="2 D",
            barSizeSetting="30 mins",
            whatToShow="TRADES",
            useRTH=0,
            formatDate=1,
            keepUpToDate=False,
            chartOptions=[]
        )

    def Opt_params(self, expirations):
        strikes = range(490, 570, 5)
        reqId = self.orderId

        for expiration in expirations:
            for strike in strikes:
                contract = Contract()
                contract.symbol = "SPY"
                contract.secType = "OPT"
                contract.lastTradeDateOrContractMonth = expiration
                contract.strike = float(strike)
                contract.right = "C"
                contract.exchange = "SMART"
                contract.currency = "USD"
                contract.multiplier = "100"
                contract.includeExpired = True

                print(f"conrtact {contract}")
                self.contracts.append(contract)
                reqId += 1
                time.sleep(0.1)

    def reqHistOptData(self, contracts):
        for reqId, contract in enumerate(contracts, start = 15000):
            self.metadata[reqId] = {
                "secType": "OPT",
                "strike":contract.strike,
                "expiration":contract.lastTradeDateOrContractMonth
            }
            self.reqHistoricalData(
                reqId= reqId,
                contract = contract,
                endDateTime="",
                durationStr="2 D",
                barSizeSetting="30 mins",
                whatToShow="TRADES",
                useRTH=0,
                formatDate=1,
                keepUpToDate=False,
                chartOptions=[]
            )

    def Fut_contract(self, expirations):
        reqId = 20000
        # exp =['202501', '202502', '202503', '202504', '202505', '202506',
        #          '202507', '202508', '202509', '202510', '202511', '202512']
        # for expration in exp:
        for expiration in expirations:
            future = Contract()
            future.currency = "USD"
            future.lastTradeDateOrContractMonth = expiration
            future.exchange = "GLOBEX"
            future.symbol = "ES"
            future.secType = "FUT"
            future.tradingClass = "ES"
            future.multiplier = "50"
            future.includeExpired = True

            print(f"future : {future}")
            self.futures.append(future)
            reqId += 1
            time.sleep(0.1)


    def reqHistFutData(self, futures):
        for reqId, future in enumerate(futures, start=5000):
            self.metadata[reqId] = {
                "secType": "FUT",
                "expiration": future.lastTradeDateOrContractMonth
            }

            self.reqHistoricalData(
                reqId=reqId,
                contract=future,
                endDateTime="",
                durationStr="2 D",
                barSizeSetting="30 mins",
                whatToShow="TRADES",
                useRTH=0,
                formatDate=1,
                keepUpToDate=False,
                chartOptions=[]
            )



    def historicalData(self, req_id, bar):
        print("data received")
        metadata = self.metadata.get(req_id, {})

        if metadata.get("secType") == "OPT":
            bar_data ={
                "date": bar.date,
                "OptClose": bar.close,
                "strike": metadata.get("strike"),
                "OExpiration": metadata.get("expiration")
            }
            print(bar_data)

            self.allSecData.append(bar_data)

        elif metadata.get("secType") == "FUT":
            bar_data = {
                "FutClose": bar.close,
                "Fexpiration": metadata.get("expiration")
            }
            print(bar_data)
            self.allSecData.append(bar_data)
        elif metadata.get("secType") == "STK":
            bar_data = {
                "StkClose": bar.close
            }
            print(bar_data)
            self.allSecData.append(bar_data)

        self.data_storage(self.allSecData)

    def data_storage(self, data):
        corrected_data = []
        for Security in data:
            organize_data = {
                "OptClose": Security.get("OptClose"),
                "StkClose":Security.get("StkClose"),
                "FutClose":Security.get("FutClose"),
                "Strike": Security.get("Strike"),
                "OExpiration": Security.get("OExpiration"),
                "Date": Security.get("date")
            }

            corrected_data.append(organize_data)


        fieldnames = ["OptClose", "StkClose", "FutClose", "Strike","Date","OExpiration"]
        with open("data.csv", "a+", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            file.seek(0)
            if not file.readline():
                writer.writeheader()

            writer.writerows(corrected_data)

def clear_csv_file():
    df = pd.read_csv("data.csv", nrows=0)
    df.to_csv("data.csv", index=False)

if __name__ == "__main__":
    client = IBKRClient(d_host, port, d_client_id)


