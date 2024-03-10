from typing import List
from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    DVD_CAPACITY = 15
    CUSTOMER_CAPACITY = 10

    def __init__(self, name: str):
        self.name = name
        self.customers: List[Customer] = []
        self.dvds: List[DVD] = []

    @staticmethod
    def dvd_capacity() -> int:
        return MovieWorld.DVD_CAPACITY

    @staticmethod
    def customer_capacity() -> int:
        return MovieWorld.CUSTOMER_CAPACITY

    def add_customer(self, customer: Customer) -> None:
        if len(self.customers) < MovieWorld.CUSTOMER_CAPACITY:
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD) -> None:
        if len(self.dvds) < MovieWorld.DVD_CAPACITY:
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        # Option with for loop
        # for current_dvd in self.dvds:
        #     if current_dvd.id == dvd_id:
        #         dvd = current_dvd
        #         break
        #
        # for current_customer in self.customers:
        #     if current_customer.id == customer_id:
        #         customer = current_customer
        #         break

        customer = next(filter(lambda c: c.id == customer_id, self.customers))
        dvd = next(filter(lambda d: d.id == dvd_id, self.dvds))

        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"

        if dvd.is_rented:
            return "DVD is already rented"

        if dvd.age_restriction > customer.age:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

        customer.rented_dvds.append(dvd)
        dvd.is_rented = True
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id: Customer, dvd_id: DVD):
        customer = next(filter(lambda c: c.id == customer_id, self.customers))
        dvd = next(filter(lambda d: d.id == dvd_id, self.dvds))

        if dvd in customer.rented_dvds:
            customer.rented_dvds.remove(dvd)
            dvd.is_rented = False
            return f"{customer.name} has successfully returned {dvd.name}"
        return f"{customer.name} does not have that DVD"

    def __repr__(self):
        result = ""

        for customer in self.customers:
            result += f"{customer.__repr__()}\n"

        for dvd in self.dvds:
            result += f"{dvd.__repr__()}\n"

        return result.strip()
