import time

import requests
from bs4 import BeautifulSoup

ticker = "INFY"
url = f"https://www.google.com/finance/quote/{ticker}:NSE"
resp = requests.get(url)

for i in range(3):
    soup = BeautifulSoup(resp.text, 'html.parser')

    price_class = "YMlKec fxKbKc"
    price = soup.find(class_=price_class).text
    float_price = float(price.strip()[1:].replace(",", ""))
    print(float_price)
    time.sleep(10)
