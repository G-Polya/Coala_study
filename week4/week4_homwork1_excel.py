import requests
from bs4 import BeautifulSoup
import openpyxl

try:
    wb = openpyxl.load_workbook("naverbooks.xlsx")
    sheet = wb.active
    print("불러오기 완료")

except :
    wb = openpyxl.Workbook()
    sheet = wb.active
    print("새로운 파일 생성")
    sheet.append(["제목", "저자"])


for page in range(1,101,20):
    raw = requests.get('https://series.naver.com/ebook/top100List.nhn?page='+str(page),
                       headers = {'User-Agent':'Mozilla/5.0'})

    html = BeautifulSoup(raw.text,'html.parser')


    books = html.select('ul.lst_thum.v1 li')

    for book in books:
        title = book.select_one('ul.lst_thum.v1 li a strong').text.strip()
        author = book.select_one('ul.lst_thum.v1 li a span.writer').text.strip()

        sheet.append([title,author])

        print(title, author)