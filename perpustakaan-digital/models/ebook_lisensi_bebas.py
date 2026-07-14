from media import Media

class EbookLisensiBebas(Media):
    def __init__(self, judul, id_media, genre, penulis):
        super().__init__(judul, id_media, genre, penulis)
        self.daftar_peminjam = set()

    def pinjam(self, id_member):
        if id_member in self.daftar_peminjam:
            return False
        else:
            self.daftar_peminjam.add(id_member)
            return True
        
    def kembalikan(self, id_member):
        if id_member in self.daftar_peminjam:
            self.daftar_peminjam.remove(id_member)
            return True
        else:
            return False
        
    def cek_ketersediaan(self):
        return True