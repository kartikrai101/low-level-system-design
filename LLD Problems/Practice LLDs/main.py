from parking_lot import ParkingLot
from level import Level
from car import Car
from truck import Truck
from bike import Bike


class Main:
    @staticmethod
    def run():
        parking_lot = ParkingLot.get_instance()
        parking_lot.add_level(Level(0, 100))
        parking_lot.add_level(Level(1, 50))

        # create our vehicles
        car = Car("UP-4532-AD")
        bike = Bike("UP-6765-FS")
        truck = Truck("HR-2311-GH")
        car2 = Car("DL-7787-TR")

        # park the vehicles
        parking_lot.park_vehicle(car)
        parking_lot.park_vehicle(bike)
        parking_lot.park_vehicle(truck)
        parking_lot.park_vehicle(car2)

        # display availability
        parking_lot.display_availability()

        # un-park vehicle
        parking_lot.unpark_vehicle(car2)

        # display the updated availability
        parking_lot.display_availability()

if __name__ == "__main__":
    Main.run()