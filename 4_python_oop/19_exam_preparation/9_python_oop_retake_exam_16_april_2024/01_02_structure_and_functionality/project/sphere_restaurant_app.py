from project.clients.base_client import BaseClient
from project.clients.regular_client import RegularClient
from project.clients.vip_client import VIPClient
from project.waiters.base_waiter import BaseWaiter
from project.waiters.full_time_waiter import FullTimeWaiter
from project.waiters.half_time_waiter import HalfTimeWaiter


class SphereRestaurantApp:
    VALID_TYPE_OF_WAITERS = {
        "FullTimeWaiter": FullTimeWaiter,
        "HalfTimeWaiter": HalfTimeWaiter,
    }

    VALID_TYPE_OF_CLIENTS = {
        "RegularClient": RegularClient,
        "VIPClient": VIPClient,
    }

    def __init__(self):
        self.waiters: list[BaseWaiter] = []
        self.clients: list[BaseClient] = []

    def hire_waiter(self, waiter_type: str, waiter_name: str, hours_worked: int):
        if waiter_type not in self.VALID_TYPE_OF_WAITERS:
            return f"{waiter_type} is not a recognized waiter type."

        try:
            next(filter(lambda w: w.name == waiter_name, self.waiters))
            return f"{waiter_name} is already on the staff."
        except StopIteration:

            waiter = self.VALID_TYPE_OF_WAITERS[waiter_type](waiter_name, hours_worked)
            self.waiters.append(waiter)
            return f"{waiter_name} is successfully hired as a {waiter_type}."

    def admit_client(self, client_type: str, client_name: str):
        if client_type not in self.VALID_TYPE_OF_CLIENTS:
            return f"{client_type} is not a recognized client type."

        try:
            next(filter(lambda c: c.name == client_name, self.clients))
            return f"{client_name} is already a client."
        except StopIteration:

            client = self.VALID_TYPE_OF_CLIENTS[client_type](client_name)
            self.clients.append(client)
            return f"{client_name} is successfully admitted as a {client_type}."

    def process_shifts(self, waiter_name: str):
        try:
            current_waiter = next(filter(lambda w: w.name == waiter_name, self.waiters))
            return current_waiter.report_shift()
        except StopIteration:
            return f"No waiter found with the name {waiter_name}."

    def process_client_order(self, client_name: str, order_amount: float):
        try:
            current_client = next(filter(lambda c: c.name == client_name, self.clients))
            points = current_client.earning_points(order_amount)
            return f"{client_name} earned {points} points from the order."
        except StopIteration:
            return f"{client_name} is not a registered client."

    def apply_discount_to_client(self, client_name: str):
        try:
            current_client = next(filter(lambda c: c.name == client_name, self.clients))
            discount_percent_and_points = current_client.apply_discount()
            return (f"{client_name} received a {discount_percent_and_points[0]}% discount. "
                    f"Remaining points {discount_percent_and_points[1]}")
        except StopIteration:
            return f"{client_name} cannot get a discount because this client is not admitted!"

    def generate_report(self):
        total_earnings = 0
        total_clients_unused_points = 0
        total_clients_count = len(self.clients)

        for waiter in self.waiters:
            total_earnings += waiter.calculate_earnings()

        for client in self.clients:
            total_clients_unused_points += client.points

        sorted_waiters = sorted(self.waiters, key=lambda x: -x.calculate_earnings())

        result = "$$ Monthly Report $$\n"
        result += f"Total Earnings: ${total_earnings:.2f}\n"
        result += f"Total Clients Unused Points: {int(total_clients_unused_points)}\n"
        result += f"Total Clients Count: {total_clients_count}\n"
        result += f"** Waiter Details **"

        for current_waiter in sorted_waiters:
            result += f"\n{current_waiter.__str__()}"

        return result
