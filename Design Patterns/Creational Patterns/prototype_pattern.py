from abc import ABC, abstractmethod
import copy


class Prototype(ABC):
    @abstractmethod
    def clone(self) -> 'Prototype':  # We use string annotation for forward reference since the Prototype class is not fully defined at this point
        pass


# Create a concrete prototype
class ConcretePrototype1(Prototype):
    def __init__(self, value: str) -> None:
        self.value = value

    def clone(self) -> Prototype:
        return copy.deepcopy(self)

    # overload the str method
    def __str__(self) -> str:
        return f"ConcretePrototype1 with value: {self.value}"


# Using the prototype
if __name__ == "__main__":
    original = ConcretePrototype1("Prototype Pattern")
    print(f"Original: {original}")

    clone = original.clone()
    print(f"Clone: {clone}")

    # Modifying the clone to demonstrate they are separate objects
    clone.value = "Modified Prototype Pattern"
    print(f"Modified Clone: {clone}")
    print(f"Original after modification: {original}")