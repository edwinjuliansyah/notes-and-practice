from services.kategori_service import KategoriService

def test_hasil_fungsi_pencarian_kategori_jika_ketemu():
    kategori = KategoriService()
    tambah_kategori = kategori.tambah_kategori("fiksi")

    cari = kategori.pencarian_kategori("fiksi")

    assert tambah_kategori == True
    assert cari == True

def test_hasil_fungsi_pencarian_kategori_jika_tidak_ketemu():
    kategori = KategoriService()

    cari = kategori.pencarian_kategori("fiksi")

    assert cari == False