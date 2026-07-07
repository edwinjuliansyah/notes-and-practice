jasa = "=== SELAMAT DATANG DI EMUN EXPRESS ==="

def garis():
  print("=" * len(jasa))

print(jasa)
harga = {
  "PER_KG": 2000,
  "PER_KM": 3000
}

surcharge = {
    "BERAT>15KG": 5000,
    "JARAK>50KM": 10000
}

print("Tarif pengiriman")
for item in harga:
  print(f"{item} = Rp{harga[item]}")
garis()

print("Tarif tambahan")
for item in surcharge:
  print(f"{item} = Rp{surcharge[item]}")
garis()

while True:
  try:
    inp1 = float(input("Masukan berat barang: "))
    inp2 = float(input("Masukan jarak pengiriman: "))
    if inp1 <= 0 or inp2 <= 0:
      print("Berat dan jarak harus lebih besar dari nol! (berikan titik jika desimal)")
      continue
    break
  except ValueError:
    print("Input tidak valid, pastikan input berupa angka (berikan titik jika desimal)")

biaya_berat = inp1 * harga["PER_KG"]
biaya_jarak = inp2 * harga["PER_KM"]
total_biaya = biaya_berat + biaya_jarak

if inp1 > 15:
  total_biaya += surcharge["BERAT>15KG"]

if inp2 > 50:
  total_biaya += surcharge["JARAK>50KM"]

garis()
print(f"Total biaya Rp{total_biaya}")
