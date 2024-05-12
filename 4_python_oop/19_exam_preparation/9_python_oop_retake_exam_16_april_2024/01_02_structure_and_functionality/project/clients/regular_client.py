from math import floor
from project.clients.base_client import BaseClient


class RegularClient(BaseClient):
    MEMBERSHIP_TYPE = "Regular"
    MONEY_SPENT_FOR_ONE_POINT = 10

    def __init__(self, name: str):
        super().__init__(name, self.MEMBERSHIP_TYPE)

    def earning_points(self, order_amount: float):
        earned_points = floor(order_amount / self.MONEY_SPENT_FOR_ONE_POINT)
        self.points += earned_points
        return earned_points
