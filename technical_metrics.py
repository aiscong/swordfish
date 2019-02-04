import pandas as pd
import numpy as np

# reference website
# https://pyalgotrade-docs-zh-cn.readthedocs.io/zh_CN/latest/technical.html#module-pyalgotrade.technical.macd/

data = pd.read_csv('/Users/j0y01rf/PycharmProjects/swordfish/historical_data/AAPL.csv', index_col=0)

####################################
# returns

def log_return(data):
    """
    :param data: input values [type: pd.Series/pd.DataFrame] [index: datetime]
    :return: log returns [type: pd.Series/pd.DataFrame] [index: datetime]
    """
    return np.log(data/data.shift(1)) - 1

####################################
# trend indicator

def simple_moving_average(data, windowSize):
    """
    :param data: input values [type: pd.Series/pd.DataFrame] [index: datetime]
    :param windowSize: moving average window in mins [type: int]
    :return: simple moving average values [type: pd.Series/pd.DataFrame] [index: datetime]
    """
    return data.rolling(window=(windowSize//5)).mean().dropna()

####################################
# volatility indicator


def simple_moving_historical_volatility(data, windowSize):
    """
    :param data: input values [type: pd.Series/pd.DataFrame] [index: datetime]
    :param windowSize: moving average window in mins [type: int]
    :return: simple moving average historical volatility [type: pd.Series/pd.DataFrame] [index: datetime]
    """
    return data.rolling(window=(windowSize//5)).std() * np.sqrt(windowSize)

####################################
# momentum indicators

# Moving Average Convergence/Divergence Oscillator
def MACD(data, fastEMA=12, slowEMA=26, signalEMA=9):
    """
    :param data: input values [type: pd.Series/pd.DataFrame] [index: datetime]
    :param fastEMA: The number of values to use to calculate the fast EMA. [type: int]
    :param slowEMA: The number of values to use to calculate the slow EMA. [type: int]
    :param signalEMA: The number of values to use to calculate the signal EMA. [type: int]
    :return: [type: pd.Series/pd.DataFrame] [index: datetime]
        MACD_line: fastEMA - slowEMA
        Single_line: singalEMA of MACD_line
        MACD_histogram: MACD_line - Single_line
    """
    data_fastEMA = data.ewm(span=fastEMA, adjust=False).mean()
    data_slowEMA = data.ewm(span=slowEMA, adjust=False).mean()
    MACD_line = data_fastEMA - data_slowEMA
    Single_line = MACD_line.ewm(span=signalEMA, adjust=False).mean()
    MACD_histogram = MACD_line - Single_line

    return MACD_line, Single_line, MACD_histogram