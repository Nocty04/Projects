from numpy import *
import numpy as np
from scipy import stats
import pandas as pd
from pandas import json_normalize
import requests
from datetime import datetime
import os
import time
from math import exp, sqrt, log
import matplotlib.pyplot as plt



def montecarlo(S0=100, K=105, T=1, r=0.05, sigma=0.2, I=100000):
    # S0 = price of the underlying asset
    # K = strike price
    # r = riskless rate
    # sigma = volatility
    # T = time until expiration date
    # I = number of simulations

    # uses normal distribution for I simulations
    z = random.standard_normal(I)
    # future value of the underlying asset Black-Scholes
    ST = S0 * exp((r - 1 / 2 * sigma ** 2) * T + sigma * sqrt(T) * z)
    # Calculate the Payoff at maturity
    ht = maximum(ST - K, 0)
    # calculate the average of the payoffs and comes back to the present value
    # follows a Geometric Brownian Motion, GBM and as simulations tends to infinity = Black scholes
    CO = exp(-r * T) * sum(ht) / I

    print("The value of the European option is %5.3f" % CO)


### Option pricing black scholes Formulas ###
# S0 = price of the underlying asset
# K = strike price
# r = riskless rate
# sigma = volatility
# T = time until expiration date
# C0 = price of the option
# sigma_est= estimate of volatility

# Black-Scholes for option pricing
# Follows a Lognormal Distribution

### Calculates implied vollatillity for sp500 with maturity date march 15(available futures data) ###
def bs_value(S0, K, r, sigma, T):
    # represents the probability of being in the money option
    d1 = (log(S0 / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * sqrt(T))
    # represents the probability of the option being exercised in the expiration date
    d2 = (log(S0 / K) + (r - 0.5 * sigma ** 2) * T) / (sigma * sqrt(T))

    # uses both d1 and d2 to calculate the mixed probability of the two propositions
    # returns present value of option
    value = (S0 * stats.norm.cdf(d1) - K * exp(-r * T) * stats.norm.cdf(d2))

    return value


def bs_vega(S0, K, r, sigma, T):
    d1 = (log(S0 / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * sqrt(T))
    # sensitivity of option prices based on changes in volatility
    vega = S0 * stats.norm.cdf(d1, 0.0, 1.0) * sqrt(T)

    return vega

    # optimizing implied volatility based on the estimate and returns implied volatility
    # Newton-Raphson method.


def bs_sigma_est(S0, K, T, r, C0, sigma_est, it):
    for i in range(it):
        price_diff = bs_value(S0, K, r, sigma_est, T) - C0
        vega = bs_vega(S0, K, r, sigma_est, T)
        sigma_est -= price_diff / vega
    return sigma_est

def date_time():
    today = datetime.now().strftime('%Y-%m-%d')
    return today

def vollatility(tol=0.1):
    # Opens csv file of stored info and creates a new dataframe
    df = pd.read_csv("data.csv")  # contract information option
    df["imp_vol"] = 0
    # available futures data of Emini-series SP500 for maturity: march-15
    for idx, row in df.iterrows():
        forward = df["FutClose"].values[idx]
        print(forward)
        # creates new collumn for time to maturity
        current_date = datetime.strptime(date_time(), "%Y-%m-%d")
        ttm = (datetime.strptime(row["OExpiration"], "%Y-%m-%d") - current_date).days / 365
        df.loc[idx,"TTM"] = ttm

        if forward * (1 - tol) < row["Strike"] < forward * (1 + tol):
            imp_vol = bs_sigma_est(
                S0=row["FutClose"],
                K=row["Strike"],
                T=row["TTM"],
                r=0.01,
                C0=row["OptClose"],
                sigma_est=0.2,
                it=100)
            df.loc[idx,"imp_vol"] = float(imp_vol)

    df.to_csv("data.csv", index = False)


def graph_smile():
    plt.figure(figsize=(8, 6))
    data = pd.read_csv("data.csv")
    plt.plot(data["Strike"], data["imp_vol"], label=["TTM"], lw=1.5)
    plt.plot(data["Strike"], data["imp_vol"], "r.")

    plt.grid(True)
    plt.xlabel("Strike")
    plt.ylabel("implied volatility")
    plt.legend()
    plt.show()

def vector_montecarlo(S0=100, M=50, I=250000, r=0.05, k=105, sigma=0.2, T=1):
    # Calculate the payoff at maturity for each path using np.maximum(S[-1] - K, 0).
    # Sum all the payoffs from all the simulated paths.
    # Discount the sum of payoffs back to the present using exp(−rT).
    # Average the discounted payoffs by dividing by I (the number of simulations).
    dt = T / M
    S = np.zeros((M + 1, I))
    # starting at the same stock price
    S[0] = S0
    for t in range(1, M + 1):
        z = np.random.standard_normal(I)
        # Geometric Brownian Motion (GBM)
        S[t] = S[t - 1] * np.exp((r - 0.5 * sigma ** 2) * dt + sigma * sqrt(dt) * z)

    C0 = exp(-r * T) * np.sum(np.maximum(S[-1] - k, 0)) / I

    print(C0)
    print(sum(S[-1] < k))

    fig, ax = plt.subplots(1, 3, figsize=(12, 6))

    ax[0].plot(S[:, :10])
    ax[0].grid(True)
    ax[0].set_ylabel("Index level")
    ax[0].set_xlabel("timestep")
    ax[0].set_title("Stock price paths")

    ax[1].hist(S[-1], bins=50)
    ax[1].grid(True)
    ax[1].set_xlabel("indexlevel")
    ax[1].set_ylabel("frequency")
    ax[1].set_title("histogram of final index levels")

    ax[2].hist(np.maximum(S[-1] - k, 0), bins=50)
    ax[2].grid(True)
    ax[2].set_xlabel("option inner value")
    ax[2].set_ylabel("Frequency")
    ax[2].set_ylim(0, 50000)
    ax[2].set_title("histogram of final option value")

    plt.tight_layout()
    plt.show()

        # wait  60 seconds until new api request available and all option tickers have been scraped

    # FUNCTION THAT CALLS ALL OTHERS TO UPDATE THE DATA IN CSV FILES TO IMPLEME

