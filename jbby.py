import requests
import json
import csv
import io
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

URL_dict = {"Volume" : "https://data.bitcoinity.org/export_data.csv?c=e&data_type=volume&r=hour&t=b&timespan=30d",
            "Price" : "https://data.bitcoinity.org/export_data.csv?c=e&currency=USD&data_type=price&r=hour&t=l&timespan=30d",
            "MkCap" : "https://data.bitcoinity.org/export_data.csv?currency=USD&data_type=market_cap&t=l&timespan=30d",
            "TradesPerMin" : "https://data.bitcoinity.org/export_data.csv?c=e&data_type=tradespm&r=hour&t=a&timespan=30d",
            "Volatility" : "https://data.bitcoinity.org/export_data.csv?c=e&currency=USD&data_type=volatility&f=m10&g=15&r=hour&st=log&t=l&timespan=30d",
            "BidAskSpread" : "https://data.bitcoinity.org/export_data.csv?c=e&currency=USD&data_type=spread&f=m10&r=hour&st=log&t=l&timespan=30d",
            "BidAskSum" : "https://data.bitcoinity.org/export_data.csv?bp=10&bu=c&currency=USD&data_type=bidask_sum&exchange=coinbase&r=hour&t=m&timespan=30d",
            }

for URL_Name, Link in URL_dict.items():
    r = requests.get(Link)
    r = r.content.decode('utf-8')
    c=pd.read_csv(io.StringIO(r))
    URL_dict[URL_Name]=c.iloc[-716:]
    print(f"Converting {URL_Name} CSV to a Pandas DataFrame")



####################################################################################



BidAskSpread_bitx = URL_dict.get("BidAskSpread").iloc[:,[1]]
BidAskSpread_bitfinex = URL_dict.get("BidAskSpread").iloc[:,[3]]
BidAskSpread_bitstamp = URL_dict.get("BidAskSpread").iloc[:,[4]]
BidAskSpread_cexio = URL_dict.get("BidAskSpread").iloc[:,[5]]
BidAskSpread_coinbase = URL_dict.get("BidAskSpread").iloc[:,[6]]
BidAskSpread_exmo = URL_dict.get("BidAskSpread").iloc[:,[7]]
BidAskSpread_gemini = URL_dict.get("BidAskSpread").iloc[:,[8]]
BidAskSpread_itbit = URL_dict.get("BidAskSpread").iloc[:,[9]]
BidAskSpread_kraken = URL_dict.get("BidAskSpread").iloc[:,[10]]

BidAskSum_asks = URL_dict.get("BidAskSum").iloc[:,[1]]
BidAskSum_bids = URL_dict.get("BidAskSum").iloc[:,[2]]
BidAskSum_price = URL_dict.get("BidAskSum").iloc[:,[3]]

Price_bitx = URL_dict.get("Price").iloc[:,[1]]
Price_bitfinex = URL_dict.get("Price").iloc[:,[3]]
Price_bitstamp = URL_dict.get("Price").iloc[:,[4]]
Price_cexio = URL_dict.get("Price").iloc[:,[5]]
Price_coinbase = URL_dict.get("Price").iloc[:,[6]]
Price_exmo = URL_dict.get("Price").iloc[:,[7]]
Price_gemini = URL_dict.get("Price").iloc[:,[8]]
Price_itbit = URL_dict.get("Price").iloc[:,[9]]
Price_kraken = URL_dict.get("Price").iloc[:,[10]]

TradesPerMin_bitx = URL_dict.get("TradesPerMin").iloc[:,[1]]
TradesPerMin_bitfinex = URL_dict.get("TradesPerMin").iloc[:,[2]]
TradesPerMin_bitflyer = URL_dict.get("TradesPerMin").iloc[:,[3]]
TradesPerMin_bithumb = URL_dict.get("TradesPerMin").iloc[:,[4]]
TradesPerMin_bitstamp = URL_dict.get("TradesPerMin").iloc[:,[5]]
TradesPerMin_coinbase = URL_dict.get("TradesPerMin").iloc[:,[6]]
TradesPerMin_exmo = URL_dict.get("TradesPerMin").iloc[:,[7]]
TradesPerMin_gemini = URL_dict.get("TradesPerMin").iloc[:,[8]]
TradesPerMin_kraken = URL_dict.get("TradesPerMin").iloc[:,[9]]
TradesPerMin_others = URL_dict.get("TradesPerMin").iloc[:,[10]]

