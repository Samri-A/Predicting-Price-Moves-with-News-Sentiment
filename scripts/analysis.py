import talib as tl
import matplotlib.pyplot as plt
import pandas as pd
from pypfopt.efficient_frontier import EfficientFrontier
from pypfopt import risk_models , expected_returns
import seaborn as sns


def calculateTechnicalIndicator(stock_data):
    stock_data['SMA'] = tl.SMA(stock_data['Close'], timeperiod=20)
    stock_data['RSI'] = tl.RSI(stock_data['Close'], timeperiod=14)
    stock_data['EMA'] = tl.EMA(stock_data['Close'], timeperiod=20)

    macd_signal, macd, _ = tl.MACD(stock_data['Close'])
    stock_data['MACD'] =macd
    stock_data['MACD_Signal']=macd_signal

def analysisClosingPriceWithDate(stock_data_aapl,stock_data_amzn,stock_data_goog,stock_data_meta,stock_data_msft,stock_data_nvda):
    # Create subplots for side-by-side display
    fig, axs = plt.subplots(2, 3, figsize=(20, 10))  # Adjust figsize as needed

    axs[0,0].plot(stock_data_aapl['Date'], stock_data_aapl['Close'], label='Close',color='green')
    axs[0,0].set_title('AAPL')
    axs[0,0].legend()

    axs[0,1].plot(stock_data_amzn['Date'], stock_data_amzn['Close'], label='AMZN')
    axs[0,1].set_title('AMZN')
    axs[0,1].legend()


    axs[0,2].plot(stock_data_goog['Date'], stock_data_goog['Close'], label='Close',color='yellow')
    axs[0,2].set_title('GOOG')
    axs[0,2].legend()


    axs[1,0].plot(stock_data_nvda['Date'], stock_data_nvda['Close'], label='Close',color='brown')
    axs[1,0].set_title('NVDA')
    axs[1,0].legend()
    axs[1,0].set_xlabel('Date')


    axs[1,1].plot(stock_data_msft['Date'], stock_data_msft['Close'], label='Close',color='purple')
    axs[1,1].set_title('MSFT')
    axs[1,1].legend()
    axs[1,1].set_xlabel('Date')

    axs[1,2].plot(stock_data_meta['Date'], stock_data_meta['Close'], label='Close',color='orange')
    axs[1,2].set_title('META')
    axs[1,2].legend()
    axs[1,2].set_xlabel('Date')

    plt.show()


def technicalIndicatorsVsClosingPrice(stock_data_aapl,stock_data_amzn,stock_data_goog,stock_data_meta,stock_data_msft,stock_data_nvda,ticker):
    fig, axs = plt.subplots(2, 3, figsize=(20, 10))  # Adjust figsize as needed

    axs[0,0].plot(stock_data_aapl['Date'], stock_data_aapl['Close'], label='Closing price',color='green')
    axs[0,0].plot(stock_data_aapl['Date'], stock_data_aapl[ticker], label=ticker,color='red')
    axs[0,0].set_title('AAPL')
    axs[0,0].legend()

    axs[0,1].plot(stock_data_amzn['Date'], stock_data_amzn['Close'], label='Closing price')
    axs[0,1].plot(stock_data_amzn['Date'], stock_data_amzn[ticker], label=ticker,color='red')
    axs[0,1].set_title('AMZN')
    axs[0,1].legend()


    axs[0,2].plot(stock_data_goog['Date'], stock_data_goog['Close'], label='Closing price',color='yellow')
    axs[0,2].plot(stock_data_goog['Date'], stock_data_goog[ticker], label=ticker,color='red')
    axs[0,2].set_title('GOOG')
    axs[0,2].legend()


    axs[1,0].plot(stock_data_nvda['Date'], stock_data_nvda['Close'], label='Closing price',color='blue')
    axs[1,0].plot(stock_data_nvda['Date'], stock_data_nvda[ticker], label=ticker,color='red')
    axs[1,0].set_title('NVDA')
    axs[1,0].legend()
    axs[1,0].set_xlabel('Date')


    axs[1,1].plot(stock_data_msft['Date'], stock_data_msft['Close'], label='Closing price',color='purple')
    axs[1,1].plot(stock_data_msft['Date'], stock_data_msft[ticker], label=ticker,color='red')
    axs[1,1].set_title('MSFT')
    axs[1,1].legend()
    axs[1,1].set_xlabel('Date')

    axs[1,2].plot(stock_data_meta['Date'], stock_data_meta['Close'], label='Closing price',color='pink')
    axs[1,2].plot(stock_data_meta['Date'], stock_data_meta[ticker], label=ticker,color='red')
    axs[1,2].set_title('META')
    axs[1,2].legend()
    axs[1,2].set_xlabel('Date')

    plt.show()
    
    
    
