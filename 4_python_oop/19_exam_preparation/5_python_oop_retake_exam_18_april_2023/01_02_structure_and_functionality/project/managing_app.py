from typing import List

from project.route import Route
from project.user import User
from project.vehicles.base_vehicle import BaseVehicle
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:
    VALID_TYPES_OF_VEHICLES = {
        "PassengerCar": PassengerCar,
        "CargoVan": CargoVan
    }

    def __init__(self):
        self.users: List[User] = []
        self.vehicles: List[BaseVehicle] = []
        self.routes: List[Route] = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        try:
            next(filter(lambda u: u.driving_license_number == driving_license_number, self.users))
            return f"{driving_license_number} has already been registered to our platform."
        except StopIteration:

            new_user = User(first_name, last_name, driving_license_number)
            self.users.append(new_user)
            return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in self.VALID_TYPES_OF_VEHICLES:
            return f"Vehicle type {vehicle_type} is inaccessible."

        try:
            next(filter(lambda v: v.license_plate_number == license_plate_number, self.vehicles))
            return f"{license_plate_number} belongs to another vehicle."
        except StopIteration:

            new_vehicle = self.VALID_TYPES_OF_VEHICLES[vehicle_type](brand, model, license_plate_number)
            self.vehicles.append(new_vehicle)
            return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        try:
            filtered_road = next(
                filter(lambda r: r.start_point == start_point and r.end_point == end_point, self.routes))
        except StopIteration:
            filtered_road = None

        if filtered_road is not None:
            if filtered_road.length == length:
                return f"{start_point}/{end_point} - {length} km had already been added to our platform."
            elif filtered_road.length < length:
                return f"{start_point}/{end_point} shorter route had already been added to our platform."
            elif filtered_road.length > length:
                filtered_road.is_locked = True

        route_id = len(self.routes) + 1
        new_route = Route(start_point, end_point, length, route_id)
        self.routes.append(new_route)
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,
                  is_accident_happened: bool):
        user = next(filter(lambda u: u.driving_license_number == driving_license_number, self.users))
        vehicle = next(filter(lambda v: v.license_plate_number == license_plate_number, self.vehicles))
        route = next(filter(lambda r: r.route_id == route_id, self.routes))

        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle.drive(route.length)

        if is_accident_happened:
            vehicle.change_status()
            user.decrease_rating()
        else:
            user.increase_rating()

        return str(vehicle)

    def repair_vehicles(self, count: int):
        damaged_vehicles = [v for v in self.vehicles if v.is_damaged]
        sorted_damaged_vehicles = sorted(damaged_vehicles, key=lambda v: (v.brand, v.model))

        if len(sorted_damaged_vehicles) > count:
            sorted_damaged_vehicles = sorted_damaged_vehicles[:count]

        for v in sorted_damaged_vehicles:
            v.change_status()
            v.recharge()

        return f"{len(sorted_damaged_vehicles)} vehicles were successfully repaired!"

    def users_report(self):
        sorted_users = sorted(self.users, key=lambda u: -u.rating)

        result = "*** E-Drive-Rent ***\n"
        result += '\n'.join([str(user) for user in sorted_users])

        return result
