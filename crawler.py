from bs4 import BeautifulSoup
import requests
import os
import uuid
from PIL import Image
from urllib.request import urlopen
import concurrent.futures
import time

# 設置最大數量
images_num = 10000

# log目前第幾張
pic_divider = 1000

def getCaptcha(num):
    id = uuid.uuid4()
    url = f"https://digiapp.vietcombank.com.vn/utility-service/v1/captcha/{id}"
    img = Image.open(urlopen(url))
    img.save(f"{id}.jpeg","jpeg")
    if (num % pic_divider == 0):
        print(f"No. {num} Pic")

numCaptcha = list(range(0,images_num))
start_time = time.time()  # 開始時間

# 同時建立及啟用10個執行緒
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    executor.map(getCaptcha, numCaptcha)
 
end_time = time.time()
print(f"{end_time - start_time} 秒爬取圖片")