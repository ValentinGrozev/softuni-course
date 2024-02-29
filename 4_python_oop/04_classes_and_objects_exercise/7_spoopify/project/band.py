from typing import List
from project.album import Album


class Band:

    def __init__(self, name: str):
        self.name = name
        self.albums: List = []

    def add_album(self, album: Album) -> str:
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."

        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str) -> str:
        for current_album in self.albums:
            if current_album.name == album_name and current_album.published:
                return "Album has been published. It cannot be removed."
            elif current_album.name == album_name:
                self.albums.remove(current_album)
                return f"Album {current_album.name} has been removed."

        return f"Album {album_name} is not found."

    def details(self) -> str:
        result = f"Band {self.name}\n"

        for album in self.albums:
            result += f"{album.details()}\n"

        return result
    