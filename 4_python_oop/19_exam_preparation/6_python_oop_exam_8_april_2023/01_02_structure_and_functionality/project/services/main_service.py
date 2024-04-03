from project.services.base_service import BaseService


class MainService(BaseService):
    FIXED_CAPACITY = 30

    def __init__(self, name: str):
        super().__init__(name, self.FIXED_CAPACITY)

    def details(self):
        if len(self.robots) == 0:
            result = f"{self.name} Main Service:\n"
            result += "Robots: none"
            return result
        else:
            result = f"{self.name} Main Service:\n"
            result += f"Robots: {' '.join([r.name for r in self.robots])}"
            return result
