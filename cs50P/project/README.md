# Financial Calculator

## Video Demo: [Watch the Demo](https://youtu.be/nmJ90pNfsSw)

## Description:
My project allows the user to get historical stock data and manipulate that data to return useful values about a stock. If the user decides to buy the stock, the program will pretty-print all relevant information to assist with that decision.

## Function Descriptions

### `main()`
This function orchestrates the flow of the program. It starts by calling `get_months()`, then loops over `get_data()`, `get_statistics()`, and `buy_decision()`. The user may want to continue searching for other stocks if they don’t want to buy the current one. Finally, it calls the `portfolio()` function.

### `get_months()`
This function gathers the last day of the last twelve months using libraries like `calendar`. It is important because the last twelve months are used to fetch stock data in the next function, `get_data()`.

### `get_data()`
The core function of the project. It uses an API to gather stock data and returns a dictionary with key-value pairs, the most important being the closing prices of stocks for the last day of each month. The API requires a key, which you can get from [Alpha Vantage](https://www.alphavantage.co/). The function searches the dictionary for the closing prices and returns them as a list. If the last day of the month doesn’t match the market’s last day, it subtracts days until it finds the correct closing price.

### `get_statistics()`
This function uses the `pandas` library to calculate percentage changes over the last twelve closing prices. These values help calculate the expected value and deviation, which represent the expected return and risk of a stock. These values are passed to the `buy_decision()` function.

### `buy_decision()`
This function presents the calculated statistics and offers the user the option to buy or not to buy the stock. If the user chooses to buy, the program will ask how many stocks they want to purchase. If the user chooses not to buy, it will return to the `get_data()` function. The `main()` function has a loop that allows the user to search for other stocks.

### `portfolio()`
This function gathers all relevant data: the stock ticker, the number of stocks, the price, and the value (price multiplied by the number of stocks). It then presents this data in a neatly formatted table using the `tabulate` library.

---

## Conclusion
This project is useful for those who want a quick calculation of historical stock data. Although it may not be accurate for predicting future trends, it provides important information that can lead to better investment decisions.

**THIS WAS MY FINAL PROJECT**

Thank you.
