from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
options = Options()
options.add_argument("--headless")
driver = webdriver.Firefox(firefox_options=options)
print("before loop")
while True:
    driver.get("http://freedoge.online/")
    inputElement = driver.find_element_by_css_selector('#walletAddress')
    inputElement.send_keys('DQxKMfc8NHHeZJy4CsA2mAQJmtDnL4aSQ5')# chage this to your doge address
    driver.find_element_by_css_selector('.btn.btn-success').click()
    time.sleep(2)
    driver.find_element_by_css_selector('.btn.btn-primary').click()
    time.sleep(5)
    driver.close()
    print("running")
    time.sleep(1800)
