class vowels:
    def __init__(self, string: str):
        self.string = string
        self.vowels = ["a", "e", "i", "u", "y", "o"]
        self.idx = -1
        self.vowels_found = [vowel for vowel in self.string if vowel.lower() in self.vowels]

    def __iter__(self):
        return self

    def __next__(self):
        self.idx += 1
        if self.idx == len(self.vowels_found):
            raise StopIteration
        return self.vowels_found[self.idx]


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
