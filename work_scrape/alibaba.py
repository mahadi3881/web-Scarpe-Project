from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) 

driver.get("https://www.alibaba.com/trade/search?spm=a2700.8293689.HomeLeftCategory.d134.1e8967afXEdRwF&CatId=134&SearchText=Agricultural+Machinery+Parts&language=en&indexArea=product_en")

count = len(driver.find_elements(by=By.CLASS_NAME, value='elements-title-normal'))

print(count)
title_list = []

for i in range(1,count+1):
    X_path='//*[@id="root"]/div/div[3]/div[2]/div/div/div/div['+str(i)+']/div/div[2]/div[1]/h2/a/p'
    title = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, X_path )))

    title_list.append(title.text)
print(title_list)


time.sleep(500)

driver.quit()    