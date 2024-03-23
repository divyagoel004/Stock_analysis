import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
from datetime import datetime
a1=pd.read_csv("TSLA.csv")
a2=pd.read_csv('MARA.csv')
a3=pd.read_csv('AAPL.csv')
a4=pd.read_csv('HDB.csv')
a5=pd.read_csv('INR=X.csv')
a6=pd.read_csv('JIOFIN.NS.csv')
a7=pd.read_csv('TATAMOTORS.NS.csv')
a1['Date']=pd.to_datetime(a1['Date'])
a2['Date']=pd.to_datetime(a2['Date'])
a3['Date']=pd.to_datetime(a3['Date'])
a4['Date']=pd.to_datetime(a4['Date'])
a5['Date']=pd.to_datetime(a5['Date'])
a6['Date']=pd.to_datetime(a6['Date'])
a7['Date']=pd.to_datetime(a7['Date'])

if(a1.shape[0]>=200):
    a1['MA_20'] = a1['Close'].rolling(window=20).mean()
    a1['MA_200'] = a1['Close'].rolling(window=200).mean()

    a1['Sell_Signal'] = 0
    a1.loc[(a1['MA_20'] < a1['MA_200']) , 'Sell_Signal'] = 1
    plt.figure(figsize=(12, 6))
    plt.plot(a1.index, a1['MA_20'], label='20-day MA')
    plt.plot(a1.index, a1['MA_200'], label='200-day MA')
    plt.scatter(a1[a1['Sell_Signal'] == 1].index, a1['MA_20'][a1['Sell_Signal'] == 1], marker='v', color='r', label='Sell Signal')
    plt.title('OHLC Data with Moving Averages and Sell Signals of TSLA Data')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()
    if(a1.shape[0]>=500):
        a1['MA_50'] = a1['Close'].rolling(window=50).mean()
        a1['MA_500'] = (a1['Close']).rolling(window=500).mean()
        a1['Signal'] = 0

        a1.loc[a1['MA_50'] >a1['MA_500'], 'Signal'] = 1
        plt.figure(figsize=(12, 6))
        plt.plot(a1.index, a1['MA_50'], label='50-day MA')
        plt.plot(a1.index, a1['MA_500'], label='500-day MA')
        plt.plot(a1[a1['Signal'] == 1].index, a1['MA_50'][a1['Signal'] == 1], '^', markersize=10, color='g', lw=0, label='Buy Signal')
        plt.title('OHLC Data with Moving Averages and Buy Signal of TSLA Data')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.show()
print('Closing signal for  buy position on TSLA Data\n\n\n\n')
a1['MA_10'] = a1['Close'].rolling(window=10).mean()
a1['MA_20'] = a1['Close'].rolling(window=20).mean()

a1['Close_Signal'] = 0
a1.loc[(a1['MA_10'] < a1['MA_20']), 'Close_Signal'] = 1
a1.index=a1['Date']
for index, row in a1.iterrows():
    if row['Close_Signal'] == 1:
        print(f"Closing buy position on {index.date()} at price {row['Close']}")

    

print('Closing signal for  sell position on TSLA Data\n\n\n\n')
a1['MA_5'] = a1['Close'].rolling(window=5).mean()
a1['MA_10'] = a1['Close'].rolling(window=10).mean()

a1['Close_Signal'] = 0
a1.loc[(a1['MA_5'] > a1['MA_10']) , 'Close_Signal'] = 1
for index, row in a1.iterrows():
    if row['Close_Signal'] == 1:
     print(f"Closing sell position on {row['Date'].date()} at price {row['Close']}")

