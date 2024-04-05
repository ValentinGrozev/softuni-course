from typing import List
from project.booths.booth import Booth
from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.delicacy import Delicacy
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    VALID_TYPES_OF_DELICACY = {
        "Gingerbread": Gingerbread,
        "Stolen": Stolen
    }

    VALID_TYPES_OF_BOOTH = {
        "Open Booth": OpenBooth,
        "Private Booth": PrivateBooth,
    }

    def __init__(self):
        self.booths: List[Booth] = []
        self.delicacies: List[Delicacy] = []
        self.income: float = 0.0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        if type_delicacy not in self.VALID_TYPES_OF_DELICACY:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        try:
            next(filter(lambda d: d.name == name, self.delicacies))
            raise Exception(f"{name} already exists!")
        except StopIteration:

            delicacy = self.VALID_TYPES_OF_DELICACY[type_delicacy](name, price)
            self.delicacies.append(delicacy)
            return f"Added delicacy {delicacy.name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        if type_booth not in self.VALID_TYPES_OF_BOOTH:
            raise Exception(f"{type_booth} is not a valid booth!")

        try:
            next(filter(lambda b: b.booth_number == booth_number, self.booths))
            raise Exception(f"Booth number {booth_number} already exists!")
        except StopIteration:

            booth = self.VALID_TYPES_OF_BOOTH[type_booth](booth_number, capacity)
            self.booths.append(booth)
            return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        for current_booth in self.booths:
            if current_booth.capacity >= number_of_people and current_booth.is_reserved is False:
                current_booth.reserve(number_of_people)
                return f"Booth {current_booth.booth_number} has been reserved for {number_of_people} people."

        raise Exception(f"No available booth for {number_of_people} people!")

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        try:
            current_booth = next(filter(lambda b: b.booth_number == booth_number, self.booths))
        except StopIteration:
            raise Exception(f"Could not find booth {booth_number}!")

        try:
            current_delicacy = next(filter(lambda d: d.name == delicacy_name, self.delicacies))
        except StopIteration:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        current_booth.delicacy_orders.append(current_delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        current_booth = next(filter(lambda b: b.booth_number == booth_number, self.booths))
        price_for_delicacy_orders = 0

        for cur_delicacy in current_booth.delicacy_orders:
            price_for_delicacy_orders += cur_delicacy.price

        bill = price_for_delicacy_orders + current_booth.price_for_reservation
        self.income += bill

        current_booth.is_reserved = False
        current_booth.price_for_reservation = 0.0
        current_booth.delicacy_orders = []

        result = f"Booth {booth_number}:\n"
        result += f"Bill: {bill:.2f}lv."

        return result

    def get_income(self):
        return f"Income: {self.income:.2f}lv."
