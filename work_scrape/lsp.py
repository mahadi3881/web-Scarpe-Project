
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
import time

driver.get("https://www.facebook.com/")

email = driver.find_element(by=By.XPATH, value='//*[@id="email"]')
password = driver.find_element(by=By.XPATH, value='//*[@id="pass"]')

submit = driver.find_element(by=By.CSS_SELECTOR, value='[name="login"]')

email.send_keys('01725473881')
password.send_keys('mehedi_12345@#@#')


submit.submit()

time.sleep(50000)

driver.quit()