if(a2.shape[0]>=200):
    a2['MA_20'] = a2['Close'].rolling(window=20).mean()
    a2['MA_200'] = a2['Close'].rolling(window=200).mean()

    a2['Sell_Signal'] = 0
    a2.loc[(a2['MA_20'] < a2['MA_200']) , 'Sell_Signal'] = 1
    plt.figure(figsize=(12, 6))
    plt.plot(a2.index, a2['MA_20'], label='20-day MA')
    plt.plot(a2.index, a2['MA_200'], label='200-day MA')
    plt.scatter(a2[a2['Sell_Signal'] == 1].index, a2['MA_20'][a2['Sell_Signal'] == 1], marker='v', color='r', label='Sell Signal')
    plt.title('OHLC Data with Moving Averages and Sell Signals on MARA Data')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()
    if(a2.shape[0]>=500):
        a2['MA_50'] = a2['Close'].rolling(window=50).mean()
        a2['MA_500'] = (a2['Close']).rolling(window=500).mean()
        a2['Signal'] = 0

        a2.loc[a2['MA_50'] >a2['MA_500'], 'Signal'] = 1
        plt.figure(figsize=(12, 6))
        plt.plot(a2.index, a2['MA_50'], label='50-day MA')
        plt.plot(a2.index, a2['MA_500'], label='500-day MA')
        plt.plot(a2[a2['Signal'] == 1].index, a2['MA_50'][a2['Signal'] == 1], '^', markersize=10, color='g', lw=0, label='Buy Signal')
        plt.title('OHLC Data with Moving Averages and Buy Signal on MARA Data')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.show()
print('Closing signal for buy position on MARA Data\n\n\n\n')
a2['MA_10'] = a2['Close'].rolling(window=10).mean()
a2['MA_20'] = a2['Close'].rolling(window=20).mean()

a2['Close_Signal'] = 0
a2.loc[(a2['MA_10'] < a2['MA_20']) , 'Close_Signal'] = 1
a2.index=a2['Date']
for index, row in a2.iterrows():
    if row['Close_Signal'] == 1:
        print(f"Closing buy position on {index.date()} at price {row['Close']}")

    

print('\n\n\n\nClosing signal for  sell position on MARA Data\n\n\n\n')

a2['MA_5'] = a2['Close'].rolling(window=5).mean()
a2['MA_10'] = a2['Close'].rolling(window=10).mean()

a2['Close_Signal'] = 0
a2.loc[(a2['MA_5'] > a2['MA_10']), 'Close_Signal'] = 1

for index, row in a2.iterrows():
    if row['Close_Signal'] == 1:
        print(f"Closing sell position on {row['Date'].date()} at price {row['Close']}")
            

if(a3.shape[0]>=200):
    a3['MA_20'] = a3['Close'].rolling(window=20).mean()
    a3['MA_200'] = a3['Close'].rolling(window=200).mean()

    a3['Sell_Signal'] = 0
    a3.loc[(a3['MA_20'] < a3['MA_200']) , 'Sell_Signal'] = 1
    plt.figure(figsize=(12, 6))
    plt.plot(a3.index, a3['MA_20'], label='20-day MA')
    plt.plot(a3.index, a3['MA_200'], label='200-day MA')
    plt.scatter(a3[a3['Sell_Signal'] == 1].index, a3['MA_20'][a3['Sell_Signal'] == 1], marker='v', color='r', label='Sell Signal')
    plt.title('OHLC Data with Moving Averages and Sell Signals on AAPL Data')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()
    if(a3.shape[0]>=500):
        a3['MA_50'] = a3['Close'].rolling(window=50).mean()
        a3['MA_500'] = (a3['Close']).rolling(window=500).mean()
        a3['Signal'] = 0

        a3.loc[a3['MA_50'] >a3['MA_500'], 'Signal'] = 1
        plt.figure(figsize=(12, 6))
        plt.plot(a3.index, a3['MA_50'], label='50-day MA')
        plt.plot(a3.index, a3['MA_500'], label='500-day MA')
        plt.plot(a3[a3['Signal'] == 1].index, a3['MA_50'][a3['Signal'] == 1], '^', markersize=10, color='g', lw=0, label='Buy Signal')
        plt.title('OHLC Data with Moving Averages and Buy Signal on AAPL Data')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.show()
