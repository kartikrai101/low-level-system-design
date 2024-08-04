from abc import ABC, abstractmethod


# ABSTRACT PRODUCT INTERFACES
# Abstract Chair Interface
class Chair(ABC):
    @abstractmethod
    def sit_on(self):
        pass


# Abstract Sofa Interface
class Sofa(ABC):
    @abstractmethod
    def lie_on(self):
        pass


# CONCRETE PRODUCT IMPLEMENTATIONS
# Victorian Chair
class VictorianChair(Chair):
    def sit_on(self):
        return "Sitting on a Victorian chair"


# Modern Chair
class ModernChair(Chair):
    def sit_on(self):
        return "Sitting on a Modern chair"


# Victorian Sofa
class VictorianSofa(Sofa):
    def lie_on(self):
        return "Lying on a Victorian sofa"


# Modern Sofa
class ModernSofa(Sofa):
    def lie_on(self):
        return "Lying on a Modern sofa"


# ABSTRACT FACTORY INTERFACE
# Abstract Furniture Factory Interface
class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self) -> Chair:
        pass

    @abstractmethod
    def create_sofa(self) -> Sofa:
        pass


# CONCRETE FACTORIES
# Victorian Furniture Factory
class VictorianFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return VictorianChair()

    def create_sofa(self) -> Sofa:
        return VictorianSofa()


# Modern Furniture Factory
class ModernFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return ModernChair()

    def create_sofa(self) -> Sofa:
        return ModernSofa()


# CLIENT CODE:
def client_code(factory: FurnitureFactory):
    chair = factory.create_chair()
    sofa = factory.create_sofa()

    print(chair.sit_on())
    print(sofa.lie_on())


# Client using Victorian Furniture Factory
victorian_factory = VictorianFurnitureFactory()
client_code(victorian_factory)

# Client using Modern Furniture Factory
modern_factory = ModernFurnitureFactory()
client_code(modern_factory)