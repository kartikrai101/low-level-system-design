# Composite Pattern ->
from abc import ABC, abstractmethod


# define the component interface
class Component(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_size(self) -> int:
        pass

    def add(self, component: 'Component') -> None:
        pass

    def remove(self, component: 'Component') -> None:
        pass

    def get_child(self, index: int) -> 'Component':
        pass


# create leaf and composite classes
class File(Component):
    def __init__(self, name: str, size: int) -> None:
        self._name = name
        self._size = size

    def get_name(self) -> str:
        return self._name

    def get_size(self) -> int:
        return self._size


class Directory(Component):
    def __init__(self, name: str) -> None:
        self._name = name
        self._children = []

    def get_name(self) -> str:
        return self._name

    def get_size(self) -> int:
        total_size = 0
        for child in self._children:
            total_size += child.get_size()
        return total_size

    def add(self, component: Component) -> None:
        self._children.append(component)

    def remove(self, component: Component) -> None:
        self._children.remove(component)

    def get_child(self, index: int) -> Component:
        return self._children[index]


# using the composite pattern
if __name__ == "__main__":
    root = Directory("root")

    file1 = File("file1.txt", 100)
    file2 = File("file2.txt", 200)
    file3 = File("file3.txt", 300)

    dir1 = Directory("dir1")
    dir2 = Directory("dir2")

    root.add(file1)
    root.add(dir1)

    dir1.add(file2)
    dir1.add(dir2)

    dir2.add(file3)

    print(f"Total size of root directory: {root.get_size()} bytes")
    print(f"Total size of dir1 directory: {dir1.get_size()} bytes")
    print(f"Total size of dir2 directory: {dir2.get_size()} bytes")
