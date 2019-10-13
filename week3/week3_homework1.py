import requests
from bs4 import BeautifulSoup

for page in range(1,101,20):
    raw = requests.get('https://series.naver.com/ebook/top100List.nhn?page='+str(page),
                       headers = {'User-Agent':'Mozilla/5.0'})

    html = BeautifulSoup(raw.text,'html.parser')


    books = html.select('ul.lst_thum.v1 li')

    for book in books:
        title = book.select_one('ul.lst_thum.v1 li a strong').text
        author = book.select_one('ul.lst_thum.v1 li a span.writer').text

        print(title, author)