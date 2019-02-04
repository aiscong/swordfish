import pandas as pd
import numpy as np
import os
import datetime
# reference website
# https://pyalgotrade-docs-zh-cn.readthedocs.io/zh_CN/latest/technical.html#module-pyalgotrade.technical.macd/

data = pd.read_csv(os.getcwd() + '/historical_data/AAPL.csv', index_col=0)


####################################te
# returns


def log_return(data, start_date, end_date):
    """
    :param data: input values [type: pd.Series/pd.DataFrame] [index: datetime]
    :return: log returns [type: pd.Series/pd.DataFrame] [index: datetime]
    """
    data.index = pd.to_datetime(data.index)
    df = data.loc[start_date:end_date]
    return np.log(df['close'].iloc[-1] / df['close'].iloc[0])


####################################
# trend indicator


def sma(data, window_size):
    """
    :param data: input values [type: pd.Series/pd.DataFrame] [index: datetime]
    :param window_size: moving average window in mins [type: int]
    :return: simple moving average values [type: pd.Series/pd.DataFrame] [index: datetime]
    """
    return data.rolling(window=(window_size // 5)).mean().dropna()


####################################
# volatility indicator


<<<<<<< HEAD
def simple_moving_historical_volatility(data, windowSize):
=======
def simple_moving_historical_volatility(data, window_size):
>>>>>>> 7e574d68c1cded4fabd0c8232848f4850c699920
    """
    :param data: input values [type: pd.Series/pd.DataFrame] [index: datetime]
    :param window_size: moving average window in mins [type: int]
    :return: simple moving average historical volatility [type: pd.Series/pd.DataFrame] [index: datetime]
    """
<<<<<<< HEAD
    return data.rolling(window=(windowSize//5)).std() * np.sqrt(windowSize)
=======
    return data.rolling(window=(window_size // 5)).std() * np.sqrt(window_size)

>>>>>>> 7e574d68c1cded4fabd0c8232848f4850c699920

####################################
# momentum indicators


# Moving Average Convergence/Divergence Oscillator
def macd(data, fast_span=12, slow_span=26, signal_span=9):
    """
    :param data: input values [type: pd.Series/pd.DataFrame] [index: datetime]
    :param fast_span: The number of values to use to calculate the fast EMA. [type: int]
    :param slow_span: The number of values to use to calculate the slow EMA. [type: int]
    :param signal_span: The number of values to use to calculate the signal EMA. [type: int]
    :return: [type: pd.Series/pd.DataFrame] [index: datetime]
        macd_line: fast_ema - slow_ema
        signal_line: signalEMA of MACD_line
        MACD_histogram: macd - signal
    """
    fast_ema = data.ewm(span=fast_span, adjust=False).mean()
    slow_ema = data.ewm(span=slow_span, adjust=False).mean()
    macd = fast_ema - slow_ema
    signal = macd.ewm(span=signal_span, adjust=False).mean()
    macd_histogram = macd - signal

    return macd, signal, macd_histogram

print(log_return(data, start_date='2019-01-23', end_date='2019-01-23'))