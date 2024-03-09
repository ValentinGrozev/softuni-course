class Integer:
    ROMAN_SYMBOLS = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    def __init__(self, value):
        self.value = value

    @classmethod
    def from_float(cls, value: float):
        if isinstance(value, float):
            return cls(int(value))
        return "value is not a float"

    @classmethod
    def from_roman(cls, value: str):
        number = 0
        for char in range(len(value)):
            if char != 0 and cls.ROMAN_SYMBOLS[value[char]] > cls.ROMAN_SYMBOLS[value[char - 1]]:
                number += cls.ROMAN_SYMBOLS[value[char]] - 2 * cls.ROMAN_SYMBOLS[value[char - 1]]
            else:
                number += cls.ROMAN_SYMBOLS[value[char]]
        return cls(number)

    @classmethod
    def from_string(cls, value: str):
        if isinstance(value, str):
            return cls(int(value))
        return "wrong type"


first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("IV")
print(second_num.value)

print(Integer.from_float("2.6"))
print(Integer.from_float(2.6))

