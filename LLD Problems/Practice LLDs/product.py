from abc import ABC


class Product(ABC):
    def __init__(self, name: str, cost: float):
        self.name = name
        self.cost = cost