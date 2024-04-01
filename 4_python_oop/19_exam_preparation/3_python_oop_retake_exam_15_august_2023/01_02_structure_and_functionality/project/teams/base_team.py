from abc import ABC, abstractmethod


class BaseTeam(ABC):

    def __init__(self, name: str, country: str, advantage: int, budget: float):
        self.name = name
        self.country = country
        self.advantage = advantage
        self.budget = budget
        self.wins = 0
        self.equipment = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Team name cannot be empty!")
        self.__name = value

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, value):
        if len(value.strip()) < 2:
            raise ValueError("Team country should be at least 2 symbols long!")
        self.__country = value

    @property
    def advantage(self):
        return self.__advantage

    @advantage.setter
    def advantage(self, value):
        if value <= 0:
            raise ValueError("Advantage must be greater than zero!")
        self.__advantage = value

    @abstractmethod
    def win(self):
        pass

    def get_statistics(self):
        result = f"Name: {self.name}\n"
        result += f"Country: {self.country}\n"
        result += f"Advantage: {self.advantage} points\n"
        result += f"Budget: {self.budget:.2f}EUR\n"
        result += f"Wins: {self.wins}\n"

        total_equipment_price = sum([p.price for p in self.equipment])
        result += f"Total Equipment Price: {total_equipment_price:.2f}\n"

        average_protection = sum(p.protection for p in self.equipment) / len(self.equipment) if self.equipment else 0
        result += f"Average Protection: {int(average_protection)}"

        return result
