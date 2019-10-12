import requests
from bs4 import BeautifulSoup

raw = requests.get('https://tv.naver.com/r/')
html = BeautifulSoup(raw.text, 'html.parser')

#1. 컨테이너 수집하기
container = html.select('dl.cds_info') # 파싱된 코드에서 div.inner를 골라줘!

# #2. 세부데이터 수집
# title = container[0].select_one('dt.title')
# chn = container[0].select_one('dd.chn')
# hit = container[0].select_one('span.hit')
# like = container[0].select_one('span.like')
#
# print(title.text.strip())
# print(chn.text.strip())
# print(hit.text.strip())
# print(like.text.strip())

#3. 컨테이너 반복하며 수집하기
for cont in container:
    title = cont.select_one('dt.title')
    chn = cont.select_one('dd.chn')
    hit = cont.select_one('span.hit')
    like = cont.select_one('span.like')

    print(title.text.strip())
    print(chn.text.strip())
    print(hit.text.strip())
    print(like.text.strip())
    print('-' * 50)
