# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# import time
# from selenium.webdriver.support.ui import WebDriverWait 
# from selenium.webdriver.support import expected_conditions as EC


# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) 
# driver.get("https://www.thuisbezorgd.nl/bestellen/eten/binnenstad-3512")


# # title =driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[2]/section/div[1]/div/section[1]/div[2]/ul/li[1]/div/a/div/div/div/div/div[1]/div[2]/div/div[1]/div/h3').text
# # time.sleep(50)
# x_path = '//*[@id="search-results-panel-menu_items"]/div[2]/div/ul/li[2]/div/a/div/div/div[2]/div/div/div[1]/div[1]/h3'
# title = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, x_path )))
# print(title)

# from django.shortcuts import render
# from django.shortcuts import HttpResponse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# def index(request):
    
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.daraz.com.bd/catalog/?spm=a2a0e.home.search.1.735212f7L7tnME&q=mens%20watch&_keyori=ss&clickTrackInfo=textId--2272977964443954682__abId--300705__pvid--c9c69c83-c11c-4721-99a8-5de41878734d__matchType--1__srcQuery--mens%20watch__spellQuery--mens%20watch&from=suggest_normal&sugg=mens%20watch_0_1')
    
    
product_piece=10*4
title_list = []

for i in range(1, product_piece):
    X_path = '//*[@id="root"]/div/div[2]/div/div/div[1]/div[2]/div['+str(i)+']/div/div/div[2]/div[2]'
    price_path = '//*[@id="root"]/div/div[2]/div/div/div[1]/div[2]/div['+str(i)+']/div/div/div[2]/div[3]/span'
    img_path = '//*[@id="root"]/div/div[2]/div/div/div[1]/div[2]/div['+str(i)+']/div/div/div[1]/div[1]/a/img'
    title = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, X_path)))
    Price = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, price_path)))
    img = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, img_path)))
    

    title_list.append(title.text)
    title_list.append(Price.text)
    title_list.append(img.get_attribute('src'))

    print(title_list)  
    
    # return render(request,'index.html')