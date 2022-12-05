
#============================Un Soolved ERROR/ not for selenium use beautifullshop can solved ====================#
# from requests import options
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# # options = Options()
# # options.headless = True
# # options.add_argument("--window-size=1920,1200")
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# print(driver.get("https://www.alibaba.com/product-detail/Ziitop-Hot-Sale-Anime-Shoes-One_1600527014202.html?fbclid=IwAR0ATpsT-Fq1to3GseoZ-lZCQ0mPPTaUpPJapRtWifAe31SeQkX-XJHRbp0"))

# title = driver.find_element(by=By.XPATH, value='//*[@id="container"]/div[1]/div/div[2]/div[1]/div[1]/div[3]/div[1]/h1').text
# video = driver.find_element(by=By.XPATH, value='//*[@id="main-video"]/div/div/div/video').get_attribute('src')
# ratting =  driver.find_element(by=By.XPATH, value='//*[@id="product-review"]/div/div/div/div/div/div[2]/label[4]/i').get_attribute('src')
# buyer =  driver.find_element(by=By.XPATH, value='//*[@id="product-review"]/div/span').text
# orginal_price =  driver.find_element(by=By.XPATH, value='//*[@id="container"]/div[1]/div/div[2]/div[1]/div[1]/div[3]/div[3]/div[1]/div[2]/span').text
# discount_price =  driver.find_element(by=By.XPATH, value='//*[@id="container"]/div[1]/div/div[2]/div[1]/div[1]/div[3]/div[3]/div[2]/div[2]/span').text
# print("Title:",title)
# print("Video:",video)
# print("Ratting:",ratting)
# print("Buyer:",buyer)
# print("Orginal Price:",orginal_price)
# print("Discount Price:",discount_price)
# driver.quit()



#===================== 1.Amazon web scrapping=====================#

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# print(driver.get("https://www.amazon.com/SteelSeries-Aerox-Lightweight-Ultra-lightweight-Resistant-Connectivity/dp/B09VNTCZZN/ref=sr_1_1_sspa?keywords=gaming+mouse&pd_rd_r=2fac5dcc-aa3f-4a3f-84a1-ae318db16f74&pd_rd_w=sITU9&pd_rd_wg=J4RB3&pf_rd_p=12129333-2117-4490-9c17-6d31baf0582a&pf_rd_r=V0ZFSV1ENSAZ0GJD6S82&qid=1667390944&qu=eyJxc2MiOiI2Ljk0IiwicXNhIjoiNi4zMiIsInFzcCI6IjUuOTEifQ%3D%3D&sr=8-1-spons&psc=1"))


# title  = driver.find_element(by=By.XPATH, value='//*[@id="productTitle"]').text
# price = driver.find_element(by=By.XPATH, value='//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span/span[2]/span[2]').text
# img  = driver.find_element(by=By.XPATH, value='//*[@id="landingImage"]').get_attribute('src')

# ratting = driver.find_element(by=By.XPATH, value='//*[@id="acrPopover"]/span[1]/a/i[1]').get_attribute('src')



# print("title:",title)
# print("Ratting:",ratting)
# print("Price:",price)
# print("Picture:",img)
# driver.quit()




#===================== 2.Alibaba  web scrapping=====================#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# print(driver.get("https://www.alibaba.com/product-detail/Custom-logo-Anime-high-top-men_1600450042303.html?spm=a27aq.21285148.2734936890.1.27574560Z2No0E"))

# title  = driver.find_element(by=By.XPATH, value='//*[@id="container"]/div[1]/div/div[2]/div/div[1]/div[3]/div[1]/h1').text

# video  = driver.find_element(by=By.XPATH, value='//*[@id="main-video"]/div/div/div/video').get_attribute('src')

# price  = driver.find_element(by=By.XPATH, value='//*[@id="container"]/div[1]/div/div[2]/div/div[1]/div[3]/div[3]/div[1]/div[2]/span').text

# print("title:",title)
# print("Price:",price)
# print("Video Link:",video)
# driver.quit()

