from services.katalog_service import KatalogService
from models.ebook_lisensi_bebas import EbookLisensiBebas

def test_tambah_media_berhasil():
    katalog = KatalogService()
    buku = EbookLisensiBebas("Laskar Pelangi", "B001", {"Fiksi"}, "Andrea Hirata")

    hasil = katalog.tambah_media(buku)

    assert hasil == True
    assert katalog.cari_by_id("B001") == buku

def test_hapus_media_berhasil():
    katalog = KatalogService()
    buku = EbookLisensiBebas("Laskar Pelangi", "B001", {"Fiksi"}, "Andrea Hirata")

    tambah = katalog.tambah_media(buku)

    hapus = katalog.hapus_media(buku.id_media)

    assert tambah == True
    assert hapus == True
    assert katalog.cari_by_id("B001") == None


def test_hapus_media_gagal_jika_id_tidak_ada():
    katalog = KatalogService()
    buku = EbookLisensiBebas("Laskar Pelangi", "B001", {"Fiksi"}, "Andrea Hirata")
    tambah = katalog.tambah_media(buku)

    hasil = katalog.hapus_media("B009")
    
    assert hasil == False

def test_semua_media_mengembalikan_list_berisi_semua_media():
    # Arrange: siapin katalog + 2 media berbeda
    katalog = KatalogService()
    buku1 = EbookLisensiBebas("Laskar Pelangi", "B001", {"Fiksi"}, "Andrea Hirata")
    buku2 = EbookLisensiBebas("Bumi Manusia", "B002", {"Fiksi", "Sejarah"}, "Pramoedya")
    katalog.tambah_media(buku1)
    katalog.tambah_media(buku2)

    # Act
    hasil = katalog.semua_media()

    # Assert: harus list, isinya 2, dan kedua buku ada di dalamnya
    assert len(hasil) == 2
    assert buku1 in hasil
    assert buku2 in hasil


def test_semua_media_katalog_kosong():
    # Arrange: katalog baru, belum ada isi
    katalog = KatalogService()

    # Act
    hasil = katalog.semua_media()

    # Assert: harus list kosong, bukan None atau error
    assert hasil == []

