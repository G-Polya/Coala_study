import requests
from bs4 import BeautifulSoup
import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active
sheet.append(['제목','채널명','재생수','좋아요수'])


raw = requests.get('https://tv.naver.com/r/')

html = BeautifulSoup(raw.text, 'html.parser')
container = html.select('div.inner') # 파싱된 코드에서 div.inner를 골라줘!



for cont in container:
    title = cont.select_one('dt.title').text.strip()  # 한 컨테이너 안에 dt.title은 하나밖에 없기 때문에 select_one
    chn = cont.select_one('dd.chn').text.strip()
    hit = cont.select_one('span.hit').text.strip()
    like = cont.select_one('span.like').text.strip()

    hit = hit.replace('재생 수','')
    like = like.replace('좋아요 수','')
    
    sheet.append([title,chn,hit,like])

wb.save('navertv.xlsx')