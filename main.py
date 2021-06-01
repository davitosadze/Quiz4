import random
import requests
from bs4 import BeautifulSoup
import sqlite3
import time

conn = sqlite3.connect('mobiles.sqlite')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS mobiles (
mobileName VARCHAR(255),price VARCHAR(255) ,image VARCHAR(255))''')
for num in range(1, 6):
    url = f"https://alta.ge/smartphones-page-{num}.html"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    content = soup.find_all('div', class_="ty-column3")
    # print(content)
    for i in content:
        mobileName = i.find('a', class_="product-title").text
        price = i.find('span', class_="ty-price-num").text

        image = i.find('img', class_='ty-pict')
        imageLink = image["src"]

        cur.execute('INSERT INTO mobiles (mobileName,price,image) VALUES(?,?,?)', (mobileName, price, imageLink))
        conn.commit()
    time.sleep(random.randint(15, 20))
    print("DONE")
    cur.close()
