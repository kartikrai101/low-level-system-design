# Decorator Pattern -> https://refactoring.guru/design-patterns/decorator
from abc import ABC, abstractmethod

# Create the product interface
class Coffee(ABC):
    @abstractmethod
    def cost(self) -> float:
        pass
    @abstractmethod
    def description(self) -> str:
        pass


# Create concrete products
class SimpleCoffee(Coffee):
    def cost(self) -> float:
        return 5.0
    def description(self) -> str:
        return "Simple Coffee!"


# Create the decorators
class CoffeeDecorator(Coffee):
    def __init__(self, coffee: Coffee):
        self._decorated_coffee = coffee

    def cost(self) -> float:
        return self._decorated_coffee.cost()

    def description(self) -> str:
        return self._decorated_coffee.description()


class MilkDecorator(CoffeeDecorator):
    def cost(self) -> float:
        return self._decorated_coffee.cost() + 1.5

    def description(self) -> str:
        return f"{self._decorated_coffee.description()}, milk"


class SugarDecorator(CoffeeDecorator):
    def cost(self) -> float:
        return self._decorated_coffee.cost() + 0.5

    def description(self) -> str:
        return f"{self._decorated_coffee.description()}, sugar"


# Using the decorators
if __name__ == "__main__":
    simple_coffee = SimpleCoffee()
    print(f"Cost: {simple_coffee.cost()}, Description: {simple_coffee.description()}")

    milk_coffee = MilkDecorator(simple_coffee)
    print(f"Cost: {milk_coffee.cost()}, Description: {milk_coffee.description()}")

    sugar_milk_coffee = SugarDecorator(milk_coffee)
    print(f"Cost: {sugar_milk_coffee.cost()}, Description: {sugar_milk_coffee.description()}")
