from project.teams.base_team import BaseTeam


class OutdoorTeam(BaseTeam):
    ADVANTAGE_TO_INCREASE = 115

    def __init__(self, name: str, country: str, advantage: int):
        super().__init__(name, country, advantage, 1000.0)

    def win(self):
        self.advantage += self.ADVANTAGE_TO_INCREASE
        self.wins += 1
