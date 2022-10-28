import requests
import pandas as pd
from typing import List
import time
from requests.models import to_key_val_list
import os
import tools

db = tools.CSVManager.load('FIIs.csv')

for i in range(len(db['NameFIIs'])):


    nameFIIs =  db["NameFIIs"][i]
    url = f"https://api.hgbrasil.com/finance/stock_price?key=YOURKEY&symbol={nameFIIs}"

    values = requests.get(url).json()
    price = values["results"][nameFIIs]['price']

    print(f'{nameFIIs} R${db["CurrentPrice"][i]} --> R${price} ')
    print('-'*10)

    list = db['CurrentPrice']
    list[i] = price
    df = pd.DataFrame(db)
    df.to_csv('FIIs.csv', index=False)