print('Closing signal for  buy position on AAPL Data\n\n\n\n')
a3['MA_10'] = a3['Close'].rolling(window=10).mean()
a3['MA_20'] = a3['Close'].rolling(window=20).mean()

a3['Close_Signal'] = 0
a3.loc[(a3['MA_10'] < a3['MA_20']) , 'Close_Signal'] = 1
a3.index=a3['Date']
for index, row in a3.iterrows():
        if row['Close_Signal'] == 1:
            print(f"Closing buy position on {index.date()} at price {row['Close']}")

    

print('\n\n\n\nClosing signal for  sell position on AAPL Data\n\n\n\n')

a3['MA_5'] = a3['Close'].rolling(window=5).mean()
a3['MA_10'] = a3['Close'].rolling(window=10).mean()
a3['Close_Signal'] = 0
a3.loc[(a3['MA_5'] > a3['MA_10']) , 'Close_Signal'] = 1

for index, row in a3.iterrows():
    if row['Close_Signal'] == 1:
        print(f"Closing sell position on {row['Date'].date()} at price {row['Close']}")
            

        

if(a4.shape[0]>=200):
    a4['MA_20'] = a4['Close'].rolling(window=20).mean()
    a4['MA_200'] = a4['Close'].rolling(window=200).mean()

    a4['Sell_Signal'] = 0
    a4.loc[(a4['MA_20'] < a4['MA_200']) , 'Sell_Signal'] = 1
    plt.figure(figsize=(12, 6))
    plt.plot(a4.index, a4['MA_20'], label='20-day MA')
    plt.plot(a4.index, a4['MA_200'], label='200-day MA')
    plt.scatter(a4[a4['Sell_Signal'] == 1].index, a4['MA_20'][a4['Sell_Signal'] == 1], marker='v', color='r', label='Sell Signal')
    plt.title('OHLC Data with Moving Averages and Sell Signals on HBD Data')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()
    if(a4.shape[0]>=500):
        a4['MA_50'] = a4['Close'].rolling(window=50).mean()
        a4['MA_500'] = (a4['Close']).rolling(window=500).mean()
        a4['Signal'] = 0

        a4.loc[a4['MA_50'] >a4['MA_500'], 'Signal'] = 1
        plt.figure(figsize=(12, 6))
        plt.plot(a4.index, a4['MA_50'], label='50-day MA')
        plt.plot(a4.index, a4['MA_500'], label='500-day MA')
        plt.plot(a4[a4['Signal'] == 1].index, a4['MA_50'][a4['Signal'] == 1], '^', markersize=10, color='g', lw=0, label='Buy Signal')
        plt.title('OHLC Data with Moving Averages and Buy Signal on  HDB Data')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.show()
print('Closing signal for  buy position on HBD Data\n\n\n\n')
a4['MA_10'] = a4['Close'].rolling(window=10).mean()
a4['MA_20'] = a4['Close'].rolling(window=20).mean()

a4['Close_Signal'] = 0
a4.loc[(a4['MA_10'] < a4['MA_20']) , 'Close_Signal'] = 1
a4.index=a4['Date']
for index, row in a4.iterrows():
    if row['Close_Signal'] == 1:
        print(f"Closing buy position on {index.date()} at price {row['Close']}")

    

print('\n\n\n\nClosing signal for  sell position on HDB Data\n\n\n\n')

a4['MA_5'] = a4['Close'].rolling(window=5).mean()
a4['MA_10'] = a4['Close'].rolling(window=10).mean()

a4['Close_Signal'] = 0
a4.loc[(a4['MA_5'] > a4['MA_10']), 'Close_Signal'] = 1

for index, row in a4.iterrows():
    if row['Close_Signal'] == 1:
        print(f"Closing sell position on {row['Date'].date()} at price {row['Close']}")
            

        

