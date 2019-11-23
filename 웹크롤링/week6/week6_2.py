#셀레니움 연습하기
from selenium import webdriver
import time

#1. 웹드라이버 켜기
driver = webdriver.Chrome("./chromedriver")
#2. 네이버 지도 접속하기
driver.get("https://v4.map.naver.com/")

driver.find_elements_by_css_selector("button.btn_close")[1].click()

#3. 검색창에 검색어 입력하기 // input#search-input
search_box = driver.find_element_by_css_selector("input#search-input")
search_box.send_keys("치킨")

#4. 검색버튼 누르기 button.spm
search_button = driver.find_element_by_css_selector("button.spm")
search_button.click()

#5. 검색결과 확인하기

# 지연시간
time.sleep(1)

# 컨테이너 dl.lsnx_det
# 가게이름 dt > a
# 가게주소 dd.addr
# 전화번호 dd.tel

stores = driver.find_elements_by_css_selector("dl.lsnx_det")

for s in stores:
    name = s.find_element_by_css_selector("dt > a").text
    address = s.find_element_by_css_selector("dd.addr").text
    tel = s.find_element_by_css_selector("dd.tel").text
    print(name)
    print(address)
    print(tel)
    print("="*50)

driver.close()