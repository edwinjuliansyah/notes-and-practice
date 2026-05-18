warkop = "=== SELAMAT DATANG DI WARKOP EMUN ==="
total_belanja = 0
keranjang = {}

def garis():
  print("=" * len(warkop))

def tampilkan_keranjang(massage):
  print(massage)
for key, value in keranjang.items():
    harga_format = f"Rp{value['harga']:,}".replace(",", ".")
    subtotal_format = f"Rp{value['subtotal']:,}".replace(",", ".")
    print(f"- {value['jumlah']} {value['nama']:<10} x {harga_format} = {subtotal_format:>8}")

def buat_nota():
  nota = ""
  laporan = f" Nota Pembelian {nama_pembeli} "
  nota += f"{laporan:=^{len(warkop)}}\n"
  for key, value in keranjang.items():
    harga_format = f"Rp{value['harga']:,}".replace(",", ".")
    subtotal_format = f"Rp{value['subtotal']:,}".replace(",", ".")
    nota += f"- {value['jumlah']} {value['nama']:<10} x {harga_format} = {subtotal_format}\n"
  nota += "=" * len(warkop) + "\n"
  total_format = f"Rp{total_belanja:,}".replace(",", ".")
  nota += f"Total Belanja: {total_format}"
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
    print(f"{item}. {menu[item]['nama']:<10} | Rp {menu[item]['harga']:>6}")
garis()

nama_pembeli = input("Masukkan nama anda: ").strip()

while True:
  try:
    pesanan = int(input("Pilih menu (1-5): ").strip())
    if pesanan in menu:
      quantity = int(input("Masukkan jumlah pesanan: ").strip())
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

print(buat_nota())
garis()
print(f"Terima kasih {nama_pembeli} telah memesan di Warkop Emun!\n")

with open("laporan_nota.txt", "a") as file:
    baris_akhir = ' Transaksi selesai '
    end = f"{buat_nota()}\n{baris_akhir:=^{len(warkop)}}\n\n\n\n"
    file.write(end)
