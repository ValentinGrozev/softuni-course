from typing import List

from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def add_animal(self, animal: Animal, price: int) -> str:
        if self.__budget >= price and len(self.animals) < self.__animal_capacity:
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        if self.__budget < price and len(self.animals) < self.__animal_capacity:
            return "Not enough budget"
        else:
            return "Not enough space for animal"

    def hire_worker(self, worker: Worker) -> str:
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name: str) -> str:
        for current_worker in self.workers:
            if worker_name == current_worker.name:
                self.workers.remove(current_worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self) -> str:
        total_salary = 0
        for current_worker in self.workers:
            total_salary += current_worker.salary

        if self.__budget >= total_salary:
            self.__budget -= total_salary
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return f"You have no budget to pay your workers. They are unhappy"

    def tend_animals(self) -> str:
        total_cost = 0
        for current_animal in self.animals:
            total_cost += current_animal.money_for_care

        if self.__budget >= total_cost:
            self.__budget -= total_cost
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int) -> None:
        self.__budget += amount

    def animals_status(self) -> str:
        result = f"You have {len(self.animals)} animals\n"
        all_lions = [lion for lion in self.animals if lion.__class__.__name__ == "Lion"]
        result += f"----- {len(all_lions)} Lions:\n"
        result += '\n'.join([lion.__repr__() for lion in all_lions])

        all_tigers = [tiger for tiger in self.animals if tiger.__class__.__name__ == "Tiger"]
        result += f"\n----- {len(all_tigers)} Tigers:\n"
        result += '\n'.join([tiger.__repr__() for tiger in all_tigers])

        all_cheetahs = [cheetah for cheetah in self.animals if cheetah.__class__.__name__ == "Cheetah"]
        result += f"\n----- {len(all_cheetahs)} Cheetahs:\n"
        result += '\n'.join([cheetah.__repr__() for cheetah in all_cheetahs])

        return result.strip()

    def workers_status(self) -> str:
        result = f"You have {len(self.workers)} workers\n"
        all_keepers = [keeper for keeper in self.workers if keeper.__class__.__name__ == "Keeper"]
        result += f"----- {len(all_keepers)} Keepers:\n"
        result += '\n'.join([keeper.__repr__() for keeper in all_keepers])

        all_caretakers = [caretaker for caretaker in self.workers if caretaker.__class__.__name__ == "Caretaker"]
        result += f"\n----- {len(all_caretakers)} Caretakers:\n"
        result += '\n'.join([caretaker.__repr__() for caretaker in all_caretakers])

        all_vets = [vet for vet in self.workers if vet.__class__.__name__ == "Vet"]
        result += f"\n----- {len(all_vets)} Vets:\n"
        result += '\n'.join([vet.__repr__() for vet in all_vets])

        return result.strip()
