import requests
from bs4 import BeautifulSoup

#csv 형식으로 저장하기
f = open('navertv.csv','w',encoding='UTF-8')
f.write('제목, 채널명, 재생수, 좋아요\n')

raw = requests.get('https://tv.naver.com/r/')

html = BeautifulSoup(raw.text, 'html.parser')

container = html.select('div.inner') # 파싱된 코드에서 div.inner를 골라줘!


for cont in container:
    title = cont.select_one('dt.title').text.strip()  # 한 컨테이너 안에 dt.title은 하나밖에 없기 때문에 select_one
    chn = cont.select_one('dd.chn').text.strip()
    hit = cont.select_one('span.hit').text.strip()
    like = cont.select_one('span.like').text.strip()
    title = title.replace(',','')
    chn = chn.replace(',','')
    hit = hit.replace(',', '')
    like = like.replace(',', '')

    hit = hit.replace('재생 수','')
    like=like[5:]

    #hit = hit.replace("재생 수","")
    #like = like[5:]


    f.write(title+','+chn+','+hit+','+like+'\n')

f.close()