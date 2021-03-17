from django.shortcuts import render
from .models import Track
from django.core.paginator import Paginator

import sqlite3
import requests
from bs4 import BeautifulSoup
import pandas as pd

def track(request):
    Tracks = Track.objects.all()
    paginator = Paginator(Tracks, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'product/track.html', context={'Tracks': page_obj})
"""
liste = []
a = 1
while a <= 1:
    uheaders = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 Edg/86.0.622.69'}
    r = requests.get(
        "https://www.hepsiburada.com/demmex?kategori=2147483637&sayfa="+str(a)+"", headers=uheaders)
    soup = BeautifulSoup(r.content, "lxml")
    ürünler = soup.find_all("li", attrs={"class": "not-fashion-flex"})
    for ürün in ürünler:
        link_sonu = ürün.a.get("href")
        link_bası = "http://www.hepsiburada.com"
        link = link_bası+link_sonu
        uheaders = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 Edg/86.0.622.69'}
        r1 = requests.get(link, headers=uheaders)
        soup1 = BeautifulSoup(r1.content, "lxml")

        try:
            discount_price = soup1.find(
                "span", attrs={"itemprop": "price"}).text.strip()
            clean_price1 = discount_price.replace("TL", "")
        except:
            clean_price1 = "Fiyat Yok"
        try:
            price = soup1.find(
                "del", attrs={"id": "originalPrice"}).text.strip()
            clean_price2 = price.replace("TL", "")
        except:
            clean_price2= "Orjinal Fiyat Yok"
        try:
            rating = soup1.find("span", attrs={"class": "rating-evaluate"}).text.strip()
        except:
            rating= "Değerlendirme Yok"
        try:
            title = soup1.find("h1", attrs={"itemprop": "name"}).text.strip()
        except:
            title = "Ürün Adı Yok"
        try:
            decription=soup1.find("div",attrs={"id":"productDescriptionContent"}).text.strip()
        except:
            decription="Ürün Açıklama Yok" 

        try:
            date_added=soup1.find("div",attrs={"id":"productDescriptionContent"}).text.strip()
        except:
            date_added="Tarih Yok" 
    

        liste.append([link,clean_price1, clean_price2, title,rating])

        conn = sqlite3.connect('db.sqlite3', check_same_thread=False)
        c = conn.cursor()
        c.execute("INSERT INTO tracks_track(link,price,discount_price,title,rating,decription,date_added)VALUES (?,?,?,?,?,?,?)",(link,clean_price1, clean_price2, title,rating,decription,date_added))
        conn.commit()
        conn.close()
        a = a+1
  
        #df = pd.DataFrame(liste)
        #df.columns = ["ürün_adı", "marka", "link", "foto", "yeni_fiyat","orjinal_fiyat", "puan", "değerlendirme_sayısı","ürün_açıklama"]
        # df.to_excel("demmex.xlsx")
 
"""  