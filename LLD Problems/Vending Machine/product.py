# this will be an interface for all the products that we will create
from abc import ABC


class Product(ABC):
    def __init__(self, name: str, price: float):
        self.price = price
        self.name = name