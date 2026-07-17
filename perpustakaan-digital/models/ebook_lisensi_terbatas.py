from media import Media

class EbookLisensiTerbatas(Media):
    def __init__(self, judul: str, id_media: str, genre: str, penulis: str) -> None:
        super().__init__(judul, id_media, genre, penulis)
        self.kuota_lisensi: int = 3
        self.daftar_peminjam: set[str] = set()

    def __str__(self) -> str:
        info_dasar = super().__str__()
        return f"{info_dasar}\nKuota: {len(self.daftar_peminjam)}/{self.kuota_lisensi}"

    def pinjam(self, id_member: str) -> bool:
        if id_member in self.daftar_peminjam:
            return False

        if len(self.daftar_peminjam) < self.kuota_lisensi:
            self.daftar_peminjam.add(id_member)
            return True
        else:
            return False

    def kembalikan(self, id_member: str) -> bool:
        if id_member in self.daftar_peminjam:
            self.daftar_peminjam.remove(id_member)
            return True
        else:
            return False
        
    def cek_ketersediaan(self) -> bool:
        return len(self.daftar_peminjam) < self.kuota_lisensi
        
