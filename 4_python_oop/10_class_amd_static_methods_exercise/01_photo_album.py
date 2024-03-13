from math import ceil
from typing import List


class PhotoAlbum:
    MAX_PHOTO_ON_PAGE: int = 4
    DASH_COUNTER: int = 11
    SYMBOL: str = '-'

    def __init__(self, pages: int):
        self.pages = pages
        self.photos: List[List[str]] = [[] for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(ceil(photos_count / cls.MAX_PHOTO_ON_PAGE))

    def add_photo(self, label: str) -> str:
        for page in range(self.pages):
            if len(self.photos[page]) < self.MAX_PHOTO_ON_PAGE:
                slot = len(self.photos[page]) + 1
                self.photos[page].append(label)

                return f"{label} photo added successfully on page {page + 1} slot {slot}"

        return "No more free slots"

    def display(self) -> str:
        result = [self.DASH_COUNTER * self.SYMBOL]

        for page in self.photos:
            result.append(("[] " * len(page)).rstrip())
            result.append(self.DASH_COUNTER * self.SYMBOL)

        return "\n".join(result)


album = PhotoAlbum(1)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