Volatility_bitx = URL_dict.get("Volatility").iloc[:,[1]]
Volatility_bitfinex = URL_dict.get("Volatility").iloc[:,[2]]
Volatility_bitstamp = URL_dict.get("Volatility").iloc[:,[3]]
Volatility_cexio = URL_dict.get("Volatility").iloc[:,[4]]
Volatility_coinbase = URL_dict.get("Volatility").iloc[:,[5]]
Volatility_exmo = URL_dict.get("Volatility").iloc[:,[6]]
Volatility_gemini = URL_dict.get("Volatility").iloc[:,[7]]
Volatility_itbit = URL_dict.get("Volatility").iloc[:,[8]]
Volatility_kraken = URL_dict.get("Volatility").iloc[:,[9]]

Volume_bitx = URL_dict.get("Volume").iloc[:,[1]]
Volume_bitbay = URL_dict.get("Volume").iloc[:,[2]]
Volume_bitfinex = URL_dict.get("Volume").iloc[:,[3]]
Volume_bitflyer = URL_dict.get("Volume").iloc[:,[4]]
Volume_bithumb = URL_dict.get("Volume").iloc[:,[5]]
Volume_bitstamp = URL_dict.get("Volume").iloc[:,[6]]
Volume_coinbase = URL_dict.get("Volume").iloc[:,[7]]
Volume_gemini = URL_dict.get("Volume").iloc[:,[8]]
Volume_kraken = URL_dict.get("Volume").iloc[:,[9]]
Volume_others = URL_dict.get("Volume").iloc[:,[10]]



##################################################################################################


DataSets = [BidAskSpread_bitx,
            BidAskSpread_bitfinex,
            BidAskSpread_bitstamp,
            BidAskSpread_cexio,
            BidAskSpread_coinbase,
            BidAskSpread_exmo,
            BidAskSpread_gemini,
            BidAskSpread_itbit,
            BidAskSpread_kraken,
            BidAskSum_asks,
            BidAskSum_bids,
            BidAskSum_price,
            Price_bitx,
            Price_bitfinex,
            Price_bitstamp,
            Price_cexio,
            Price_coinbase,
            Price_exmo,
            Price_gemini,
            Price_itbit,
            Price_kraken,
            TradesPerMin_bitx,
            TradesPerMin_bitfinex,
            TradesPerMin_bitflyer,
            TradesPerMin_bithumb,
            TradesPerMin_bitstamp,
            TradesPerMin_coinbase,
            TradesPerMin_exmo,
            TradesPerMin_gemini,
            TradesPerMin_kraken,
            TradesPerMin_others,
            Volatility_bitx,
            Volatility_bitfinex,
            Volatility_bitstamp,
            Volatility_cexio,
            Volatility_coinbase,
            Volatility_exmo,
            Volatility_gemini,
            Volatility_itbit,
            Volatility_kraken,
            Volume_bitx,
            Volume_bitbay,
            Volume_bitfinex,
            Volume_bitflyer,
            Volume_bithumb,
            Volume_bitstamp,
            Volume_coinbase,
            Volume_gemini,
            Volume_kraken,
            Volume_others,
           ]

##################################################################################################


ConcatFrame = pd.concat(DataSets, axis=1, join='inner')
scaler = MinMaxScaler(feature_range=(0,1))
ConcatFrame = pd.DataFrame(scaler.fit_transform(ConcatFrame),columns = ConcatFrame.columns)
print(ConcatFrame)

X = []  
y = []  
for i in range(55, 715):  
    X.append(ConcatFrame.iloc[i-55:i, :])
    y.append(ConcatFrame.iloc[i, [0]])
    #print(f"iteration {i}")

X = np.stack(X)
y = np.stack(y)

print(X.shape)
print(y.shape)

##################################################################################################




model = Sequential()
model.add(CuDNNLSTM(units=50, return_sequences= True, input_shape=(660,55,50)))
model.add(Dropout(0.2))
model.add(CuDNNLSTM(units=50, return_sequences=True))
model.add(Dropout(0.2))
model.add(CuDNNLSTM(units=50))
model.add(Dropout(0.2))
model.add(Dense(units=1))
model.summary()

model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(X_train, y_train, epochs=200, batch_size=16)

