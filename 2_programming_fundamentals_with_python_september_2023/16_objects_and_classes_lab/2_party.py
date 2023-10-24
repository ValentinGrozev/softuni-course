class Party:
    def __init__(self):
        self.people = []

    def printing_function(self):
        return f"Going: {', '.join(self.people)}\nTotal: {len(self.people)}"


command = input()
party_people = Party()

while command != "End":
    party_people.people.append(command)

    command = input()

print(party_people.printing_function())
