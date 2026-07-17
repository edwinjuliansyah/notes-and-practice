from abc import ABC, abstractmethod

class Media(ABC):
    def __init__(self, judul: str, id_media: str, genre: set[str], penulis: str) -> None:
        self.judul = judul
        self.id_media = id_media
        self.genre = set(genre)
        self.penulis = penulis

    def __str__(self) -> str:
        return f"Judul: {self.judul}\nPenulis: {self.penulis}\nGendre: {self.genre}"
    
    def tambah_genre(self, genre_baru: str) -> None:
        self.genre.add(genre_baru)

    @abstractmethod
    def pinjam(self, id_member: str) -> bool:
        pass

    @abstractmethod
    def kembalikan(self, id_member: str) -> bool:
        pass

    @abstractmethod
    def cek_ketersediaan(self) -> bool:
        pass