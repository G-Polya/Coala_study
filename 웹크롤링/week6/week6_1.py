import requests
from bs4 import BeautifulSoup

raw = requests.get("https://map.naver.com/",
                   headers={"User-Agent" : "Mozilla/5.0"})
html = BeautifulSoup(raw.text,'html.parser')

# 컨테이너 search-item-place.item_search
stores = html.select(("search-item-place.item_search"))
print(stores)
# 가게이름
