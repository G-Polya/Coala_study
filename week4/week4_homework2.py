import requests
from bs4 import BeautifulSoup
import openpyxl
f = open('daumnews.csv','w')

f.write("기사제목, 기사요약,\n")

try:
    wb = openpyxl.load_workbook("daumnews.xlsx")
    sheet = wb.active
    print("기존파일에 추가")

except:
    wb = openpyxl.Workbook()
    sheet = wb.active
    print("새로운 파일 생성")
    sheet.append(["기사제목","기사요약"])


for page in range(1, 4):
    raw = requests.get('https://search.daum.net/search?w=news&nil_search=btn&DA=NTB&enc=utf8&cluster=y&cluster_page=1&q=코알라&p='+str(page))

    html = BeautifulSoup(raw.text,'html.parser')

    news_container = html.select('div.cont_inner')

    for news in news_container:
        title = news.select_one('a.f_link_b').text.strip()
        news_abstract = news.select_one('p.f_eb.desc').text.strip()
        print(title, news_abstract)
        print('-'*50)

        title = title.replace(",","")
        news_abstract = news_abstract.replace(",","")

        f.write(title+","+news_abstract+"\n")

        sheet.append([title,news_abstract])


f.close()
wb.save("daumnews.xlsx")