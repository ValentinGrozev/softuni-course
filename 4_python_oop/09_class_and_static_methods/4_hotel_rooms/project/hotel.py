from typing import List
from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms: List[Room] = []
        self.guests: int = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f'{stars_count} stars Hotel')

    def add_room(self, room: Room) -> None:
        self.rooms.append(room)

    def take_room(self, room_number: int, people: int) -> None or str:
        for current_room in self.rooms:
            if room_number == current_room.number and not current_room.is_taken:
                if current_room.capacity <= people:
                    current_room.take_room(people)
                    self.guests += people
                    return
                return f"Room number {current_room.number} cannot be taken"

    def free_room(self, room_number: int) -> str or None:
        for current_room in self.rooms:
            if room_number == current_room.number and current_room.is_taken:
                people = current_room.guests
                current_room.free_room()
                self.guests -= people
                return
            return f"Room number {current_room.number} is not taken"

    def status(self):
        result = f"Hotel {self.name} has {self.guests} total guests"
        free_rooms = f'Free rooms: {", ".join(str(r.number) for r in self.rooms if not r.is_taken)}'
        taken_rooms = f'Taken rooms: {", ".join(str(r.number) for r in self.rooms if r.is_taken)}'
        return f'{result}\n{free_rooms}\n{taken_rooms}'
