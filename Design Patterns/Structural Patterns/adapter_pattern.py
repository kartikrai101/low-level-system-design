# Adapter Pattern: https://refactoring.guru/design-patterns/adapter
class EuropeanSocketInterface:
    def voltage(self) -> int:
        return 230

    def live(self) -> int:
        return 1

    def neutral(self) -> int:
        return -1


class AmericanSocketInterface:
    def voltage(self) -> int:
        return 120

    def live(self) -> int:
        return 1

    def neutral(self) -> int:
        return -1

    def ground(self) -> int:
        return 0


class EuropeanToAmericanAdapter(AmericanSocketInterface):
    def __init__(self, european_socket: EuropeanSocketInterface) -> None:
        self.european_socket = european_socket

    def voltage(self) -> int:
        return self.european_socket.voltage()

    def live(self) -> int:
        return self.european_socket.live()

    def neutral(self) -> int:
        return self.european_socket.neutral()

    def ground(self) -> int:
        return 0  # European sockets don't have ground


def test_socket(socket: AmericanSocketInterface) -> None:
    print(f"Voltage: {socket.voltage()}")
    print(f"Live: {socket.live()}")
    print(f"Neutral: {socket.neutral()}")
    print(f"Ground: {socket.ground()}")


if __name__ == "__main__":
    european_socket = EuropeanSocketInterface()
    adapter = EuropeanToAmericanAdapter(european_socket)
    print("Testing European to American Adapter:")
    test_socket(adapter)
