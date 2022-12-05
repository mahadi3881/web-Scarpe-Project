

#amazon Site Details.......

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
print(driver.get("https://www.amazon.com/ZAGG-InvisibleShield-Glass-Elite-Plus/dp/B099KJFNCP/"))

title = driver.find_element(by=By.XPATH, value='//*[@id="productTitle"]').text
img = driver.find_element(by=By.XPATH, value='//*[@id="landingImage"]').get_attribute('src')
list_info=[title,img]
print("List Of Data",list_info)