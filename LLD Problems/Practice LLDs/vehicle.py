from vehicle_type import VehicleType


class Vehicle:
    def __init__(self, vehicle_type: VehicleType, license_plate: str):
        self.vehicle_type = vehicle_type
        self.license_plate = license_plate

    def get_type(self):
        return self.vehicle_type