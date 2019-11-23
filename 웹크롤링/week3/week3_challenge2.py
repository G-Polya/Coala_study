import requests
from bs4 import BeautifulSoup

for page in range(1,4):
    raw = requests.get('https://news.ycombinator.com/news?p='+str(page),
                       headers={'User-Agent': 'Mozilla/5.0'})


    html = BeautifulSoup(raw.text, 'html.parser')

    newspaper = html.select('tr.athing')

    for news in newspaper:
        title = news.select_one('a.storylink').text
        rank = news.select_one('span.rank').text

        print(rank, title)