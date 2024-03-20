from abc import ABC, abstractmethod


class FormulaTeam(ABC):
    def __init__(self, budget: int):
        self.budget = budget

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value: int):
        if value < 1000000:
            raise ValueError("F1 is an expensive sport, find more sponsors!")
        self.__budget = value

    @property
    @abstractmethod
    def sponsors(self):
        pass

    @property
    @abstractmethod
    def expenses_for_one_race(self):
        pass

    def calculate_revenue_after_race(self, race_pos: int) -> str:
        revenue = 0

        for sponsor in self.sponsors.values():
            for pos in sponsor:
                if race_pos <= pos:
                    revenue += sponsor[pos]
                    break

        revenue -= self.expenses_for_one_race
        self.budget += revenue

        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
