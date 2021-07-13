from bs4 import BeautifulSoup
import requests
import os

if not os.path.exists('train'):
    os.mkdir('train')  # 建立資料夾
    print("creat:", 'train')

input_image = input("輸入:")

response = requests.get(f"https://unsplash.com/s/photos/{input_image}")

soup = BeautifulSoup(response.text,"lxml")

results = soup.find_all("img",{"class":"_2UpQX"},limit=5)

image_links = [result.get("src") for result in results] #圖片來源

for index, link in enumerate(image_links):
    if not os.path.exists(f'train/{input_image}'):
        os.mkdir(f'train/{input_image}') #建立資料夾
        print("creat:", f'train/{input_image}')

    img = requests.get(link) #下載

    with open(f'train/{input_image}' + "\\" + str(index+1) + ".jpg", "ab") as file:
        file.write(img.content)