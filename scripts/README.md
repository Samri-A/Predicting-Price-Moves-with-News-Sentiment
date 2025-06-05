# 📈 Stock Technical Analysis Module

This Python module provides utilities for **visualizing stock data** and calculating common **technical indicators** using `TA-Lib`, along with price trend comparisons for major stocks like AAPL, AMZN, GOOG, META, MSFT, and NVDA.

## 🚀 Features

* Calculate key technical indicators:

  * Simple Moving Average (SMA)
  * Exponential Moving Average (EMA)
  * Relative Strength Index (RSI)
  * MACD and Signal Line
* Visualize:

  * Stock closing price over time
  * Technical indicators vs closing price
  * RSI trends and overbought/oversold zones
  * MACD crossover patterns

## 🛠️ Requirements

Install the dependencies:

```bash
pip install pandas matplotlib seaborn TA-Lib PyPortfolioOpt
```

> **Note:** TA-Lib must be installed separately at the system level for some platforms. See: [https://mrjbq7.github.io/ta-lib/install.html](https://mrjbq7.github.io/ta-lib/install.html)

## 📦 Usage

```python
import pandas as pd
from your_module import calculateTechnicalIndicator, analysisClosingPriceWithDate
```

### 1. Calculate Indicators

```python
calculateTechnicalIndicator(stock_data_aapl)
```

### 2. Visualize Closing Prices

```python
analysisClosingPriceWithDate(stock_data_aapl, stock_data_amzn, stock_data_goog,
                              stock_data_meta, stock_data_msft, stock_data_nvda)
```

### 3. Compare Technical Indicators

```python
technicalIndicatorsVsClosingPrice(stock_data_aapl, stock_data_amzn,
                                   stock_data_goog, stock_data_meta,
                                   stock_data_msft, stock_data_nvda,
                                   ticker="SMA")  # or RSI, EMA, MACD, etc.
```

### 4. Visualize RSI or MACD Separately

```python
closingPriceRelativeStrengthIndex(stock_data_aapl, ...)
closingPriceMovingAverageConvergenceDivergence(stock_data_aapl, ...)
```

## 📊 Sample Plot

> The module produces multi-panel plots comparing price trends and indicator performance across top stocks.

---

## 🧠 Notes

* MACD plots use a default reference from AAPL data; for better clarity, adjust to use the corresponding stock's MACD.
* Ensure `Date` columns are in datetime format and sorted.

---

