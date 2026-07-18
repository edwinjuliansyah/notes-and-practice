from services.katalog_service import KatalogService
from models.ebook_lisensi_bebas import EbookLisensiBebas

def test_tambah_media_berhasil():
    katalog = KatalogService()
    buku = EbookLisensiBebas("Laskar Pelangi", "B001", {"Fiksi"}, "Andrea Hirata")

    hasil = katalog.tambah_media(buku)

    assert hasil == True
    assert katalog.cari_by_id("B001") == buku