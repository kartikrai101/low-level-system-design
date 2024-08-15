from parking_lot import ParkingLot
from level import Level
from car import Car
from motorcycle import Motorcycle
from truck import Truck


class ParkingLotDemo:
    @staticmethod
    def run():
        parking_lot = ParkingLot.get_instance()
        parking_lot.add_level(Level(1, 100))
        parking_lot.add_level(Level(2, 80))

        car = Car("UP 1232-AD")
        truck = Truck("UP 5463-WS")
        bike = Motorcycle("DL 4323-KJ")

        # Park the vehicles
        parking_lot.park_vehicle(car)
        parking_lot.park_vehicle(truck)
        parking_lot.park_vehicle(bike)

        # display availability
        parking_lot.display_availability()

        # un-park vehicle
        parking_lot.unpark_vehicle(bike)

        # display the updated availability
        parking_lot.display_availability()


if __name__ == "__main__":
    ParkingLotDemo.run()