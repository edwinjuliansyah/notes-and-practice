# Operator Python
## 1. Operator Matematika (Aritmatika)
Operator ini digunakan untuk melakukan operasi hitung matematis pada angka.

| Simbol | Nama | Penjelasan | Contoh | Hasil |
| :---: | :--- | :--- | :--- | :--- |
| `+` | Penjumlahan | Menambahkan angka | `5 + 2` | `7` |
| `-` | Pengurangan | Mengurangi angka | `5 - 2` | `3` |
| `*` | Perkalian | Mengalikan angka | `5 * 2` | `10` |
| `/` | Pembagian | Membagi angka (hasilnya selalu float/desimal) | `5 / 2` | `2.5` |
| `//` | Floor Division | Pembagian dengan hasil pembulatan ke bawah | `5 // 2` | `2` |
| `%` | Modulo | Sisa hasil bagi | `5 % 2` | `1` |
| `**` | Eksponen | Pemangkatan | `5 ** 2` | `25` |

---

## 2. Operator Logika
Operator logika digunakan untuk menggabungkan pernyataan kondisional (boolean).

| Operator | Deskripsi | Logika |
| :--- | :--- | :--- |
| `and` | True jika **keduanya** benar | `(5 > 2) and (3 < 5)` → True |
| `or` | True jika **salah satu** benar | `(5 > 2) or (3 > 10)` → True |
| `not` | Membalikkan hasil (True jadi False) | `not(5 > 2)` → False |

---

## 3. Operator Perbandingan
Digunakan untuk membandingkan dua nilai. Hasilnya selalu berupa `True` atau `False`.

| Simbol | Nama | Contoh |
| :---: | :--- | :--- |
| `==` | Sama dengan | `5 == 5` (True) |
| `!=` | Tidak sama dengan | `5 != 3` (True) |
| `>` | Lebih besar dari | `5 > 3` (True) |
| `<` | Lebih kecil dari | `5 < 3` (False) |
| `>=` | Lebih besar atau sama dengan | `5 >= 5` (True) |
| `<=` | Lebih kecil atau sama dengan | `5 <= 4` (False) |

---

## 4. Operator Penugasan (Assignment)
Digunakan untuk memberikan nilai atau memperbarui nilai pada variabel secara efisien.

| Simbol | Contoh | Sama dengan |
| :---: | :--- | :--- |
| `=` | `x = 5` | `x = 5` |
| `+=` | `x += 3` | `x = x + 3` |
| `-=` | `x -= 2` | `x = x - 2` |
| `*=` | `x *= 2` | `x = x * 2` |

---

## Contoh Implementasi dalam Kode
```python
# Contoh penggunaan operator dalam satu script
stok = 10
pembelian = 3

# Matematika & Penugasan
stok -= pembelian

# Logika & Perbandingan
stok_aman = stok > 0
promo_aktif = False

if stok_aman and not promo_aktif:
    print(f"Pesanan diproses. Sisa stok: {stok}")
else:
    print("Pesanan tidak dapat diproses.")
#Output
#Pesanan diproses. Sisa stok: 7
```
