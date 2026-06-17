# Catatan Belajar: Refactoring Kasir ke OOP
---

## 1. OOP Bukan Selalu Lebih Baik

Hal pertama yang saya pelajari justru adalah OOP tidak selalu lebih baik dari kode prosedural. Untuk program kecil seperti kasir sederhana ini, OOP membuat kode terlihat lebih panjang dan "ribet". OOP baru worth it ketika:

- Kode berkembang besar dan dikerjakan banyak orang
- Ada banyak object dari tipe yang sama
- Logic-nya kompleks dan perlu diorganisir ketat
- Butuh reusability class yang sama dipakai di banyak tempat

Prinsipnya: **"Use the right tool for the right job"**

---

## 2. Cara Berpikir OOP: Design Dulu, Coding Belakangan

Sebelum nulis kode, saya harus **design dulu** ini yang paling penting agar dapat coding dengan baik dan terstruktur.

Caranya:
1. Identifikasi semua "benda" (noun) yang ada di problem ini calon class
2. Untuk tiap benda tanya: **"Benda ini tau apa?"** → attribute, **"Benda ini bisa ngapain?"** → method
3. Cek apakah ada hubungan hierarki antar class (inheritance) atau tidak

Di project kasir ini, saya awalnya salah design — terlalu banyak class dan hierarkinya tidak masuk akal. Setelah dipikir ulang, cukup **2 class**:
- `Menu` — menyimpan daftar produk
- `Transaksi` — menyimpan semua data satu sesi pembelian

---

## 3. "Is-A" Test untuk Inheritance

Inheritance itu berarti "A adalah B". Sebelum bikin parent-child, selalu tanya:

> *"Apakah X adalah Y?"*

- `Anjing` adalah `Hewan` ✅ → inheritance masuk akal
- `Kasir` adalah `Menu` ❌ → tidak ada hubungannya

Jangan paksa inheritance kalau memang tidak ada hubungan hierarki yang natural.

---

## 4. Single Responsibility Principle

Setiap class/function harusnya punya **satu tanggung jawab saja**. Kalau sebuah function melakukan terlalu banyak hal, itu tanda dia perlu dipecah.

Contoh: `tampilkan_keranjang()` tugasnya hanya menampilkan — bukan sekaligus menghitung total atau menyimpan data.

---

## 5. Attribute vs Variable Lokal

Ini yang bikin saya bingung paling lama. Aturannya:

- **`self.attribute`** → data yang perlu **diingat** oleh object dan dipakai di method lain
- **Variable lokal** → data yang hanya dibutuhkan **sesaat** dalam satu method

Contoh:
```python
def tambah_pesanan(self, pesanan, quantity, menu_item):
    harga = menu_item[pesanan]["harga"]  # lokal, cukup — hanya dipakai di sini
    subtotal = harga * quantity           # lokal, cukup
    self.total_belanja += subtotal        # self — perlu diingat untuk nota nanti
```

---

## 6. Semua Attribute Harus Ada di `__init__`

Ini tentang **predictable state** — siapapun yang pakai class kita, langsung tau attribute apa saja yang dimiliki object sejak pertama dibuat.

Berbahaya kalau attribute baru "lahir" di tengah method:
```python
# ⚠️ Berbahaya — nama_pembeli belum exist kalau inp_nama_pembeli() belum dipanggil
def buat_nota(self):
    print(self.nama_pembeli)  # AttributeError kalau dipanggil duluan!
```

Yang benar — semua attribute didefinisikan di `__init__` meskipun nilainya kosong dulu:
```python
def __init__(self):
    self.nama_pembeli = ""   # kosong dulu, diisi nanti
    self.uang_kembalian = 0  # kosong dulu, diisi nanti
```

---

## 7. Jangan Akses Variable Global dari Dalam Method

Kalau method butuh data dari luar object, data itu harus **masuk lewat parameter** secara eksplisit — bukan diambil diam-diam dari variable global.

```python
# ⚠️ Salah — bergantung pada variable global
def tambah_pesanan(self):
    nama = menu.item[pesanan]["nama"]  # menu dan pesanan dari mana?

# ✅ Benar — semua data dari luar masuk lewat parameter
def tambah_pesanan(self, pesanan, quantity, menu_item):
    nama = menu_item[pesanan]["nama"]
```

