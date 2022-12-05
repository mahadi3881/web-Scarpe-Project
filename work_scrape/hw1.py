

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://perfumancebd.com/product-category/perfume/refreshing/')

product_piece=4*3
# title_list = []

for i in range(1, product_piece):
    X_path = '//*[@id="rig-adpr"]/div['+str(i)+']/p[1]'
    price_path = '//*[@id="rig-adpr"]/div['+str(i)+']/p[2]'
    img_path = '//*[@id="rig-adpr"]/div['+str(i)+']/a/img'
    title = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, X_path)))
    Price = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, price_path)))
    img = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, img_path)))
    

    print("Title:",title.text)
    print("Price",Price.text)
    print("Photo",img.get_attribute('src'))
for i in range(1, 12):
    driver.get("https://perfumancebd.com/product-category/perfume/refreshing/")
    image = driver.find_element(by=By.XPATH, value='//*[@id="rig-adpr"]/div['+str(i)+']/a/img')
    dwn = image.get_attribute('src')
    driver.get(dwn)
    img_loc = "F:\python"+str(i)+".png"
    driver.save_screenshot(img_loc)

    # print(title_list)

time.sleep(500)
driver.quit()