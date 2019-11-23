from selenium import webdriver
import time

driver = webdriver.Chrome("./chromedriver")

driver.get("https://nid.naver.com")

id_box = driver.find_element_by_css_selector("input#id")
id_box.send_keys("tollea1234")
pw_box = driver.find_element_by_css_selector("input#pw")
pw_box.send_keys("1234")
login_button = driver.find_element_by_css_selector("input.btn_global")
login_button.click()


time.sleep(10)


driver.get("https://www.facebook.com/")
id_box = driver.find_element_by_css_selector("input#email")
id_box.send_keys("01029330743")
pw_box = driver.find_element_by_css_selector("input#pass")
pw_box.send_keys("tollea1324!")
login_button = driver.find_element_by_css_selector("input#u_0_e")
login_button.click()