def closingPriceRelativeStrengthIndex(stock_data_aapl,stock_data_amzn,stock_data_goog,stock_data_meta,stock_data_msft,stock_data_nvda):
    fig, axs = plt.subplots(6,2, gridspec_kw={"height_ratios": [1, 1, 1, 1,1,1]}, figsize=(16,22))

    # For AAPL
    axs[0][0].plot(stock_data_aapl['Date'], stock_data_aapl['Close'],label="Close")
    axs[0][0].set_title("AAPL Stock Price")
    axs[0][0].legend()
    axs[1][0].axhline(y=70, color='r',linestyle="--")
    axs[1][0].axhline(y=30, color='g',linestyle="--")
    axs[1][0].plot(stock_data_aapl['Date'],stock_data_aapl['RSI'], color='orange', label="RSI")
    axs[1][0].legend()

    # for GOOG
    axs[0][1].plot(stock_data_goog['Date'], stock_data_goog['Close'],label="Close")
    axs[0][1].set_title("GOOG Stock Price")
    axs[0][1].legend()
    axs[1][1].axhline(y=70, color='r',linestyle="--")
    axs[1][1].axhline(y=30, color='g',linestyle="--")
    axs[1][1].plot(stock_data_goog['Date'],stock_data_goog['RSI'], color='orange', label="RSI")
    axs[1][1].legend()

    # for AMZN
    axs[2][0].plot(stock_data_amzn['Date'], stock_data_amzn['Close'],label="Close")
    axs[2][0].set_title("AMZN Stock Price")
    axs[2][0].legend()
    axs[3][0].axhline(y=70, color='r',linestyle="--")
    axs[3][0].axhline(y=30, color='g',linestyle="--")
    axs[3][0].plot(stock_data_amzn['Date'],stock_data_amzn['RSI'], color='orange', label="RSI")
    axs[3][0].legend()

    # for NVDA
    axs[2][1].plot(stock_data_nvda['Date'], stock_data_nvda['Close'],label="Close")
    axs[2][1].set_title("NVDA Stock Price")
    axs[2][1].legend()
    axs[3][1].axhline(y=70, color='r',linestyle="--")
    axs[3][1].axhline(y=30, color='g',linestyle="--")
    axs[3][1].plot(stock_data_nvda['Date'],stock_data_nvda['RSI'], color='orange', label="RSI")
    axs[3][1].legend()


    # for MSFT
    axs[4][0].plot(stock_data_msft['Date'], stock_data_msft['Close'],label="Close")
    axs[4][0].set_title("MSFT Stock Price")
    axs[4][0].legend()
    axs[5][0].axhline(y=70, color='r',linestyle="--")
    axs[5][0].axhline(y=30, color='g',linestyle="--")
    axs[5][0].plot(stock_data_msft['Date'],stock_data_msft['RSI'], color='orange', label="RSI")
    axs[5][0].legend()

    # for META
    axs[4][1].plot(stock_data_meta['Date'], stock_data_meta['Close'],label="Close")
    axs[4][1].set_title("META Stock Price")
    axs[4][1].legend()
    axs[5][1].axhline(y=70, color='r',linestyle="--")
    axs[5][1].axhline(y=30, color='g',linestyle="--")
    axs[5][1].plot(stock_data_meta['Date'],stock_data_meta['RSI'], color='orange', label="RSI")
    axs[5][1].legend()
    fig.show()
    # momentum oscillator that measures the speed and change of price movements.
    # Identifying overbought and oversold conditions. A reading above 70 is typically 
    # considered overbought, while a reading below 30 is considered oversold.
    
    




    
