from project.services.base_service import BaseService


class SecondaryService(BaseService):
    FIXED_CAPACITY = 15

    def __init__(self, name: str):
        super().__init__(name, self.FIXED_CAPACITY)

    def details(self):
        if len(self.robots) == 0:
            result = f"{self.name} Secondary Service:\n"
            result += "Robots: none"
            return result
        else:
            result = f"{self.name} Secondary Service:\n"
            result += f"Robots: {' '.join([r.name for r in self.robots])}"
            return result
