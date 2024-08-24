from abc import ABC, abstractmethod
from coin import Coin
from note import Note
from product import Product


class VendingMachineState(ABC):
    def __init__(self, vending_machine):
        self.vending_machine = vending_machine

    @abstractmethod
    def select_product(self, product: Product):
        pass

    @abstractmethod
    def insert_coin(self, coin: Coin):
        pass

    @abstractmethod
    def insert_note(self, note: Note):
        pass

    @abstractmethod
    def dispense_product(self):
        pass

    @abstractmethod
    def return_change(self):
        pass