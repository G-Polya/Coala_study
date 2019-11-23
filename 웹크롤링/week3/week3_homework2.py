import requests
from bs4 import BeautifulSoup


for page in range(1, 4):
    raw = requests.get('https://search.daum.net/search?w=news&nil_search=btn&DA=NTB&enc=utf8&cluster=y&cluster_page=1&q=코알라&p='+str(page))

    html = BeautifulSoup(raw.text,'html.parser')

    news_container = html.select('div.coll_cont>ul>li')

    for news in news_container:
        title = news.select_one('a.f_link_b').text
        news_abstract = news.select_one('p.f_eb.desc').text
        print(title, news_abstract)
        print('-'*50)