from abc import ABC, abstractmethod

class Media(ABC):
    def __init__(self, judul, id_media, genre, penulis):
        self.judul = judul
        self.id_media = id_media
        self.genre = set(genre)
        self.penulis = penulis

    def __str__(self):
        return f"Judul: {self.judul}\nPenulis: {self.penulis}\nGendre: {self.genre}"
    
    def tambah_genre(self, genre_baru):
        self.genre.add(genre_baru)

    @abstractmethod
    def pinjam(self, id_member):
        pass

    @abstractmethod
    def kembalikan(self, id_member):
        pass

    @abstractmethod
    def cek_ketersediaan(self):
        pass