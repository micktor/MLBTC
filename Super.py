#!/usr/bin/env python
# coding: utf-8

# # Imports

# In[1]:


import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from keras import Sequential
from keras.layers import Dense, LSTM, Dropout, CuDNNLSTM


# # Collect CSV's

# In[13]:


BidAskSpread = pd.read_csv('30dbidaskspreadhourly.csv')
BidAskSum = pd.read_csv('30dbidasksumhourly.csv')
Price = pd.read_csv('30dpricehourly.csv')
TradesPerMin = pd.read_csv('30dtpmhourly.csv')
Volatility = pd.read_csv('30dvolatilityhourly.csv')
Volume = pd.read_csv('30dvolumehourly.csv')


# In[34]:


BidAskSpread_bitx = BidAskSpread.iloc[:,[1]]
BidAskSpread_bitfinex = BidAskSpread.iloc[:,[3]]
BidAskSpread_bitstamp = BidAskSpread.iloc[:,[4]]
BidAskSpread_cexio = BidAskSpread.iloc[:,[5]]
BidAskSpread_coinbase = BidAskSpread.iloc[:,[6]]
BidAskSpread_exmo = BidAskSpread.iloc[:,[7]]
BidAskSpread_gemini = BidAskSpread.iloc[:,[8]]
BidAskSpread_itbit = BidAskSpread.iloc[:,[9]]
BidAskSpread_kraken = BidAskSpread.iloc[:,[10]]


# In[46]:


BidAskSum_asks = BidAskSum.iloc[:,[1]]
BidAskSum_bids = BidAskSum.iloc[:,[2]]


# In[47]:


Price_bitx = Price.iloc[:,[1]]
Price_bitfinex = Price.iloc[:,[3]]
Price_bitstamp = Price.iloc[:,[4]]
Price_cexio = Price.iloc[:,[5]]
Price_coinbase = Price.iloc[:,[6]]
Price_exmo = Price.iloc[:,[7]]
Price_gemini = Price.iloc[:,[8]]
Price_itbit = Price.iloc[:,[9]]
Price_kraken = Price.iloc[:,[10]]


# In[56]:


TradesPerMin_bitx = TradesPerMin.iloc[:,[1]]
TradesPerMin_bitfinex = TradesPerMin.iloc[:,[2]]
TradesPerMin_bitflyer = TradesPerMin.iloc[:,[3]]
TradesPerMin_bithumb = TradesPerMin.iloc[:,[4]]
TradesPerMin_bitstamp = TradesPerMin.iloc[:,[5]]
TradesPerMin_coinbase = TradesPerMin.iloc[:,[6]]
TradesPerMin_exmo = TradesPerMin.iloc[:,[7]]
TradesPerMin_gemini = TradesPerMin.iloc[:,[8]]
TradesPerMin_kraken = TradesPerMin.iloc[:,[9]]
TradesPerMin_others = TradesPerMin.iloc[:,[10]]


# In[62]:


Volatility_bitx = Volatility.iloc[:,[1]]
Volatility_bitfinex = Volatility.iloc[:,[2]]
Volatility_bitstamp = Volatility.iloc[:,[3]]
Volatility_cexio = Volatility.iloc[:,[4]]
Volatility_coinbase = Volatility.iloc[:,[5]]
Volatility_exmo = Volatility.iloc[:,[6]]
Volatility_gemini = Volatility.iloc[:,[7]]
Volatility_itbit = Volatility.iloc[:,[8]]
Volatility_kraken = Volatility.iloc[:,[9]]


# In[66]:


Volume_bitx = Volume.iloc[:,[1]]
Volume_bitbay = Volume.iloc[:,[2]]
Volume_bitfinex = Volume.iloc[:,[3]]
Volume_bitflyer = Volume.iloc[:,[4]]
Volume_bithumb = Volume.iloc[:,[5]]
Volume_bitstamp = Volume.iloc[:,[6]]
Volume_coinbase = Volume.iloc[:,[7]]
Volume_gemini = Volume.iloc[:,[8]]
Volume_kraken = Volume.iloc[:,[9]]
Volume_others = Volume.iloc[:,[10]]


# In[ ]:




