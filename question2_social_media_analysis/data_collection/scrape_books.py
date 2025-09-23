import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import re

def scrape_books(pages=3, delay=2):
    books = []
    for page in range(1, pages+1):
        url = f"http://books.toscrape.com/catalogue/page-{page}.html"
        resp = requests.get(url)
        if resp.status_code != 200:
            break
        soup = BeautifulSoup(resp.content, "html.parser")
        for book in soup.find_all('article', class_='product_pod'):
            title = book.h3.a['title']
            price = float(re.sub(r'[^\d.]', '', book.find('p', class_='price_color').text))
            rating_map = {'One':1, 'Two':2, 'Three':3, 'Four':4, 'Five':5}
            rating = rating_map.get(book.p['class'][1], 0)
            books.append({"title": title, "price": price, "rating": rating})
        print(f"Scraped page {page}")
        time.sleep(delay)
    df = pd.DataFrame(books)
    df.to_csv("books_data.csv", index=False)
    return df
