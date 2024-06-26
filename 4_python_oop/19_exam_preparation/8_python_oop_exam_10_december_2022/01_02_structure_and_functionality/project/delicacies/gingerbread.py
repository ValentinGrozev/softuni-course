from project.delicacies.delicacy import Delicacy


class Gingerbread(Delicacy):
    FIXED_PORTION = 200

    def __init__(self, name: str, price: int):
        super().__init__(name, self.FIXED_PORTION, price)

    def details(self):
        return f"Gingerbread {self.name}: 200g - {self.price:.2f}lv."
