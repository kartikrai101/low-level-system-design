# Factory Pattern -> https://refactoring.guru/design-patterns/factory-method

from abc import ABC, abstractmethod

# Abstract base class
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

# Concrete classes
class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Factory class
class AnimalFactory:
    @staticmethod
    def get_animal(animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError(f"Unknown animal type: {animal_type}")

# Example usage
if __name__ == "__main__":
    # Create a dog using the factory
    animal = AnimalFactory.get_animal("dog")
    print(animal.speak())  # Output: Woof!

    # Create a cat using the factory
    animal = AnimalFactory.get_animal("cat")
    print(animal.speak())  # Output: Meow!
