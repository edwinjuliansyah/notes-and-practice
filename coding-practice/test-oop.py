class Produk:
    def __init__(self, nama_makanan, harga_makanan):
        self.nama = nama_makanan         
        self.harga = harga_makanan       

    def tampilkan_info(self):
        return f"Menu: {self.nama} | Harga: Rp{self.harga}"

menu1 = Produk("Roti", 2000)
menu2 = Produk("Kopi", 3000)

print(menu1.tampilkan_info()) 
print(menu2.tampilkan_info())