#===================== 3.Daraz  web scrapping=====================#

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# print(driver.get("https://www.daraz.com.bd/products/tvs-apache-rtr-160cc-4v-motor-cycle-sd-carb-black-i107406337-s1022558423.html?spm=a2a0e.searchlistcategory.list.2.531a552chJpBeh&search=1"))

# title  = driver.find_element(by=By.XPATH, value='//*[@id="module_product_title_1"]/div/div/span').text

# price = driver.find_element(by=By.XPATH, value='//*[@id="module_product_price_1"]/div/div/span').text
# img  = driver.find_element(by=By.XPATH, value='//*[@id="module_item_gallery_1"]/div/div[1]/div/img').get_attribute('src')
# ratting = driver.find_element(by=By.XPATH, value='//*[@id="module_product_review_star_1"]/div').get_attribute('src')

# print("title:",title)
# print("Price:",price)
# print("Picture Link:",img)
# print("Ratting:",ratting)
# driver.quit()


#===================== 4.Filpkart  web scrapping=====================#

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# print(driver.get("https://www.flipkart.com/hp-ink-tank-wireless-415-all-one-multi-function-wifi-color-printer-voice-activated-printing-google-assistant-alexa-color-page-cost-20-paise-black-10-paise/p/itm3d317b6a651a2?pid=PRNF6M6F8V9BPNQ5&lid=LSTPRNF6M6F8V9BPNQ59PCYJM&marketplace=FLIPKART&store=6bo%2Ftia%2Fffn%2Ft64&srno=b_1_4&otracker=hp_omu_Best%2Bof%2BElectronics_1_3.dealCard.OMU_D54DFY00C5JD_3&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_2_L2_view-all%2Chp_omu_PINNED_neo%2Fmerchandising_Best%2Bof%2BElectronics_NA_dealCard_cc_1_NA_view-all_3&fm=neo%2Fmerchandising&iid=c510d01f-2cbf-4ef8-a69f-f43d76598ab1.PRNF6M6F8V9BPNQ5.SEARCH&ppt=browse&ppn=browse&ssid=elq6bxi1i80000001667390991960"))



# title  = driver.find_element(by=By.XPATH, value='//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/h1/span').text

# price_discount = driver.find_element(by=By.XPATH, value='//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div[3]/div[1]/div/div[1]').text
# price = driver.find_element(by=By.XPATH, value='//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div[3]/div[1]/div/div[2]').text
# img  = driver.find_element(by=By.XPATH, value='//*[@id="container"]/div/div[3]/div[1]/div[1]/div[1]/div/div[1]/div[2]/div[1]/div[2]/img').get_attribute('src')
# ratting = driver.find_element(by=By.XPATH, value='//*[@id="productRating_LSTPRNF6M6F8V9BPNQ59PCYJM_PRNF6M6F8V9BPNQ5_"]/div').get_attribute('src')

# rating = driver.find_element(by=By.XPATH, value='//*[@id="productRating_LSTPRNF6M6F8V9BPNQ59PCYJM_PRNF6M6F8V9BPNQ5_"]/div').text

# print("title:",title)
# print("Orginal Price:",price)
# print("Picture Link:",img)
# print("Discount Price:",price_discount)
# print("Ratting Picture:",ratting)
# print("Ratting :",rating)
# driver.quit()


#===================== 5.Food Panda web scrapping=====================#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# print(driver.get("https://www.foodpanda.com.bd/restaurant/cg68/rahman-cakes"))


# title  = driver.find_element(by=By.XPATH, value='').text

# # price = driver.find_element(by=By.XPATH, value='//*[@id="module_product_price_1"]/div/div/span').text
# # img  = driver.find_element(by=By.XPATH, value='//*[@id="module_item_gallery_1"]/div/div[1]/div/img').get_attribute('src')
# # ratting = driver.find_element(by=By.XPATH, value='//*[@id="module_product_review_star_1"]/div').get_attribute('src')




# print("title:",title)
# # print("Price:",price)
# # print("Picture Link:",img)
# # print("Ratting:",ratting)
# # driver.quit()

