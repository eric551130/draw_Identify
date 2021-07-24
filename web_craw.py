from bs4 import BeautifulSoup
import requests
import os,time
from selenium import webdriver
import base64

if not os.path.exists('train'):
    os.mkdir('train')
    print("creat:", 'train')

input_image = input("輸入:")
#input_image = 'cat'

if not os.path.exists(f'train/{input_image}'):
    os.mkdir(f'train/{input_image}')
    print("creat:", f'train/{input_image}')

driver=webdriver.Chrome('chromedriver.exe')

driver.get(f"https://www.google.com.tw/search?q={input_image}&source=lnms&tbm=isch")
#response = requests.get(f"https://www.google.com.tw/search?q={input_image}&source=lnms&tbm=isch")

for i in range(5):
    driver.execute_script(f"window.scrollTo({i*2000}, {i*2000+2000});")
    time.sleep(0.5)

soup = BeautifulSoup(driver.page_source,'lxml')

items = driver.find_elements_by_class_name("rg_i.Q4LuWd")

for item in items:
    if i == 110:
        break
    img_url = item.get_attribute('src')
    #print(img_url)
    if img_url != None:
        if 'data' in img_url:
            continue
        i += 1
        img = requests.get(img_url)
        img_name = f'train/{input_image}/' + str(i) + '.png'
        with open(img_name, 'wb') as file:  # 以byte形式將圖片資料寫入
            file.write(img.content)
            file.flush()
        file.close()
        print(f'第 {i} 張')

print(i)

driver.close()