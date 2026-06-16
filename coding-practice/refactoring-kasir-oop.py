from datetime import datetime
warkop = f"{' SELAMAT DATANG DI WARKOP EMUN ':=^50}"

def garis():
  print("=" * len(warkop))
  
def format_rupiah(nilai):
  return f"Rp{nilai:,}".replace(",", ".")

class Menu:
  def __init__(self):
    self.item = {}
    self.counter = 0
  
  def tambah_menu(self, nama, harga):
    self.counter += 1
    self.item[self.counter] = {"nama": nama, "harga": harga}

  def tampilkan_menu(self):
    for key, value in self.item.items():
      print(f"{key}. {value['nama']:<10} {'|':^25} {format_rupiah(value['harga']):>10}")

class Transaksi:
  def __init__(self):
    self.keranjang = {}
    self.total_belanja = 0
    self.nama_pembeli = ""
    self.uang_bayar = 0
    self.uang_kembalian = 0

  def inp_nama_pembeli(self):
    while True:
      self.nama_pembeli = input("Masukkan nama anda: ").strip()
      if not self.nama_pembeli:
        print("Nama tidak boleh kosong")
        continue

      if not self.nama_pembeli.replace(" ", "").isalpha():
        print("Nama harus berupa huruf")
        continue
      else:
        break  

  def hitung_kembalian(self):
    self.uang_kembalian = self.uang_bayar - self.total_belanja

  def tambah_pesanan(self, pesanan, quantity, menu_item):
    nama = menu_item[pesanan]["nama"]
    harga = menu_item[pesanan]["harga"]
    subtotal = harga * quantity
  
    if pesanan in self.keranjang:
      self.keranjang[pesanan]["jumlah"] += quantity
      self.keranjang[pesanan]["subtotal"] += subtotal
    else:
      self.keranjang[pesanan] = {
          "nama": nama,
          "harga": harga,
          "jumlah": quantity,
          "subtotal": subtotal
      }
    self.total_belanja += subtotal

  def tampilkan_keranjang(self):
    print("Isi keranjang saat ini:")
    for key, value in self.keranjang.items():
      harga_format = format_rupiah(value['harga'])
      subtotal_format = format_rupiah(value['subtotal'])
      print(f"- {value['jumlah']:<5} {value['nama']:<10} x {harga_format:<15} = {subtotal_format:>10}")
    print(f"{'Total Belanja:':<30} {format_rupiah(self.total_belanja):>15}")

  def buat_nota(self):
    nota = ""
    laporan = f" Nota Pembelian {self.nama_pembeli} "
    nota += f"{laporan:=^{len(warkop)}}\n"
    tanggal_waktu_sekarang = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    nota += f"Tanggal Pembelian: {tanggal_waktu_sekarang}\n\n"

    for key, value in self.keranjang.items():
      harga_format = format_rupiah(value['harga'])
      subtotal_format = format_rupiah(value['subtotal'])
      nota += f"- {value['jumlah']:<5} {value['nama']:<10} x {harga_format} = {subtotal_format:>10}\n"

    nota += "=" * len(warkop) + "\n"
    total_format = format_rupiah(self.total_belanja)
    nota += f"{'Total Belanja':<15}: {total_format:>30}\n"
    uang_bayar = format_rupiah(self.uang_bayar)
    uang_kembalian = format_rupiah(self.uang_kembalian)
    nota += f"{'Uang Bayar':<15}: {uang_bayar:>30}\n"
    nota += f"{'Uang Kembalian':<15}: {uang_kembalian:>30}"
    return nota

print(warkop)
menu = Menu()
menu.tambah_menu("Roti", 2000)
menu.tambah_menu("Susu", 3000)
menu.tambah_menu("Kopi", 3000)
menu.tambah_menu("Gorengan", 2000)
menu.tambah_menu("Indomie", 6000)
menu.tampilkan_menu()
garis()

transaksi = Transaksi()
transaksi.inp_nama_pembeli()

while True:
  try:
    pesanan = int(input("Pilih menu (1-5): ").strip())
    if pesanan in menu.item:
      quantity = int(input("Masukkan jumlah pesanan: ").strip())
      if quantity <= 0:
        print("Jumlah pesanan minimal 1")
        continue
    else:
      print("Menu tidak tersedia")
      continue
  except ValueError:
    print("Input tidak valid, pastikan input berupa angka")
    continue 
  
  transaksi.tambah_pesanan(pesanan, quantity, menu.item)
  
  garis()
  transaksi.tampilkan_keranjang()
  garis()

  while True:
    pesanan_tambahan = input("Apakah ada pesanan tambahan? (y/n): ").lower().strip()
    if pesanan_tambahan == "y":
      break
    elif pesanan_tambahan == "n":
      break
    else:
      print("Pastikan ketik y/n")
      continue
  if pesanan_tambahan == "n":
    break

while True:
  try:
    transaksi.uang_bayar = int(input("Masukkan uang pembayaran: ").strip())
    if transaksi.uang_bayar < transaksi.total_belanja:
      print("Uang tidak cukup, silakan masukkan jumlah yang sesuai")
      continue
    else:
      break
  except ValueError:
    print("Input tidak valid, pastikan input berupa angka")
    continue

transaksi.hitung_kembalian()

final = transaksi.buat_nota()
print(final)
garis()

baris1 = f'Terima kasih {transaksi.nama_pembeli}'
baris2 = 'Sudah berkunjung di Warkop Emun!'
print(f"{baris1:^{len(warkop)}}")
print(f"{baris2:^{len(warkop)}}\n")

with open("laporan_nota.txt", "a") as file:
  baris_akhir = ' Transaksi selesai '
  end = f"{final}\n{baris_akhir:=^{len(warkop)}}\n\n\n\n"
  file.write(end)
