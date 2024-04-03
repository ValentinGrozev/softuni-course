from project.robots.base_robot import BaseRobot


class FemaleRobot(BaseRobot):
    INITIALLY_WEIGHT = 7
    POSSIBLE_SERVICE = "SecondaryService"

    def __init__(self, name: str, kind: str, price: float):
        super().__init__(name, kind, price, self.INITIALLY_WEIGHT)

    def eating(self):
        self.weight += 1
