from abc import ABC, abstractmethod
from typing import Any

# Define the Pizza class
class Pizza:
    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Pizza parts: {', '.join(self.parts)}")


# Create the Builder interface -> defines the building steps
class PizzaBuilder(ABC):
    @property
    @abstractmethod
    def pizza(self) -> None:
        pass

    @abstractmethod
    def build_crust(self) -> None:
        pass

    @abstractmethod
    def build_sauce(self) -> None:
        pass

    @abstractmethod
    def build_cheese(self) -> None:
        pass

    @abstractmethod
    def build_toppings(self) -> None:
        pass


# Implement a Concrete Builder -> is a concrete implementation that builds a specific type of pizza
class MargheritaPizzaBuilder(PizzaBuilder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._pizza = Pizza()

    @property
    def pizza(self) -> Pizza:
        pizza = self._pizza
        self.reset()
        return pizza

    def build_crust(self) -> None:
        self._pizza.add("Thin Crust")

    def build_sauce(self) -> None:
        self._pizza.add("Tomato Sauce")

    def build_cheese(self) -> None:
        self._pizza.add("Mozzarella Cheese")

    def build_toppings(self) -> None:
        self._pizza.add("Basil")


# Create a Director class -> controls the construction process.
class PizzaDirector:
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> PizzaBuilder:
        return self._builder

    @builder.setter
    def builder(self, builder: PizzaBuilder) -> None:
        self._builder = builder

    def build_basic_pizza(self) -> None:
        self.builder.build_crust()
        self.builder.build_sauce()
        self.builder.build_cheese()

    def build_full_pizza(self) -> None:
        self.builder.build_crust()
        self.builder.build_sauce()
        self.builder.build_cheese()
        self.builder.build_toppings()


# Client code to create pizzas
if __name__ == "__main__":
    director = PizzaDirector()
    builder = MargheritaPizzaBuilder()
    director.builder = builder

    print("Basic Margherita Pizza: ")
    director.build_basic_pizza()
    builder.pizza.list_parts()

    print("\n")

    print("Full Margherita Pizza: ")
    director.build_full_pizza()
    builder.pizza.list_parts()

    print("\n")

    print("Custom Margherita Pizza: ")
    builder.build_crust()
    builder.build_sauce()
    builder.pizza.list_parts()
