from project.animals.animal import Bird
from project.food import Meat, Vegetable, Fruit, Seed


class Owl(Bird):
    @staticmethod
    def make_sound():
        return "Hoot Hoot"

    @property
    def eaten_food(self):
        return [Meat]

    @property
    def gained_weight(self) -> float:
        return 0.25


class Hen(Bird):
    @staticmethod
    def make_sound():
        return "Cluck"

    @property
    def eaten_food(self):
        return [Vegetable, Fruit, Meat, Seed]

    @property
    def gained_weight(self) -> float:
        return 0.35
