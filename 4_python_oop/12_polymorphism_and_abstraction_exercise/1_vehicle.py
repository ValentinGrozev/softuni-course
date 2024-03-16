from abc import abstractmethod, ABC


class Vehicle(ABC):
    CAR_ADDITIONAL_FUEL_CONSUMPTION_PER_KM = 0.9
    TRUCK_ADDITIONAL_FUEL_CONSUMPTION_PER_KM = 1.6
    FILL_PERCENTAGE_OF_TRUCk_TANK = 0.95

    @abstractmethod
    def drive(self, distance: int):
        pass

    @abstractmethod
    def refuel(self, refuel: int):
        pass


class Car(Vehicle):
    def __init__(self, fuel_quantity: int, fuel_consumption: int):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance: int) -> None:
        if self.fuel_quantity >= (self.fuel_consumption + Vehicle.CAR_ADDITIONAL_FUEL_CONSUMPTION_PER_KM) * distance:
            self.fuel_quantity -= (self.fuel_consumption + Vehicle.CAR_ADDITIONAL_FUEL_CONSUMPTION_PER_KM) * distance

    def refuel(self, refuel: int) -> None:
        self.fuel_quantity += refuel


class Truck(Vehicle):
    def __init__(self, fuel_quantity: int, fuel_consumption: int):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance: int) -> None:
        if self.fuel_quantity >= (self.fuel_consumption + Vehicle.TRUCK_ADDITIONAL_FUEL_CONSUMPTION_PER_KM) * distance:
            self.fuel_quantity -= (self.fuel_consumption + Vehicle.TRUCK_ADDITIONAL_FUEL_CONSUMPTION_PER_KM) * distance

    def refuel(self, refuel: int) -> None:
        self.fuel_quantity += refuel * Vehicle.FILL_PERCENTAGE_OF_TRUCk_TANK


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
