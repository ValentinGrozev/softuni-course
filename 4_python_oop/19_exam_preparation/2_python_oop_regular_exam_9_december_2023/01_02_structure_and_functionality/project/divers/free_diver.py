from project.divers.base_diver import BaseDiver


class FreeDiver(BaseDiver):
    INITIAL_OXYGEN_LEVEL = 120

    def __init__(self, name: str):
        super().__init__(name, self.INITIAL_OXYGEN_LEVEL)

    def miss(self, time_to_catch: int):
        reduced_oxygen_level = round(0.6 * time_to_catch)

        if self.oxygen_level - reduced_oxygen_level < 0:
            self.oxygen_level = 0
        else:
            self.oxygen_level -= reduced_oxygen_level

    def renew_oxy(self):
        self.oxygen_level = self.INITIAL_OXYGEN_LEVEL
