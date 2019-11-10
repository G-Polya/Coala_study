from selenium import webdriver
import time

driver = webdriver.Chrome("./chromedriver")
driver.get("https://www.instagram.com/explore/tags/ootd/")



posts = driver.find_elements_by_css_selector("div.v1Nh3")

for i in range(0,12):
    posts[i].click()

    time.sleep(1)

    post_body = driver.find_element_by_css_selector("div.C4VMK span").text
    print(post_body)
    print("="*50)

    close_button = driver.find_element_by_css_selector("button.ckWGn")
    close_button.click()