# Projects
Personal Python Projects Portfolio

This repository showcases a collection of my Python-based projects developed as part of my journey to become a stronger software developer and quantitative analyst. The projects range from foundational programming exercises to real-world finance applications using the Interactive Brokers (IBKR) API.

## 🧠 Contents

### 📘 CS50P – Harvard's Introduction to Programming with Python
A complete walkthrough of the CS50's Python course. Covers:
- Python basics (functions, conditions, loops)
- File I/O and exceptions
- Object-oriented programming
- Unit testing
- Web APIs and JSON

Purpose: Build a strong foundation in Python by following a rigorous, project-based curriculum.

---

### ❌ Tic-Tac-Toe AI (Minimax Algorithm)
A command-line Tic-Tac-Toe game where the AI uses the **Minimax algorithm** to play perfectly.

Features:
- Human vs AI gameplay
- Minimax recursion with terminal state evaluation
- Guaranteed unbeatable AI

Purpose: Learn fundamental concepts of **game theory**, **recursion**, and **decision trees**.

---

### 📈 Interactive Brokers (IBKR) API Projects

#### 1. ✅ Market Data Extraction
Fetches historical data for stocks, options, and futures using IBKR’s `ib_insync` and `IBAPI`.

Focus:
- Derivatives pricing data for mathematical modeling
- Real-time and historical OHLCV data
- Instrument metadata and filtering (e.g., strike prices, expiry dates)

Purpose: Build a flexible and scalable system to feed pricing models for quantitative finance.

---

#### 2. 📊 Simple Trading Strategy
Implements a basic trend-following trading strategy using:
- Moving averages
- Delta signal logic
- Strategy vs. market return tracking
- Performance optimization through signal threshold (`SD`) tuning

Includes:
- Strategy backtest loop
- Log return calculation
- Cumulative return tracking
- Sharpe ratio evaluation

Purpose: Understand how to structure and evaluate algorithmic trading strategies.

---

#### 3. 🖥️ UI for Stock Plotting
An interactive visualization tool using the **`lightweight-charts`** library.

Displays:
- Price chart with real-time or historical data
- Moving averages
- Buy/sell signals from strategy logic

Purpose: Improve user interaction and data visualization for trading systems.

---

## 🛠️ Tools & Libraries Used
- Python 3.x
- `pandas`, `numpy`, `matplotlib`
- `ib_insync`, `IBAPI` (Interactive Brokers API)
- `lightweight-charts` (via PyWebView or frontend integration)
- CS50P curriculum and tooling

---

## 🚀 Future Plans
- Extend trading strategies with machine learning
- Add portfolio tracking & performance analytics
- Improve UI with more interactivity (React, Streamlit, or Dash)
- Add options greeks calculation module

---

## 📬 Contact
Feel free to connect with me if you're interested in collaborating or want to talk about quant finance, programming, or anything related.
