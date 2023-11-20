from bs4 import BeautifulSoup as bs
import requests 
import csv
from modules.csv_writer import write_csv_file, create_csv_file
from modules.models import Product


def parse_html(url: str) -> csv:
    result = requests.get(url=url)
    soup = bs(result.text, 'lxml')
    category = soup.find("h1", class_="catalog-heading ng-star-inserted").text
    max_pages = get_max_pages(url=url)
    create_csv_file(category=category)

    page = 1
    count_pages = 0

    while page <= max_pages:
        list_products = []
        res = requests.get(f"{url}page={page}/")
        soup = bs(res.text, 'lxml')
        products = soup.find_all('li', class_='catalog-grid__cell catalog-grid__cell_type_slim ng-star-inserted')
        for product in products:
            id = product.find("div", class_="g-id display-none").text
            name = product.find("span", class_="goods-tile__title").text
            price = product.find("span", class_="goods-tile__price-value").text
            img = product.find("img", class_="ng-lazyloaded")
            image = img['src'] if img and 'src' in img.attrs else None
            link = product.find("a", class_="goods-tile__heading ng-star-inserted").get("href")
            list_products.append(
                Product(id=id, name=name, price=price, link=link, image=image)
            )
        write_csv_file(category=category, products=list_products)
        count_pages += 1
        page += 1
        if count_pages >= max_pages:
            break


def get_max_pages(url: str) -> int:
    r = requests.get(url)
    soup = bs.BeautifulSoup(r.text, "lxml")
    pages = soup.find_all("a", class_="pagination__link ng-star-inserted")
    pages_values = [page.text for page in pages]
    return int(pages_values[-1])
