import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

def scrape_books():
    # Website to scrape
    url = 'http://books.toscrape.com/catalogue/category/books_1/index.html'
    response = requests.get(url)

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    books = []

    for book in soup.find_all('article', class_='product_pod'):
        title = book.h3.a['title']
        price_text = book.find('p', class_='price_color').text
        # Clean price to remove currency symbols and weird chars
        price_number = re.sub(r'[^\d.]', '', price_text)
        price = float(price_number)
        rating_class = book.p['class'][1]
        # Map rating word to number
        rating_map = {'One':1, 'Two':2, 'Three':3, 'Four':4, 'Five':5}
        rating = rating_map.get(rating_class, 0)

        books.append({'Title': title, 'Price': price, 'Rating': rating})

    return pd.DataFrame(books)
