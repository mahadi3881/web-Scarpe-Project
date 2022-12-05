from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) 
title_list = []
# total_page =  len(driver.find_elements(by=By.CLASS_NAME, value='ant-pagination-item ant-pagination-item-1'))
#print(total_page)
for page in range(1,39):
    driver.get('https://www.daraz.com.bd/men-muslim-wear/?page='+str(page)+'')
    count = len(driver.find_elements(by=By.CLASS_NAME, value='gridItem--Yd0sa'))
    print(count)
    for j in range(1,count+1):
        x_path = '//*[@id="root"]/div/div[3]/div/div/div[1]/div[2]/div['+str(j)+']/div/div/div[2]/div[2]/a'
         #print(x_path)
        #title  = driver.find_element(by=By.XPATH, value= x_path).text
        title = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, x_path )))

        title_list.append(title.text)
print(len(title_list))
print(title_list)


time.sleep(500)

driver.quit()