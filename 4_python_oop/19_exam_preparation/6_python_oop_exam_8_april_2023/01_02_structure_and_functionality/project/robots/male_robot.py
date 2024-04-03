from project.robots.base_robot import BaseRobot


class MaleRobot(BaseRobot):
    INITIALLY_WEIGHT = 9
    POSSIBLE_SERVICE = "MainService"

    def __init__(self, name: str, kind: str, price: float):
        super().__init__(name, kind, price, self.INITIALLY_WEIGHT)

    def eating(self):
        self.weight += 3
