import requests
import json
import csv
import io
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

Volume_URL = "https://data.bitcoinity.org/export_data.csv?c=e&data_type=volume&r=hour&t=b&timespan=30d"
Price_URL = "https://data.bitcoinity.org/export_data.csv?c=e&currency=USD&data_type=price&r=hour&t=l&timespan=30d"
MkCap_URL = "https://data.bitcoinity.org/export_data.csv?currency=USD&data_type=market_cap&t=l&timespan=30d"
TradesPerMin_URL = "https://data.bitcoinity.org/export_data.csv?c=e&data_type=tradespm&r=hour&t=a&timespan=30d"
Volatility_URL = "https://data.bitcoinity.org/export_data.csv?c=e&currency=USD&data_type=volatility&f=m10&g=15&r=hour&st=log&t=l&timespan=30d"
BidAskSpread_URL = "https://data.bitcoinity.org/export_data.csv?c=e&currency=USD&data_type=spread&f=m10&r=hour&st=log&t=l&timespan=30d"
BidAskSum_URL = "https://data.bitcoinity.org/export_data.csv?bp=10&bu=c&currency=USD&data_type=bidask_sum&exchange=coinbase&r=hour&t=m&timespan=30d"

URLs = [Volume_URL,
        Price_URL,
        MkCap_URL ,
        TradesPerMin_URL,
        Volatility_URL,
        BidAskSpread_URL,
        BidAskSum_URL]

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
    URL_dict[URL_Name]=c.iloc[-719:]
    print(f"Converting {URL_Name} CSV to a Pandas DataFrame")

print(URL_dict.get("BidAskSum"))

