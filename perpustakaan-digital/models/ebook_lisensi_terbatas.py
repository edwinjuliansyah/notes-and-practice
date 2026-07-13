from media import Media

class EbookLisensiTerbatas(Media):
    def __init__(self, judul, id_media, genre, penulis):
        super.__init__(judul, id_media, genre, penulis)
        self.kuota_lisensi = 3
        self.daftar_peminjam = set()

    def pinjam(self, id_member):
        if id_member in self.daftar_peminjam:
            return False

        if len(self.daftar_peminjam) < self.kuota_lisensi:
            self.daftar_peminjam.add(id_member)
            return True
        else:
            return False

    def kembalikan(self, id_member):
        if id_member in self.daftar_peminjam:
            self.daftar_peminjam.remove(id_member)
            return True
        else:
            return False
        
    def cek_ketersediaan(self):
        return len(self.daftar_peminjam) < self.kuota_lisensi
        
