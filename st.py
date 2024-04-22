import numpy as np
import pandas as pd
import requests
import xlsxwriter
import math


symbol ='AAPL'
api_url = 'https://sandbox.iexapis.com/stock/{symbol}/quote/?token={IEX_CLOUD_API_TOKEN}'
print(api_url)
data = requests.get(api_url)
print(data.status_code)