Prinsipnya: **"Explicit is better than implicit"** — salah satu filosofi inti Python.

---

## 8. Parameter vs `self` — Kapan Pakai Yang Mana?

- **`self`** → kalau data yang dibutuhkan sudah tersimpan di dalam object
- **Parameter** → kalau data datang dari luar object

Tanya ke diri sendiri: *"Apakah data ini sudah ada di `self`?"*
- Ya → pakai `self`, tidak perlu parameter
- Tidak → butuh parameter

---

## 9. Mutable vs Immutable — Data Dari Luar Bisa Berubah

Ketika kita pass data ke parameter, kita tidak membuat salinan baru — kita meminjam **referensi** ke data aslinya.

- **Mutable** (dict, list) → perubahan di luar **terasa di dalam** method
- **Immutable** (int, string) → perubahan di luar **tidak terasa** di dalam method

Untuk kasus kasir ini, ini justru yang kita inginkan — kalau harga di `menu.item` diupdate, `tambah_pesanan` otomatis pakai harga terbaru.

---

## 10. Global State itu Berbahaya

Di kode prosedural lama, `keranjang = {}` dan `total_belanja = 0` adalah global state — bisa diakses dan diubah dari mana saja. Ini berbahaya karena:

- Kalau ada bug, susah dilacak datangnya dari mana
- Kalau program melayani banyak customer, data bisa saling menimpa

Solusi OOP: pindahkan ke `self` agar data terisolasi per object.

---

## 11. OOP dan Prosedural Bukan Musuh

OOP tidak berarti nol kode prosedural. Yang berubah adalah *dimana* kode prosedural itu tinggal:

- **Sebelum OOP**: logic berserakan di mana-mana
- **Setelah OOP**: logic yang berkaitan dengan data → masuk method class. Logic yang mengatur alur program → tetap prosedural, tapi terpusat di `main program`

`while True`, `input()`, dan alur program tetap ada — mereka tinggal di main program, bukan di dalam class.

---

## 12. YAGNI — You Aren't Gonna Need It

Jangan bikin class kalau tidak benar-benar dibutuhkan. Awalnya saya bikin class `Kasir`, tapi setelah dipikir ulang — attributenya kosong dan method-nya hanya jadi perantara class lain. Itu tanda class tersebut tidak diperlukan untuk scope program ini.

Buat sesuatu hanya kalau memang dibutuhkan sekarang.

---

## 13. Naming dan Typo Itu Penting

Konsistensi penamaan sangat penting. Satu typo kecil seperti `tampikan_menu` (harusnya `tampilkan_menu`) bisa bikin bingung orang lain yang baca kode kita — atau bahkan diri sendiri 3 bulan kemudian.

---

## 14. Input Sanitization

Validasi input itu penting untuk mencegah data yang tidak valid masuk ke sistem. Yang saya pelajari:

- Selalu `.strip()` input sebelum diproses — hapus spasi yang tidak sengaja
- `.strip()` harus dipanggil **sebelum** konversi tipe: `int(input().strip())` bukan `int(input()).strip()`
- Untuk validasi string: gunakan `.isalpha()`, `.isdigit()`, `.isalnum()`
- Untuk nama dengan spasi: `.replace(" ", "").isalpha()` — hapus spasi dulu, baru cek

Pattern validasi yang bersih ("early continue"):
```python
if not kondisi_valid:
    print("pesan error")
    continue
break  # lolos semua validasi, keluar loop
```

---

## 15. OOP Baru Worth It Saat Sistem Berkembang

Meskipun untuk program sederhana OOP terasa overkill, manfaatnya baru terasa ketika sistem berkembang. Dengan OOP:

- Mau tambah fitur baru? Tambah method di class yang relevan
- Ada bug? Lebih mudah dilacak karena data terisolasi per class
- Mau dipakai ulang? Tinggal import class-nya

Ini yang namanya **maintainable code** — kode yang mudah dirawat dan dikembangkan.

