#1. 가게이름
#2. 평점
#3. wnth
#4. 카페정보 100개(5페이지)
from selenium import webdriver
import time

driver = webdriver.Chrome("./chromedriver")

driver.get("https://www.google.com/maps/")


search_box = driver.find_element_by_css_selector("input#searchboxinput")
time.sleep(5)
search_box.send_keys("카페")
search_button = driver.find_element_by_css_selector("button#searchbox-searchbutton")

search_button.click()

n = 1
count = 1

# 컨테이너: div.section-result
# 이름: h3 >span
# 평점: span.cards-rating-score
# 주소: span.section-result-location

for n in range(999):

    time.sleep(5)

    caffes = driver.find_elements_by_css_selector("div.section-result")

    for c in caffes:
        name = c.find_element_by_css_selector("h3 > span").text
        rating = c.find_element_by_css_selector("span.cards-rating-score").text
        address = c.find_element_by_css_selector("span.section-result-location").text

        print(name)
        print(rating)
        print(address)
        count += 1
        print(count)
        print("="*50)

    # span.n7lv7yjyC35__button-next-icon
    try:
        page = driver.find_elements_by_css_selector("span.n7lv7yjyC35__button-next-icon")
        page[0].click()
    except:
        print("데이터 수집 완료")
        break;