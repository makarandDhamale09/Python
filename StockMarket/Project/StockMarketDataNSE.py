# from nselib import capital_market
import requests
import pandas as pd

# data = capital_market.price_volume_and_deliverable_position_data(symbol='SBIN', from_date='19-04-2024', to_date='22-04-2024')
# print(data)

header = {
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0",
    "DNT": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/111.0.0.0 Safari/537.36",
    "Sec-Fetch-User": "?1", "Accept": "*/*", "Sec-Fetch-Site": "none", "Sec-Fetch-Mode": "navigate",
    "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "en-US,en;q=0.9,hi;q=0.8"
}


def nse_urlfetch(url):
    r_session = requests.session()
    nse_live = r_session.get("http://nseindia.com", headers=header)
    return r_session.get(url, headers=header)


def get_price_volume_and_deliverable_position_data(symbol: str, from_date: str, to_date: str):
    url = "https://www.nseindia.com/api/historical/securityArchives?"
    payload = f"from={from_date}&to={to_date}&symbol={symbol}&dataType=priceVolumeDeliverable&series=ALL&csv=true"
    try:
        data_text = nse_urlfetch(url + payload).text
        data_text = data_text.replace('\x82', '').replace('â¹', 'In Rs')
        with open('file.csv', 'w') as f:
            f.write(data_text)
        f.close()
    except Exception as e:
        raise Exception(f" Resource not available MSG: {e}")
    data_df = pd.read_csv('file.csv')
    data_df.columns = [name.replace(' ', '') for name in data_df.columns]
    return data_df


def get_data(symbol, from_date, to_date):
    url = "https://www.nseindia.com/api/historical/securityArchives?"
    payload = f"from={from_date}&to={to_date}&symbol={symbol}&dataType=priceVolumeDeliverable&series=ALL&csv=true"
    data_text = nse_urlfetch(url + payload).text
    print(data_text)
    data_text = data_text.replace('\x82', '').replace('â¹', 'In Rs').replace('ï»¿', '')
    # print(data_text)
    with open('file.csv', 'w') as f:
        f.write(data_text)
    f.close()
    data_df = pd.read_csv('file.csv')
    data_df.columns = [name.replace(' ', '') for name in data_df.columns]
    return data_df


data = get_data("INFY", "01-04-2024", "19-04-2024")
# print(type(data))
# print(data)
