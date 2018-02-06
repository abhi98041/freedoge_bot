from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("http://freedoge.online/")


while True:
    inputElement = driver.find_element_by_css_selector('#walletAddress')
    inputElement.send_keys('DQxKMfc8NHHeZJy4CsA2mAQJmtDnL4aSQ5')# chage this to your doge address
    driver.find_element_by_css_selector('.btn.btn-success').click()
    time.sleep(2)
    driver.find_element_by_css_selector('.btn.btn-primary').click()
    time.sleep(5)
    driver.close()
    time.sleep(1800)
