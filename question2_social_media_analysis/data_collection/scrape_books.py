import requests
from bs4 import BeautifulSoup
import csv

BASE_URL = "http://books.toscrape.com/"

def scrape_books(pages=5, output_file="books_raw.csv"):
    """Scrape book data from books.toscrape.com and save to CSV."""
    books = []
    for page_num in range(1, pages + 1):
        url = BASE_URL if page_num == 1 else f"{BASE_URL}catalogue/page-{page_num}.html"
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")

            for article in soup.select("article.product_pod"):
                title = article.h3.a["title"]
                price = article.select_one(".price_color").text.strip()
                rating = article.p["class"][1]

                books.append([title, price, rating])

        except Exception as e:
            print(f"Error on page {page_num}: {e}")

    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["title", "price", "rating"])
        writer.writerows(books)

    print(f"Scraping complete! Data saved to {output_file}")
