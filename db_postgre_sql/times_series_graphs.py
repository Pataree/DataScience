import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.seasonal import seasonal_decompose 
from statsmodels.tsa.stattools import acf, pacf
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.stattools import ARMA
from statsmodels.tsa.statespace import sarimax


def calculate_ma(df, colname, days):
    new_col_name = colname + '_ma_' + str(days)
    df[new_col_name] = df[colname].rolling(window=days, min_periods=0).mean()
    return df

def plot_rolling_graph(df, window=100):
    df.adjclose.plot(figsize=(15,2))
    df.adjclose.rolling(window).mean().plot(figsize=(15,2))


# Plot graphs the moving average vs volumns
def plot_moving_average( df, col1='AdjClose', col2='Volume', days=100):
###
#    Giving a data frame, plot the graph based on
#    'Adj Close' and 'Volumn' and the first column
#    100 days moving average, otherwise specify your own
###

    ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5)
    ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, sharex=ax1)
    
    #moving average based on col1 name
    col3 = col1 + '_ma_' + str(days)
    
    ax1.plot(df.index, df[col1])
    ax1.plot(df.index, df[col3])
    ax2.bar(df.index, df[col2])
    
    ax1.legend()
    ax2.legend()
    plt.show()


def stationarity_test(data, window_type, colName='adjclose'):
    shares=data[colName]
    #rolling mean
    rm=shares.rolling(window=window_type).mean()
    #median
    rmd=shares.rolling(window=window_type).median()

    #expanding
    em=shares.expanding().mean()
    # exponentially weighted mean
    ewm=shares.ewm(span=10).mean()
    
    # Dickey Fuller Test
    dft=adfuller(shares)
    dft_result=pd.Series(dft[:2],index=['T-stats','p-value'])
    print(dft_result)
    
    rolling_list=[shares, rm, rmd, em, ewm]
    label_list=[colName,'r mean','r median','expanding mean','exp w-mean']
    for u,v in zip(rolling_list,label_list):
        u.plot(label=v, figsize=(16,4),lw=2)
        plt.legend()

def rolling_std(data, window_type, colName='adjclose'):
    shares=data[colName]
    
    #rolling mean
    rm=shares.rolling(window=window_type).mean()

    #standard deviation
    rstd=shares.rolling(window=window_type).std()

    #std - upper bound (2 std away)
    stdUpper =  rm + 2* rstd
    stdLower =  rm - 2* rstd

    rolling_list=[shares, rm, stdUpper, stdLower]
    label_list=[colName,'RollingMean','UpperBound','LowerBound']
    for u,v in zip(rolling_list,label_list):
        u.plot(label=v, figsize=(16,4),lw=2)
        plt.legend()
    

    

def stationarity_2(data, window_type, colName='adjclose'):
    shares=data[colName]
    #rolling mean
    rm=shares.rolling(window=window_type).mean()
    #median
    rmd=shares.rolling(window=window_type).median()
    #expanding
    em=shares.expanding().mean()
    # exponentially weighted mean
    ewm=shares.ewm(span=10).mean()
    
    # Dickey Fuller Test
    dft=adfuller(shares)
    dft_result=pd.Series(dft[:2],index=['T-stats','p-value'])
    print('# Dickey Fuller Test')
    print(dft_result)
    
    # Diff the time series
    shares_diff = shares-shares.shift()

    # Dickey Fuller Test on diff time series
    shares_diff = shares_diff.dropna()
    dft2=adfuller(shares_diff)
    dft_results2=pd.Series(dft2[:2],index=['T-stats','p-value'])
    print('# Dickey Fuller Test on diff time series')
    print(dft_results2)
    
    rolling_list=[shares, rm, rmd, em, ewm, shares_diff]
    label_list=[colName,'r mean','r median','expanding mean','exp w-mean', colName +' diff']
    for u,v in zip(rolling_list,label_list):
        u.plot(label=v, figsize=(16,4),lw=2)
        plt.legend()