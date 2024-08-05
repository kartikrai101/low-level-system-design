# Facade Pattern -> https://refactoring.guru/design-patterns/facade
class Amplifier:
    def on(self):
        print("Amplifier is on")

    def off(self):
        print("Amplifier is off")

    def set_volume(self, volume: int):
        print(f'Amplifier volume is set to {volume}')


class Tuner:
    def on(self):
        print("Tuner is on")
    def off(self):
        print("Tuner is off")
    def set_frequency(self, freq: float):
        print(f'Tuner frequency set to {freq}')


class DVDPlayer:
    def on(self) -> None:
        print("DVD player is on")

    def off(self) -> None:
        print("DVD player is off")

    def play(self, movie: str) -> None:
        print(f"Playing movie: {movie}")

    def stop(self) -> None:
        print("Stopping the movie")

    def eject(self) -> None:
        print("Ejecting the DVD")


class Projector:
    def on(self) -> None:
        print("Projector is on")

    def off(self) -> None:
        print("Projector is off")

    def wide_screen_mode(self) -> None:
        print("Projector in widescreen mode")


# Create a facade class to simplify the working for the end user
class HomeTheaterFacade:
    def __init__(self, amp: Amplifier, tuner: Tuner, dvd: DVDPlayer, projector: Projector):
        self.amp = amp
        self.tuner = tuner
        self.dvd = dvd
        self.projector = projector

    def watch_movie(self, movie: str):
        print("Get ready to watch a movie...")
        self.projector.on()
        self.projector.wide_screen_mode()
        self.amp.on()
        self.amp.set_volume(5)
        self.dvd.on()
        self.dvd.play(movie)

    def end_movie(self):
        print("Shutting down the movie theater...")
        self.dvd.stop()
        self.dvd.eject()
        self.dvd.off()
        self.amp.off()
        self.projector.off()


# Client code
if __name__ == "__main__":
    amp = Amplifier()
    tuner = Tuner()
    dvd = DVDPlayer()
    projector = Projector()

    home_theater = HomeTheaterFacade(amp, tuner, dvd, projector)

    home_theater.watch_movie("Inception")
    print("\n")
    home_theater.end_movie()