class Inventory:
    def __init__(self):
        self.products = {}  # {product: quantity}

    def add_product(self, product: str, quantity: int):
        self.products[product] = quantity

    def remove_product(self, product: str):
        del self.products[product]

    def update_quantity(self, product: str, quantity: int):
        self.products[product] = quantity

    def get_quantity(self, product: str) -> int:
        return self.products.get(product, 0)

    def is_available(self, product: str) -> bool:
        return product in self.products and self.products[product] > 0