import json
import requests
from datetime import date, timedelta
import calendar
import pandas as pd
from tabulate import tabulate
import csv
import math

def main():
    months = get_months()

    #Loop so that it allows the user to keep searching as he/she pleases
    try:
        while True:
            prices, ticker = get_data(months)
            deviation, expected = get_statistics(prices)
            number_stock = buy_decision(deviation, expected)
            if number_stock == None:
                pass
            else:
                break
        portfolio(ticker, number_stock, prices)
    except EOFError:
        print("thank you for using my program")



def get_months():

    today = date.today()
    last_twelve_months = []

    #gathers all last days of the twelve last months

    for _ in range(12):
        last_day = calendar.monthrange(today.year, today.month)[1]  #the second position of the tuple returns last day of the month
        last_date_of_month = date(today.year, today.month, last_day)
        last_twelve_months.append(str(last_date_of_month))

        if today.month == 1:
            today = date(today.year - 1, 12, 31)    #If this month is january it returns to last year
        else:
            today = date(today.year, today.month, 1) - timedelta(days=1)    #This places today in last month to get data

    return last_twelve_months

def get_data(n):    
    api_key = "2W075STHR88VVXFJ"    #This is my Api key you may use yours

    while True:
        ticker = input("What stock do you want to buy? ").upper()
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol={ticker}&interval=5min&apikey={api_key}'
        r = requests.get(url)
        data = r.json() #all the data of the stock

        if 'Error Message' in data:
            print("Invalid Ticker")
            pass
        elif 'Information' in data:
            print("You have used 25 attempts, try again next day to get the data.")
        else:
            break

    closing_prices = []

    for i in range(12):
        actual_date = n[i]
        year, month, day = actual_date.split("-")

        #Searches for the key and returns the closing prices of the last 12 months
        while True:
            date_key = f"{year}-{month}-{day}"
            if date_key in data["Monthly Time Series"]:
                closing_prices.append(data["Monthly Time Series"][date_key]["4. close"])
                break
            else:
                if int(day) >= 1:       #Gets last day of stock market data, sometimes the last day of the month is not the last day of the stock market data
                    day = int(day) - 1
                else:                   #if it needs to change to last year to get stock market data
                    month = 12
                    year = int(year) - 1
                    day = 31


    return closing_prices, ticker

def get_statistics(m):
    prices_series = pd.Series(pd.to_numeric(m, errors='coerce'))
    percentage_change = prices_series.pct_change() * 100
    percentage_change = percentage_change.dropna() #if There is a ValueError in the data Nan

    Expected_Value = percentage_change.mean()

    squared_deviations = (percentage_change - Expected_Value) ** 2
    variance = squared_deviations.mean()
    deviation = math.sqrt(variance)

    return Expected_Value, deviation


def buy_decision(a,b):
    buy = input(f"""\nThe risk the stock has is {a}% and the expected value for the next month
based on historical data is {b}%.

Do you wish to buy the stock?
Type 'yes' to buy, or 'no' to keep using the software: """)

    while True:
        if buy == "yes":
            try:
                weight = input("\nhow many do you wish to buy? ")
                return int(weight)
            except ValueError:
                print("invalid weight")
                pass
        elif buy == "no":
            return None     #it keeps the user in the loop so that he may search another stock
        else:
            buy = input("repeat please: ")
            pass

def portfolio(ticker, weight, closing_prices):
    closing_price = closing_prices[0]
    total_value = f"{float(closing_price) * weight}$"

    with open('stock.csv', 'a', newline='') as file: #opens csv file
        writer = csv.writer(file)


        if file.tell() == 0: #if The file is empty creates headers
            writer.writerow(['Ticker', 'Price', 'Weight', 'Value'])

        writer.writerow([ticker, closing_price, weight, total_value]) #Adds the data relevant of the stock you bought to the file

    print(f"\nPortfolio updated for {ticker}:") #shows the user that the portfolio updated

    portfolio_data = [{'Ticker': ticker, 'Price': closing_price, 'Weight': weight, 'Value': total_value}]
    print(tabulate(portfolio_data, headers="keys", tablefmt="grid"))    # pretty prints the values

if __name__ == "__main__":
    main()
























