class Member:
    def __init__(self, id_member, nama):
        self.id_member = id_member
        self.nama = nama
        self.daftar_pinjaman = set()

    def __str__(self):
        return f"Nama: {self.nama}\nID: {self.id_member}\nDaftar Pinjaman: {self.daftar_pinjaman}"
    
    def tambah_pinjaman(self, id_media):
        if id_media in self.daftar_pinjaman:
            return False
        else:
            self.daftar_pinjaman.add(id_media)
            return True
        
    def hapus_pinjaman(self, id_media):
        if id_media in self.daftar_pinjaman:
            self.daftar_pinjaman.remove(id_media)
            return True
        else:
            return False