import requests
import json


class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


query = input("What type of news are you interested in?\n")
lang = input("In which Language\n")
url = (f"https://newsapi.org/v2/everything?q={query}&from=2024-04-19&language={lang}&searchIn=title,description&sortBy"
       f"=publishedAt&apiKey=71f3034c502249538a9817e9c47b2487")
resp = requests.get(url)

newsJson = json.loads(resp.text)
# print(newsJson)

for article in newsJson["articles"]:
    print(f"{color.PURPLE}Title :{color.END} {article["title"]}")
    print(f"{color.PURPLE}Description :{color.END} {article["description"]}")
    print("----------------------------")