if(a5.shape[0]>=200):
    a5['MA_20'] = a5['Close'].rolling(window=20).mean()
    a5['MA_200'] = a5['Close'].rolling(window=200).mean()

    a5['Sell_Signal'] = 0
    a5.loc[(a5['MA_20'] < a5['MA_200']) , 'Sell_Signal'] = 1
    plt.figure(figsize=(12, 6))
    plt.plot(a5.index, a5['MA_20'], label='20-day MA')
    plt.plot(a5.index, a5['MA_200'], label='200-day MA')
    plt.scatter(a5[a5['Sell_Signal'] == 1].index, a5['MA_20'][a5['Sell_Signal'] == 1], marker='v', color='r', label='Sell Signal')
    plt.title('OHLC Data with Moving Averages and Sell Signals on INR=X Data')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()
    if(a5.shape[0]>=500):
        a5['MA_50'] = a5['Close'].rolling(window=50).mean()
        a5['MA_500'] = (a5['Close']).rolling(window=500).mean()
        a5['Signal'] = 0

        a5.loc[a5['MA_50'] >a5['MA_500'], 'Signal'] = 1
        plt.figure(figsize=(12, 6))
        plt.plot(a5.index, a5['MA_50'], label='50-day MA')
        plt.plot(a5.index, a5['MA_500'], label='500-day MA')
        plt.plot(a5[a5['Signal'] == 1].index, a5['MA_50'][a5['Signal'] == 1], '^', markersize=10, color='g', lw=0, label='Buy Signal')
        plt.title('OHLC Data with Moving Averages and Buy Signal on INR=X Data')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.show()
print('Closing signal for  buy position on INR=X Data\n\n\n\n')
a5['MA_10'] = a5['Close'].rolling(window=10).mean()
a5['MA_20'] = a5['Close'].rolling(window=20).mean()

a5['Close_Signal'] = 0
a5.loc[(a5['MA_10'] < a5['MA_20']) , 'Close_Signal'] = 1
a5.index=a5['Date']
for index, row in a5.iterrows():
    if row['Close_Signal'] == 1:
        print(f"Closing buy position on {index.date()} at price {row['Close']}")

    

print('\n\n\n\nClosing signal for  sell position on INR=X Data\n\n\n\n')
a5['MA_5'] = a5['Close'].rolling(window=5).mean()
a5['MA_10'] = a5['Close'].rolling(window=10).mean()

a5['Close_Signal'] = 0
a5.loc[(a5['MA_5'] > a5['MA_10']) , 'Close_Signal'] = 1

for index, row in a5.iterrows():
    if row['Close_Signal'] == 1:
        print(f"Closing sell position on {row['Date'].date()} at price {row['Close']}")
            

        

if(a6.shape[0]>=200):
    a6['MA_20'] = a6['Close'].rolling(window=20).mean()
    a6['MA_200'] = a6['Close'].rolling(window=200).mean()

    a6['Sell_Signal'] = 0
    a6.loc[(a6['MA_20'] < a6['MA_200']) , 'Sell_Signal'] = 1
    plt.figure(figsize=(12, 6))
    plt.plot(a6.index, a6['MA_20'], label='20-day MA')
    plt.plot(a6.index, a6['MA_200'], label='200-day MA')
    plt.scatter(a6[a6['Sell_Signal'] == 1].index, a6['MA_20'][a6['Sell_Signal'] == 1], marker='v', color='r', label='Sell Signal')
    plt.title('OHLC Data with Moving Averages and Sell Signals on JIOFIN.NS Data')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()
    if(a6.shape[0]>=500):
        a6['MA_50'] = a6['Close'].rolling(window=50).mean()
        a6['MA_500'] = (a6['Close']).rolling(window=500).mean()
        a6['Signal'] = 0

        a6.loc[a6['MA_50'] >a6['MA_500'], 'Signal'] = 1
        plt.figure(figsize=(12, 6))
        plt.plot(a6.index, a6['MA_50'], label='50-day MA')
        plt.plot(a6.index, a6['MA_500'], label='500-day MA')
        plt.plot(a6[a6['Signal'] == 1].index, a6['MA_50'][a6['Signal'] == 1], '^', markersize=10, color='g', lw=0, label='Buy Signal')
        plt.title('OHLC Data with Moving Averages and Buy Signal on JIOFIN.NS Data')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.show()
