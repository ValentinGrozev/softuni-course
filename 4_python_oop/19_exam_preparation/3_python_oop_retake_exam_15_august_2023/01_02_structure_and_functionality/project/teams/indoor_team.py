from project.teams.base_team import BaseTeam


class IndoorTeam(BaseTeam):
    ADVANTAGE_TO_INCREASE = 145

    def __init__(self, name: str, country: str, advantage: int):
        super().__init__(name, country, advantage, 500.0)

    def win(self):
        self.advantage += self.ADVANTAGE_TO_INCREASE
        self.wins += 1
