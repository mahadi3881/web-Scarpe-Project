from turtle import title
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
print(driver.get("https://www.ubereats.com/store/mcdonalds-university-%26-mesa-drive/Y5oUs3IjROy4sxwlRFq8Bw/db74523c-bae4-58eb-81cc-f29412c16f37/82abdbfd-57c1-50b4-8a90-d61e1c628c06/dbf2fb5b-b6b2-5e36-946d-ef32bd87085a?fbclid=IwAR01RiCzd0HX2ZEa4s4DFOVWDHP6u7-apxyItbiwPci0vrUIS42-xOy4tu4"))

title  = driver.find_element(by=By.XPATH, value='//*[@id="main-content"]/div/div[1]/div/div[2]/div[1]/h1').text
price = driver.find_element(by=By.XPATH, value='//*[@id="main-content"]/div/div[1]/div/div[2]/div[1]/span').text
cal  = driver.find_element(by=By.XPATH, value='//*[@id="main-content"]/div/div[1]/div/div[2]/div[1]/div').text
img  = driver.find_element(by=By.XPATH, value='//*[@id="main-content"]/div/div[1]/div/div[1]/div/div/div/div/div/div/img').get_attribute('src')

print("title:",title)
print("Cal:",cal)
print("Price:",price)
print("Picture:",img)













# #new uber
# from cgi import print_exception
# import imghdr
# from turtle import title
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver.get("https://www.ubereats.com/store/mcdonalds-university-%26-mesa-drive/Y5oUs3IjROy4sxwlRFq8Bw?fbclid=IwAR1-OFxtODBF_kKamN2goWcuZiJjKEKaXwpCqJm5nFYj5onpz-HCDZmi7xU")

# title  = driver.find_element(by=By.XPATH, value='//*[@id="main-content"]/div[4]/div[2]/div[4]/ul/li[1]/ul/li[1]/div/div/div[2]/div[1]/div/span').text

# cal  = driver.find_element(by=By.XPATH, value='//*[@id="main-content"]/div[4]/div[2]/div[4]/ul/li[1]/ul/li[1]/div/div/div[2]/div[2]/span[3]').text

# price = driver.find_element(by=By.XPATH, value='//*[@id="main-content"]/div[4]/div[2]/div[4]/ul/li[1]/ul/li[1]/div/div/div[2]/div[2]/span[1]').text

# img =  driver.find_element(by=By.XPATH, value='//*[@id="main-content"]/div[4]/div[2]/div[4]/ul/li[1]/ul/li[1]/div/div/div[1]/div[1]/div[1]/picture/img').get_attribute('src')


# #list_of_all=[title,price,cal,img]
# print("title:",title)
# print("Cal:",cal)
# print("Price:",price)
# print("Picture:",img)

# driver.quit()