import requests
import lxml
import itertools
from bs4 import BeautifulSoup
import re


def get_link_data(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, "lxml")
    try:
        name = soup.find("h1", attrs={"itemprop": "name"}).text.strip()
    except:
        name = "Ürün Yok"
    try:
        price = soup.find("span", attrs={"itemprop": "price"}).text.strip()
        #clean_price1 = discount_price.replace("TL", "")
        current=price.split('\n')
        cur=current[:3]
        for i in cur:
            my_float = float(i.replace(",", "."))
    except:
        price = "Fiyat Yok"
   
    return name,my_float