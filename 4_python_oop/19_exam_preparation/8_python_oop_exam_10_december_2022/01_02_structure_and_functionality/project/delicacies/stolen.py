from project.delicacies.delicacy import Delicacy


class Stolen(Delicacy):
    FIXED_PORTION = 250

    def __init__(self, name: str, price: int):
        super().__init__(name, self.FIXED_PORTION, price)

    def details(self):
        return f"Stolen {self.name}: 250g - {self.price:.2f}lv."
