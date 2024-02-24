from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, new_pokemon: Pokemon) -> str:
        if new_pokemon not in self.pokemons:
            self.pokemons.append(new_pokemon)
            return f"Caught {Pokemon.pokemon_details(new_pokemon)}"
        else:
            return f"This pokemon is already caught"

    def release_pokemon(self, pokemon_name: str) -> str:
        # first option:
        for current_pokemon in self.pokemons:
            if current_pokemon.name == pokemon_name:
                self.pokemons.remove(current_pokemon)
                return f"You have released {pokemon_name}"
        return f"Pokemon is not caught"

        # second option:
        # try:
        #     current_pokemon = next(filter(lambda p: p.name == pokemon_name, self.pokemons))
        # except StopIteration:
        #     return "Pokemon is not caught"
        #
        # self.pokemons.remove(current_pokemon)
        # return f"You have released {pokemon_name}"

    def trainer_data(self) -> str:
        result = ""
        result += f"Pokemon Trainer {self.name}\n"
        result += f"Pokemon count {len(self.pokemons)}\n"

        for caught_pokemon in self.pokemons:
            result += f"- {Pokemon.pokemon_details(caught_pokemon)}"

        return result


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())
