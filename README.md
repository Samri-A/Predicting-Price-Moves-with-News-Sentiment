# 🧠 Financial News Sentiment and Stock Price Analysis

This project explores the relationship between financial news headlines and stock price movements using NLP and quantitative technical indicators. It combines **exploratory data analysis**, **topic modeling**, and **time series analysis** with technical analysis tools like **TA-Lib** and **PyNance**.

---

## 📁 Project Structure

```
├── .vscode/                  # Editor-specific settings
│   └── settings.json
├── .github/
│   └── workflows/
│       └── unittests.yml     # CI for unit testing
├── .gitignore
├── requirements.txt          # Python dependencies
├── README.md                 # Project overview
├── src/                      # Core Python source code
│   ├── __init__.py
├── notebooks/                # Jupyter notebooks for analysis
│   ├── __init__.py
│   └── README.md
├── tests/                    # Unit tests
│   ├── __init__.py
├── scripts/                  # Utility or helper scripts
│   ├── __init__.py
│   └── README.md
```

---

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/financial-news-analysis.git
cd financial-news-analysis
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🧪 Tasks Overview

### ✅ Task 1: Exploratory Data Analysis (EDA)

#### 📊 Descriptive Statistics

* Analyze textual features (e.g., headline length).
* Count articles by publisher.
* Analyze publication frequency over time.

#### 🧠 Text Analysis (Topic Modeling)

* Extract keywords and recurring topics (e.g., "earnings", "merger").
* Identify news themes and sentiment.

#### 📈 Time Series & Publishing Time Trends

* Analyze how news frequency changes over time.
* Detect key dates with publishing spikes (e.g., major market events).
* Investigate time-of-day publication patterns.

#### 📰 Publisher Analysis

* Rank publishers by article count.
* Detect dominant domains in publisher emails.

---

### ✅ Task 2: Quantitative Stock Analysis with TA-Lib & PyNance

#### 📥 Load and Prepare Financial Data

* Load historical stock price data (Open, High, Low, Close, Volume).

#### 📉 Apply Technical Indicators (TA-Lib)

* **Moving Averages (SMA, EMA)** – Smooth price trends.
* **RSI (Relative Strength Index)** – Detect overbought/oversold levels.
* **MACD (Moving Average Convergence Divergence)** – Spot momentum shifts.

---

### ✅ Task 3: Correlation Between News and Stock Movement

#### 📅 Date Alignment

* Ensure both datasets (news and stock prices) are aligned by date.
* Normalize timestamps to daily granularity.

#### 💬 Sentiment Analysis

* Apply sentiment scoring to news headlines (positive, neutral, negative).
* Tools: Use **NLTK** and **TextBlob** for sentiment polarity and subjectivity.

#### 📈 Stock Movement Calculation

* Compute daily stock returns using percentage change in closing prices.

#### 🔗 Correlation Analysis

* Use statistical methods (Pearson/Spearman correlation) to measure the relationship between daily sentiment scores and stock returns.
* Visualize the correlation patterns using scatter plots and heatmaps.

---

## 🛠️ Technologies Used

* **Python**: Core language
* **Pandas, NumPy**: Data manipulation
* **Matplotlib, Seaborn, Plotly**: Visualizations
* **TA-Lib**: Technical indicators
* **PyNance**: Financial metrics
* **Scikit-learn, NLTK, spaCy, TextBlob**: NLP tools
* **Git & GitHub**: Version control & collaboration
* **GitHub Actions**: CI for unit testing

---

## 📌 Future Work

* Compare price fluctuations directly with sentiment scores.
* Compare technical indicators between different stocks or events.
* Train ML models to predict price movements from sentiment and indicators.
* Deploy interactive visualizations via a web dashboard (e.g., Streamlit or Dash).

