from media import Media
from datetime import datetime 

class MajalahDigital(Media):
    def __init__(self, judul, id_media, genre, pengarang, edisi, tanggal_terbit, tanggal_expired):
        super().__init__(judul, id_media, genre, pengarang)
        self.edisi = edisi
        self.tanggal_terbit = tanggal_terbit
        self.tanggal_expired = tanggal_expired

    def __str__(self):
        return f"Majalah digital\nJudul: {self.judul}\nEdisi: {self.edisi}\nTanggal Terbit: {self.tanggal_terbit.strftime('%d-%B-%Y')}"

    def cek_ketersediaan(self):
        return self.tanggal_terbit <= datetime.now() < self.tanggal_expired

    def pinjam(self, id_member):
        return self.cek_ketersediaan()

    def kembalikan(self, id_member):
        return self.cek_ketersediaan()        
        