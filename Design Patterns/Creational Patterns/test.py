from abc import ABC, abstractmethod

# we create an abstract base class
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    # this class will define the interface in the parent abstract class
    def sound(self):
        print('Woof!!')

class Cat(Animal):
    def sound(self):
        print('Meow!!')

# Factory class
class AnimalFactory:
    @staticmethod
    def get_animal(animal_type):
        if str.lower(animal_type) == "dog":
            return Dog()
        elif str.lower(animal_type) == "cat":
            return Cat()
        else:
            ValueError('Unknown animal type!')

if __name__ == "__main__":
    # create a dog using the factory
    animal = AnimalFactory.get_animal("Dog")
    animal.sound()

    animal = AnimalFactory.get_animal("cat")
    animal.sound()