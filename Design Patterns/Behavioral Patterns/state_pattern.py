from abc import ABC, abstractmethod


class Context:
    def __init__(self, state: 'State') -> None:
        self._state = state

    def set_state(self, state: 'State') -> None:
        self._state = state

    def request(self) -> None:
        self._state.handle(self)


class State(ABC):
    @abstractmethod
    def handle(self, context: Context) -> None:
        pass


class ConcreteStateA(State):
    def handle(self, context: Context) -> None:
        print("ConcreteStateA handling request and changing state to ConcreteStateB")
        context.set_state(ConcreteStateB())


class ConcreteStateB(State):
    def handle(self, context: Context) -> None:
        print("ConcreteStateB handling request and changing state to ConcreteStateA")
        context.set_state(ConcreteStateA())


if __name__ == "__main__":
    initial_state = ConcreteStateA()
    context = Context(initial_state)

    context.request()  # Should handle by ConcreteStateA and change to ConcreteStateB
    context.request()  # Should handle by ConcreteStateB and change to ConcreteStateA
