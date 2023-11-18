import csv 
from modules.models import Product


def create_csv_file(category:str):
    with open(f'output/{category}.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(
            ['id', 'name', 'price', 'link', 'image']
        )


def write_csv_file(category:str, products: list[Product]):
    with open(f'output/{category}.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for product in products:
            writer.writerow(
                [product.id, product.name, product.price, product.link, product.image]
            )