def closingPriceMovingAverageConvergenceDivergence(stock_data_aapl,stock_data_amzn,stock_data_goog,stock_data_meta,stock_data_msft,stock_data_nvda):
        
    fig, axs = plt.subplots(6,2, gridspec_kw={"height_ratios": [1, 1, 1, 1,1,1]}, figsize=(16,22))

    # for AAPL
    axs[0][0].plot(stock_data_aapl['Date'], stock_data_aapl['Close'],label="Close")
    axs[0][0].set_title("AAPL Stock Price")
    axs[0][0].legend()
    axs[1][0].axhline(y=5, color='r',linestyle="--")
    axs[1][0].axhline(y=-5, color='g',linestyle="--")
    axs[1][0].plot(stock_data_aapl['Date'],stock_data_aapl['MACD'], color='orange', label="MACD")
    axs[1][0].plot(stock_data_aapl['Date'],stock_data_aapl['MACD_Signal'], color='r', label="MACD_Signal")
    axs[1][0].legend()


    # for GOOG
    axs[0][1].plot(stock_data_goog['Date'], stock_data_goog['Close'],label="Close")
    axs[0][1].set_title("GOOG Stock Price")
    axs[0][1].legend()
    axs[1][1].axhline(y=5, color='r',linestyle="--")
    axs[1][1].axhline(y=-5, color='g',linestyle="--")
    axs[1][1].plot(stock_data_aapl['Date'],stock_data_aapl['MACD'], color='orange', label="MACD")
    axs[1][1].plot(stock_data_aapl['Date'],stock_data_aapl['MACD_Signal'], color='r', label="MACD_Signal")
    axs[1][1].legend()

    # for AMZN
    axs[2][0].plot(stock_data_amzn['Date'], stock_data_amzn['Close'],label="Close")
    axs[2][0].set_title("AMZN Stock Price")
    axs[2][0].legend()
    axs[3][0].axhline(y=5, color='r',linestyle="--")
    axs[3][0].axhline(y=-5, color='g',linestyle="--")
    axs[3][0].plot(stock_data_aapl['Date'],stock_data_aapl['MACD'], color='orange', label="MACD")
    axs[3][0].plot(stock_data_aapl['Date'],stock_data_aapl['MACD_Signal'], color='r', label="MACD_Signal")
    axs[3][0].legend()

    # for NVDA
    axs[2][1].plot(stock_data_nvda['Date'], stock_data_nvda['Close'],label="Close")
    axs[2][1].set_title("NVDA Stock Price")
    axs[2][1].legend()
    axs[3][1].axhline(y=5, color='r',linestyle="--")
    axs[3][1].axhline(y=-5, color='g',linestyle="--")
    axs[3][1].plot(stock_data_aapl['Date'],stock_data_aapl['MACD'], color='orange', label="MACD")
    axs[3][1].plot(stock_data_aapl['Date'],stock_data_aapl['MACD_Signal'], color='r', label="MACD_Signal")
    axs[3][1].legend()


    # for MSFT
    axs[4][0].plot(stock_data_msft['Date'], stock_data_msft['Close'],label="Close")
    axs[4][0].set_title("MSFT Stock Price")
    axs[4][0].legend()
    axs[5][0].axhline(y=5, color='r',linestyle="--")
    axs[5][0].axhline(y=-5, color='g',linestyle="--")
    axs[5][0].plot(stock_data_aapl['Date'],stock_data_aapl['MACD'], color='orange', label="MACD")
    axs[5][0].plot(stock_data_aapl['Date'],stock_data_aapl['MACD_Signal'], color='r', label="MACD_Signal")
    axs[5][0].legend()

    # for META
    axs[4][1].plot(stock_data_meta['Date'], stock_data_meta['Close'],label="Close")
    axs[4][1].set_title("META Stock Price")
    axs[4][1].legend()
    axs[5][1].axhline(y=5, color='r',linestyle="--")
    axs[5][1].axhline(y=-5, color='g',linestyle="--")
    axs[5][1].plot(stock_data_aapl['Date'],stock_data_aapl['MACD'], color='orange', label="MACD")
    axs[5][1].plot(stock_data_aapl['Date'],stock_data_aapl['MACD_Signal'], color='r', label="MACD_Signal")
    axs[5][1].legend()
    fig.show()
    # A MACD crossover (when the signal line crosses the MACD line) can indicate a potential trend change.
    # In this case both MACD and MACD_Signal have the same value



def calculatePortfolioWeightAndPerformance(
    stock_data_aapl,
    stock_data_amzn,
    stock_data_goog,
    stock_data_meta,
    stock_data_msft,
    stock_data_nvda
):
    # Extract Close prices
    close_data = pd.concat([
        stock_data_aapl['Close'],
        stock_data_amzn['Close'],
        stock_data_goog['Close'],
        stock_data_meta['Close'],
        stock_data_msft['Close'],
        stock_data_nvda['Close']
    ], axis=1)

    # Rename columns for clarity
    close_data.columns = ['AAPL', 'AMZN', 'GOOG', 'META', 'MSFT', 'NVDA']

    # Calculate expected returns and sample covariance matrix
    mu = expected_returns.mean_historical_return(close_data)
    S = risk_models.sample_cov(close_data)

    # Optimize for maximum Sharpe ratio
    ef = EfficientFrontier(mu, S)
    raw_weights = ef.max_sharpe()
    cleaned_weights = dict(zip(close_data.columns, [round(value, 2) for value in raw_weights.values()]))

    # Output the portfolio weights
    print("Portfolio Weights:")
    print(cleaned_weights)

    # Output the portfolio performance
    print("\nPortfolio Performance:")
    ef.portfolio_performance(verbose=True)

    
