# Python Notes: LEGB Rule (Variable Scope)

Catatan mengenai aturan penentuan cakupan (scope) variabel di Python berdasarkan metode LEGB Rule dan konsep Order of Ascending Coverage.

---

## Apa itu LEGB Rule?

LEGB adalah urutan prioritas yang digunakan oleh Python saat mencari nilai dari sebuah variabel. Ketika suatu variabel dipanggil, Python akan mencarinya dari cakupan terdalam hingga cakupan terluar.

Urutan ini disebut Order of Ascending Coverage (Urutan cakupan yang semakin meluas):

Local -> Enclosing -> Global -> Built-in

Aturan Penting: Python hanya mencari variabel dengan arah keluar atau ke atas (dari lokal menuju built-in). Jika di keempat cakupan tersebut variabel tetap tidak ditemukan, Python akan melempar NameError.

---

## Pembagian 4 Scope di Python

### 1. Local Scope
Variabel yang didefinisikan di dalam sebuah fungsi. Variabel ini bersifat privat dan hanya hidup selama fungsi tersebut dieksekusi.

```python
def fungsi_ku():
    x = "Saya Lokal"  # Local Scope
    print(x)

fungsi_ku()
# print(x)  # ERROR: x tidak dikenal di luar fungsi
```

### 2. Enclosing Scope
Terjadi pada fungsi di dalam fungsi (nested function). Variabel ini terletak di fungsi luar (outer function), tetapi masih bisa dibaca oleh fungsi bagian dalam (inner function).

```python
def fungsi_luar():
    pesan = "Halo dari Enclosing"  # Enclosing Scope bagi fungsi_dalam
    
    def fungsi_dalam():
        print(pesan)  # Dapat membaca variabel dari fungsi luar
        
    fungsi_dalam()

fungsi_luar()
```

### 3. Global Scope
Variabel yang didefinisikan di bagian paling luar dari file script Python (tidak berada di dalam fungsi mana pun). Variabel ini bisa diakses dari mana saja di dalam file yang sama.

```python
url_api = "[https://api.whatsapp.com](https://api.whatsapp.com)"  # Global Scope

def kirim_notif():
    print(f"Menghubungkan ke {url_api}")  # Fungsi bisa langsung mengambil nilai global

kirim_notif()
```

### 4. Built-in Scope
Cakupan tingkat tertinggi yang berisi fungsi, keyword, dan tipe error bawaan dari bahasa Python itu sendiri. Selalu aktif otomatis tanpa perlu dibuat manual atau di-import.

```python
# Fungsi seperti print(), len(), str(), int() berada di Built-in Scope
list_data = [1, 2, 3]
print(len(list_data))  # 'print' dan 'len' adalah fungsi Built-in
```

---

## Analogi Sederhana (Mencari Barang)

* Local: Anda mencari gunting di dalam kamar sendiri.
* Enclosing: Gunting tidak ada, Anda keluar mencarinya di ruang tengah atau dapur bersama.
* Global: Masih tidak ada, Anda pergi mencari di warung depan rumah.
* Built-in: Jika kosong juga, Anda pergi ke supermarket pusat kota.
