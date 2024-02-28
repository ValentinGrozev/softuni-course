from project.player import Player


class Guild:

    def __init__(self, name: str):
        self.name = name
        self.players = []

    def assign_player(self, player: Player) -> str:
        if player in self.players:
            return f"Player {player.name} is already in the guild."

        elif player.guild != self.name and player.guild != "Unaffiliated":
            return f"Player {player.name} is in another guild."

        self.players.append(player)
        player.guild = self.name
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str) -> str:
        for current_player in self.players:
            if current_player.name == player_name:
                current_player.guild = "Unaffiliated"
                self.players.remove(current_player)
                return f"Player {player_name} has been removed from the guild."

        return f"Player {player_name} is not in the guild."

    def guild_info(self) -> str:
        result = f"Guild: {self.name}\n"

        for player in self.players:
            result += f"{player.player_info()}"

        return result
