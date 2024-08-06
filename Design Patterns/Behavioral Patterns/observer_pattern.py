from abc import ABC, abstractmethod
# Observer -> Subscriber
# Subject -> Publisher


class Observer(ABC):
    @abstractmethod
    def update(self, temperature: float, humidity: float, pressure: float) -> None:
        pass


class Subject(ABC):
    @abstractmethod
    def register_observer(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def remove_observer(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify_observers(self) -> None:
        pass


class WeatherStation(Subject):
    def __init__(self) -> None:
        self._observers = []
        self._temperature = 0.0
        self._humidity = 0.0
        self._pressure = 0.0

    def register_observer(self, observer: Observer) -> None:
        self._observers.append(observer)

    def remove_observer(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify_observers(self) -> None:
        for observer in self._observers:
            observer.update(self._temperature, self._humidity, self._pressure)

    def set_measurements(self, temperature: float, humidity: float, pressure: float) -> None:
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        self.notify_observers()


class CurrentConditionsDisplay(Observer):
    def __init__(self, weather_station: Subject) -> None:
        self._temperature = 0.0
        self._humidity = 0.0
        self._weather_station = weather_station
        self._weather_station.register_observer(self)

    def update(self, temperature: float, humidity: float, pressure: float) -> None:
        self._temperature = temperature
        self._humidity = humidity
        self.display()

    def display(self) -> None:
        print(f"Current conditions: {self._temperature}°C and {self._humidity}% humidity")


class ForecastDisplay(Observer):
    def __init__(self, weather_station: Subject) -> None:
        self._pressure = 0.0
        self._weather_station = weather_station
        self._weather_station.register_observer(self)

    def update(self, temperature: float, humidity: float, pressure: float) -> None:
        self._pressure = pressure
        self.display()

    def display(self) -> None:
        print(f"Forecast: More of the same at {self._pressure} pressure")


if __name__ == "__main__":
    weather_station = WeatherStation()

    current_display = CurrentConditionsDisplay(weather_station)
    forecast_display = ForecastDisplay(weather_station)

    weather_station.set_measurements(25.0, 65, 1013.1)
    weather_station.set_measurements(28.0, 70, 1012.0)
