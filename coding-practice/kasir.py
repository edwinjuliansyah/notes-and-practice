from datetime import datetime
warkop = f"{' SELAMAT DATANG DI WARKOP EMUN ':=^50}"
total_belanja = 0
keranjang = {}

def garis():
  print("=" * len(warkop))

def tampilkan_keranjang(massage):
  print(massage)
  for key, value in keranjang.items():
    harga_format = f"Rp{value['harga']:,}".replace(",", ".")
    subtotal_format = f"Rp{value['subtotal']:,}".replace(",", ".")
    print(f"- {value['jumlah']:<5} {value['nama']:<10} x {harga_format:<15} = {subtotal_format:>10}")
  print(f"{'Total Belanja:':<30} {f'Rp{total_belanja:,}'.replace(',', '.'):>15}")

def buat_nota(uang_bayar, uang_kembalian):
  nota = ""
  laporan = f" Nota Pembelian {nama_pembeli} "
  nota += f"{laporan:=^{len(warkop)}}\n"
  tanggal_waktu_sekarang = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  nota += f"Tanggal Pembelian: {tanggal_waktu_sekarang}\n\n"

  for key, value in keranjang.items():
    harga_format = f"Rp{value['harga']:,}".replace(",", ".")
    subtotal_format = f"Rp{value['subtotal']:,}".replace(",", ".")
    nota += f"- {value['jumlah']:<5} {value['nama']:<10} x {harga_format} = {subtotal_format:>10}\n"
  
  nota += "=" * len(warkop) + "\n"
  total_format = f"Rp{total_belanja:,}".replace(",", ".")
  nota += f"{'Total Belanja':<15}: {total_format:>30}\n"
  uang_bayar = f"Rp{uang_bayar:,}".replace(",", ".")
  uang_kembalian = f"Rp{uang_kembalian:,}".replace(",", ".")
  nota += f"{'Uang Bayar':<15}: {uang_bayar:>30}\n"
  nota += f"{'Uang Kembalian':<15}: {uang_kembalian:>30}"
  return nota

print(warkop)
menu = {
    1: {"nama": "Roti", "harga": 2000},
    2: {"nama": "Susu", "harga": 3000},
    3: {"nama": "Kopi", "harga": 3000},
    4: {"nama": "Gorengan", "harga": 2000},
    5: {"nama": "Indomie", "harga": 6000}
}

for item in menu:
    nama_menu = menu[item]['nama']
    harga_menu = f"Rp{menu[item]['harga']:,}".replace(",", ".")
    print(f"{item}. {nama_menu:<10} {'|':^25} {harga_menu:>10}")
garis()

nama_pembeli = input("Masukkan nama anda: ").strip()

while True:
  try:
    pesanan = int(input("Pilih menu (1-5): ").strip())
    if pesanan in menu:
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
  
  nama = menu[pesanan]["nama"]
  harga = menu[pesanan]["harga"]
  subtotal = harga * quantity

  if pesanan in keranjang:
    keranjang[pesanan]["jumlah"] += quantity
    keranjang[pesanan]["subtotal"] += subtotal
  else:
    keranjang[pesanan] = {
        "nama": nama,
        "harga": harga,
        "jumlah": quantity,
        "subtotal": subtotal
    }
  total_belanja += subtotal
  
  garis()
  tampilkan_keranjang("Isi keranjang saat ini:")
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
    uang_bayar = int(input("Masukkan uang pembayaran: "))
    if uang_bayar < total_belanja:
      print("Uang tidak cukup, silakan masukkan jumlah yang sesuai")
      continue
    else:
      break
  except ValueError:
    print("Input tidak valid, pastikan input berupa angka")
    continue

uang_kembalian = uang_bayar - total_belanja

final = buat_nota(uang_bayar, uang_kembalian)
print(final)
garis()

baris1 = f'Terima kasih {nama_pembeli}'
baris2 = 'Sudah berkunjung di Warkop Emun!'
print(f"{baris1:^{len(warkop)}}")
print(f"{baris2:^{len(warkop)}}\n")

with open("laporan_nota.txt", "a") as file:
  baris_akhir = ' Transaksi selesai '
  end = f"{final}\n{baris_akhir:=^{len(warkop)}}\n\n\n\n"
  file.write(end)
