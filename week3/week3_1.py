import requests
from bs4 import BeautifulSoup

raw = requests.get('https://tv.naver.com/r/')
#print(raw.text) 소스코드의 단순한 나열, 아무의미없다

html = BeautifulSoup(raw.text, 'html.parser')
# print(html) # html 소스코드라는 의미. 태그기준으로 나누었다

# 1~3위 컨테이너 : div.inner
# 제목 : dt.title
# 채널명 : dd.chn
# 재생수 : span.hit
# 좋아요 수 : span.like

#1. 컨테이너 수집
container = html.select('div.inner') # 파싱된 코드에서 div.inner를 골라줘!
#print(container[0])

#2. 영상데이터 수집
# title = container[0].select_one('dt.title') # 한 컨테이너 안에 dt.title은 하나밖에 없기 때문에 select_one
# chn = container[0].select_one('dd.chn')
# hit = container[0].select_one('span.hit')
# like = container[0].select_one('span.like')
# print(title.text.strip())
# print(chn.text.strip())
# print(hit.text.strip())
# print(like.text.strip())

#3. 반복하기

for cont in container:
    title = cont.select_one('dt.title').text.strip()  # 한 컨테이너 안에 dt.title은 하나밖에 없기 때문에 select_one
    chn = cont.select_one('dd.chn').text.strip()
    hit = cont.select_one('span.hit').text.strip()
    like = cont.select_one('span.like').text.strip()
    print(title)
    print(chn)
    print(hit)
    print(like)
    print('=' * 50)
