from project.equipment.base_equipment import BaseEquipment


class KneePad(BaseEquipment):
    FIXED_PROTECTION = 120
    FIXED_PRICE = 15.0

    def __init__(self):
        super().__init__(self.FIXED_PROTECTION, self.FIXED_PRICE)

    def increase_price(self):
        increased = 0.2 * self.price
        self.price += increased