print('Closing signal for  buy position on JIOFIN.Ns Data\n\n\n\n')
a6['MA_10'] = a6['Close'].rolling(window=10).mean()
a6['MA_20'] = a6['Close'].rolling(window=20).mean()

a6['Close_Signal'] = 0
a6.loc[(a6['MA_10'] < a6['MA_20']) , 'Close_Signal'] = 1
a6.index=a6['Date']
for index, row in a6.iterrows():
    if row['Close_Signal'] == 1:
        print(f"Closing buy position on {index.date()} at price {row['Close']}")

    

print('\n\n\n\nClosing signal for  sell position on JIOFIN.Ns Data\n\n\n\n')

a6['MA_5'] = a6['Close'].rolling(window=5).mean()
a6['MA_10'] = a6['Close'].rolling(window=10).mean()

a6['Close_Signal'] = 0
a6.loc[(a6['MA_5'] > a6['MA_10']) , 'Close_Signal'] = 1

for index, row in a6.iterrows():
    if row['Close_Signal'] == 1:
         print(f"Closing sell position on {row['Date'].date()} at price {row['Close']}")
            

        

if(a7.shape[0]>=200):
    a7['MA_20'] = a7['Close'].rolling(window=20).mean()
    a7['MA_200'] = a7['Close'].rolling(window=200).mean()

    a7['Sell_Signal'] = 0
    a7.loc[(a7['MA_20'] < a7['MA_200']) , 'Sell_Signal'] = 1
    plt.figure(figsize=(12, 6))
    plt.plot(a7.index, a7['MA_20'], label='20-day MA')
    plt.plot(a7.index, a7['MA_200'], label='200-day MA')
    plt.scatter(a7[a7['Sell_Signal'] == 1].index, a7['MA_20'][a7['Sell_Signal'] == 1], marker='v', color='r', label='Sell Signal')
    plt.title('OHLC Data with Moving Averages and Sell Signals on TATAMOTORS.NS Data')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()
    if(a7.shape[0]>=500):
        a7['MA_50'] = a7['Close'].rolling(window=50).mean()
        a7['MA_500'] = (a7['Close']).rolling(window=500).mean()
        a7['Signal'] = 0

        a7.loc[a7['MA_50'] >a7['MA_500'], 'Signal'] = 1
        plt.figure(figsize=(12, 6))
        plt.plot(a7.index, a7['MA_50'], label='50-day MA')
        plt.plot(a7.index, a7['MA_500'], label='500-day MA')
        plt.plot(a7[a7['Signal'] == 1].index, a7['MA_50'][a7['Signal'] == 1], '^', markersize=10, color='g', lw=0, label='Buy Signal')
        plt.title('OHLC Data with Moving Averages and Buy Signal on TATAMOTORS.NS Data')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.show()
    
print('Closing signal for  buy position on TATAMOTORS.NS Data\n\n\n\n')
a7['MA_10'] = a7['Close'].rolling(window=10).mean()
a7['MA_20'] = a7['Close'].rolling(window=20).mean()

a7['Close_Signal'] = 0
a7.loc[(a7['MA_10'] < a7['MA_20']) , 'Close_Signal'] = 1
a7.index=a7['Date']
for index, row in a7.iterrows():
    if row['Close_Signal'] == 1:
        print(f"Closing buy position on {index.date()} at price {row['Close']}")

    

print('\n\n\n\nClosing signal for  sell position on TATAMOTORS.NS Data\n\n\n\n')
a7['MA_5'] = a7['Close'].rolling(window=5).mean()
a7['MA_10'] = a7['Close'].rolling(window=10).mean()

a7['Close_Signal'] = 0
a7.loc[(a7['MA_5'] > a7['MA_10']), 'Close_Signal'] = 1

for index, row in a7.iterrows():
    if row['Close_Signal'] == 1:
        print(f"Closing sell position on {row['Date'].date()} at price {row['Close']}")
            

        


     

        

