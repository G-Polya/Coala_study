from selenium import webdriver
import time

#1. 웹브라우저 켜기
driver = webdriver.Chrome("./chromedriver")

#2. 파파고 접속하기
driver.get("https://papago.naver.com/")

# 지연시간. 안주면 selenium.common.exceptions.NoSuchElementException: Message:오류남
time.sleep(1)


#3. 번역입력창에 문장 입력하기
trans_input = driver.find_element_by_css_selector("textarea#txtSource")
trans_input.send_keys("seize the day")

#4. 번역하기 버튼 누르기
trans_button = driver.find_element_by_css_selector("button#btnTranslate")
trans_button.click()

#5. 번역출력창의 문장 가져오기
time.sleep(1) # 지연시간
trans_output =  driver.find_element_by_css_selector("div#txtTarget span").text
print(trans_output)



driver.close()