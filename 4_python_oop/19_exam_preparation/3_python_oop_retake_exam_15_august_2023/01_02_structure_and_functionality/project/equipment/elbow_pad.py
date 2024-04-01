from project.equipment.base_equipment import BaseEquipment


class ElbowPad(BaseEquipment):
    FIXED_PROTECTION = 90
    FIXED_PRICE = 25.0

    def __init__(self):
        super().__init__(self.FIXED_PROTECTION, self.FIXED_PRICE)

    def increase_price(self):
        increased = 0.1 * self.price
        self.price += increased
