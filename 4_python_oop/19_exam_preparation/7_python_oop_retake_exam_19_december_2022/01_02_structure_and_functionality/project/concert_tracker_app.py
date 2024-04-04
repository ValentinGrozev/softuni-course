from typing import List
from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.musician import Musician
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    VALID_TYPES_OF_MUSICIAN = {
        "Guitarist": Guitarist,
        "Drummer": Drummer,
        "Singer": Singer
    }

    def __init__(self):
        self.bands: List[Band] = []
        self.musicians: List[Musician] = []
        self.concerts: List[Concert] = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self.VALID_TYPES_OF_MUSICIAN:
            raise ValueError("Invalid musician type!")

        try:
            next(filter(lambda n: n.name == name, self.musicians))
            raise Exception(f"{name} is already a musician!")
        except StopIteration:

            musician = self.VALID_TYPES_OF_MUSICIAN[musician_type](name, age)
            self.musicians.append(musician)
            return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        try:
            next(filter(lambda b: b.name == name, self.bands))
            raise Exception(f"{name} band is already created!")
        except StopIteration:

            band = Band(name)
            self.bands.append(band)
            return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        try:
            current_concert = next(filter(lambda c: c.place == place, self.concerts))
            raise Exception(f"{place} is already registered for {current_concert.genre} concert!")
        except StopIteration:

            concert = Concert(genre, audience, ticket_price, expenses, place)
            self.concerts.append(concert)
            return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        try:
            musician = next(filter(lambda m: m.name == musician_name, self.musicians))
        except StopIteration:
            raise Exception(f"{musician_name} isn't a musician!")

        try:
            band = next(filter(lambda b: b.name == band_name, self.bands))
        except StopIteration:
            raise Exception(f"{band_name} isn't a band!")

        band.members.append(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        try:
            band = next(filter(lambda b: b.name == band_name, self.bands))
        except StopIteration:
            raise Exception(f"{band_name} isn't a band!")

        try:
            musician = next(filter(lambda m: m.name == musician_name, band.members))
        except StopIteration:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        band.members.remove(musician)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        band = next(filter(lambda b: b.name == band_name, self.bands))
        concert = next(filter(lambda c: c.place == concert_place, self.concerts))

        validate_type_of_musicians_in_bad = {
            "Guitarist": False,
            "Drummer": False,
            "Singer": False
        }

        for member in band.members:
            if member.__class__.__name__ in validate_type_of_musicians_in_bad:
                validate_type_of_musicians_in_bad[member.__class__.__name__] = True

        if not all(validate_type_of_musicians_in_bad.values()):
            raise Exception(f"{band.name} can't start the concert because it doesn't have enough members!")

        if concert.genre == "Rock":
            for current_member in band.members:
                if (current_member.__class__.__name__ == "Drummer" and "play the drums with drumsticks"
                        not in current_member.skills):
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if (current_member.__class__.__name__ == "Singer" and "sing high pitch notes"
                        not in current_member.skills):
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if current_member.__class__.__name__ == "Guitarist" and "play rock" not in current_member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

        elif concert.genre == "Metal":
            for current_member in band.members:
                if (current_member.__class__.__name__ == "Drummer" and "play the drums with drumsticks"
                        not in current_member.skills):
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if (current_member.__class__.__name__ == "Singer" and "sing low pitch notes"
                        not in current_member.skills):
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if current_member.__class__.__name__ == "Guitarist" and "play metal" not in current_member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

        elif concert.genre == "Jazz":
            for current_member in band.members:
                if (current_member.__class__.__name__ == "Drummer" and "play the drums with drum brushes"
                        not in current_member.skills):
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if (current_member.__class__.__name__ == "Singer" and
                        ("sing high pitch notes" not in current_member.skills
                         or "sing low pitch notes" not in current_member.skills)):
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if current_member.__class__.__name__ == "Guitarist" and "play jazz" not in current_member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = (concert.audience * concert.ticket_price) - concert.expenses

        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."
