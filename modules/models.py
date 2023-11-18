from dataclasses import dataclass


@dataclass
class Product:
    id: str
    name: str
    price: float
    link: str
    image: str
