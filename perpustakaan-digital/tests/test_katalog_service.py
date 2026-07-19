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