type type_hint_recursive = dict[str, str | type_hint_recursive]
class KategoriService:
    def __init__(self) -> None:
        self.kategori: type_hint_recursive = {}

    def tambah_kategori(self, kategori_baru: str) -> bool:
        self.kategori[kategori_baru] = {}
        return True

    def pencarian_kategori(self, cari_kategori: str) -> bool:
        return cari_kategori in self.kategori 