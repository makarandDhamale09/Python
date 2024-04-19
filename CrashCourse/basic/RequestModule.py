import requests
from bs4 import BeautifulSoup

response = requests.get("https://dev.to/ericchapman/my-beloved-django-cheat-sheet-2056")
# print(response.text)

soup = BeautifulSoup(response.text, "html.parser")
print(soup.prettify())
print("-------------")
for heading in soup.find_all("h1"):
    print(heading.text)
