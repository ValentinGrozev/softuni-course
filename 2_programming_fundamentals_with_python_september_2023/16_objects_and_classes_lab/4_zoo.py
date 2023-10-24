class Zoo:
    __animals = 0

    def __init__(self, name_of_zoo):
        self.name_of_zoo = name_of_zoo
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, species):
        if species == "mammal":
            return f"Mammals in {self.name_of_zoo}: {', '.join(self.mammals)}\nTotal animals: {Zoo.__animals}"
        elif species == "fish":
            return f"Fishes in {self.name_of_zoo}: {', '.join(self.fishes)}\nTotal animals: {Zoo.__animals}"
        elif species == "bird":
            return f"Birds in {self.name_of_zoo}: {', '.join(self.birds)}\nTotal animals: {Zoo.__animals}"


zoo_name = input()
zoo = Zoo(zoo_name)
count = int(input())

for current_animal in range(count):
    animal = input().split()
    type_of_animal = animal[0]
    name_of_animal = animal[1]
    zoo.add_animal(type_of_animal, name_of_animal)

info_for_specific_species = input()
print(zoo.get_info(info_for_specific_species))
