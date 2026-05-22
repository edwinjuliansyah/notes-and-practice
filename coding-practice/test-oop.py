class Produk:
    def __init__(self, nama_makanan, harga_makanan):
        self.nama = nama_makanan         
        self.harga = harga_makanan       

    def tampilkan_info(self):
        return f"Menu: {self.nama} | Harga: Rp{self.harga}"

    def hitung_subtotal(self, jumlah):
        return self.harga * jumlah


menu1 = Produk("Roti", 2000)
menu2 = Produk("Kopi", 3000)

print(menu1.tampilkan_info()) 
print(menu2.tampilkan_info())

subtotal_roti = menu1.hitung_subtotal(5)
subtotal_kopi = menu2.hitung_subtotal(3)

print(f"Beli 5 Roti, subtotal: Rp{subtotal_roti}")
print(f"Beli 3 Kopi, subtotal: Rp{subtotal_kopi}")
