from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
print(driver.get("https://www.alibaba.com/product-detail/Ziitop-Hot-Sale-Anime-Shoes-One_1600527014202.html?fbclid=IwAR3jajuPDyzkAn2XR4X8pHA2kVYuSaH1o0UGNRKQ7P11ywcwsBoJgSpVaxw"))
title = driver.find_element(by=By.XPATH, value='//*[@id="container"]').text
print(title)
