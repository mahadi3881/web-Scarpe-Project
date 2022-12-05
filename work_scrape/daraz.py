from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('https://www.daraz.com.bd/men-muslim-wear/?spm=a2a0e.home.cate_4.4.2e8f12f78OjGuX')

# title  = driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/div[3]/div/div/div[1]/div[2]/div[1]/div/div/div[2]/div[2]/a').text

#title = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div/div[3]/div/div/div[1]/div[2]/div[1]/div/div/div[2]/div[2]/a')))

total_product = 10*4
title_list = []
for i in range(1,total_product+1):
    x_path = '//*[@id="root"]/div/div[3]/div/div/div[1]/div[2]/div['+str(i)+']/div/div/div[2]/div[2]/a'
    title = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, x_path )))

    title_list.append(title.text)

print(title_list)
time.sleep(500)
driver.quit()