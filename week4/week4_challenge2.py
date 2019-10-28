import requests
from bs4 import BeautifulSoup

import openpyxl

keyword = input('검색어를 입력하세요: ')

try:
    wb = openpyxl.load_workbook('naver_News.xlsx')
    sheet = wb.active
    print("불러오기 완료")
except:
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.append(["검색어","제목","언론사"])
    print("새로 파일 생성완료")

for page in range(1,101,10):
    raw = requests.get('https://search.naver.com/search.naver?where=news&query='+keyword+'&start='+str(page),
                       headers = {'User-Agent':'Mozilla/5.0'})

    html = BeautifulSoup(raw.text,'html.parser')

    articles = html.select('ul.type01 > li')

    #2. 기사데이터 수집
    for ar in articles:
        title = ar.select_one('a._sp_each_title').text
        source = ar.select_one('span._sp_each_source').text



        sheet.append([keyword,title, source])


wb.save('naver_News.xlsx')