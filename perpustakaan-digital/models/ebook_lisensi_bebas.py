from models.media import Media

class EbookLisensiBebas(Media):
    def __init__(self, judul: str, id_media: str, genre: set[str], penulis: str) -> None:
        super().__init__(judul, id_media, genre, penulis)
        self.daftar_peminjam: set[str] = set()

    def pinjam(self, id_member: str) -> bool:
        if id_member in self.daftar_peminjam:
            return False
        else:
            self.daftar_peminjam.add(id_member)
            return True
        
    def kembalikan(self, id_member: str) -> bool:
        if id_member in self.daftar_peminjam:
            self.daftar_peminjam.remove(id_member)
            return True
        else:
            return False
        
    def cek_ketersediaan(self) -> bool:
        return True