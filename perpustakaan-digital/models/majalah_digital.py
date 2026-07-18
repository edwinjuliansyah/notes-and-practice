from models.media import Media
from datetime import datetime 

class MajalahDigital(Media):
    def __init__(self, judul: str, id_media: str, genre: set[str], pengarang: str, edisi: str, tanggal_terbit: datetime, tanggal_expired: datetime) -> None:
        super().__init__(judul, id_media, genre, pengarang)
        self.edisi = edisi
        self.tanggal_terbit = tanggal_terbit
        self.tanggal_expired = tanggal_expired

    def __str__(self) -> str:
        return f"Majalah digital\nJudul: {self.judul}\nEdisi: {self.edisi}\nTanggal Terbit: {self.tanggal_terbit.strftime('%d-%B-%Y')}"

    def cek_ketersediaan(self) -> bool:
        return self.tanggal_terbit <= datetime.now() < self.tanggal_expired

    def pinjam(self, id_member: str) -> bool:
        return self.cek_ketersediaan()

    def kembalikan(self, id_member: str) -> bool:
        return self.cek_ketersediaan()        
        