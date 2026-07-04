# Catatan Belajar: Sistem Rekening Bank (Inheritance & Encapsulation)
> Ditulis setelah ngerjain project Rekening Bank — drill inheritance, composition, polymorphism

---

## 1. "Has-A" vs "Is-A" — Dua Jenis Hubungan Antar Class

Sebelum bikin class, harus jelas dulu hubungan antar entitasnya:

- **"Is-A" → Inheritance**: `Britama` ADALAH `Rekening` → `class Britama(Rekening)`
- **"Has-A" → Composition**: `Nasabah` PUNYA `Rekening` → disimpan sebagai attribute (list of objects)

```python
class Rekening:
    def __init__(self, nomor_rekening):
        self.nomor_rekening = nomor_rekening

class Nasabah:
    def __init__(self, nama):
        self.nama = nama
        self.daftar_rekening = []   # "has-a" — composition
```

Cara mudah membedakan: tanya **"Apakah X ADALAH jenis dari Y?"** Kalau ya → inheritance. Kalau "X PUNYA Y" → composition.

---

## 2. `super()` — Bukan Cuma untuk `__init__`

`super()` dipakai untuk **memanggil method milik parent class** dari dalam child class. Dua kegunaan utama:

**A. Di `__init__`** — supaya attribute parent ikut ter-setup tanpa nulis ulang
```python
class Britama(Rekening):
    def __init__(self, nomor_rekening):
        super().__init__(nomor_rekening)   # jalankan __init__ parent dulu
        self.limit_harian = 20_000_000     # baru tambahan khusus child
```

**B. Di method lain** — untuk "pinjam" logic parent, lalu tambahkan logic baru
```python
class Britama(Rekening):
    def logic_kurangi_saldo(self, input_nominal):
        if input_nominal > self.limit_harian:   # validasi TAMBAHAN khusus child
            print("Melebihi limit harian")
            return False
        return super().logic_kurangi_saldo(input_nominal)   # lalu panggil versi asli parent
```

**Kapan WAJIB pakai `super().__init__()`?**
Kalau child mendefinisikan `__init__` sendiri DAN butuh attribute yang sudah di-setup parent. Kalau tidak dipanggil, attribute parent (`nomor_rekening`, `__saldo`, `riwayat`) tidak akan pernah ter-set — akan error saat diakses.

**Kapan TIDAK perlu `__init__` sama sekali di child?**
Kalau child tidak butuh attribute tambahan apapun — otomatis pakai `__init__` milik parent.

---

## 3. Polymorphism — Konsep yang Sering Disalahpahami

Polymorphism BUKAN soal `self.attribute` vs variable lokal. Polymorphism adalah:

> **Method dengan nama yang SAMA, dipanggil pada object yang BERBEDA, menghasilkan perilaku yang BERBEDA.**

```python
budi = Britama(123)
ani = Simpedes(456)

budi.tarik()   # cek limit 20 juta
ani.tarik()    # cek limit 5 juta
```

Method `tarik()` namanya sama, tapi perilakunya beda — itu polymorphism. Ini terjadi otomatis karena Python selalu mencari method **di class milik object itu sendiri dulu**, baru naik ke parent kalau tidak ketemu.

---

## 4. Override Method yang Tepat — Override yang Spesifik, Bukan yang Umum

Insight penting dari project ini: jangan override method yang **terlalu besar/umum** (seperti `tarik()` yang berisi loop, input, try/except). Sebaliknya, override method yang **lebih kecil dan spesifik** yang dipanggil di dalamnya.

```python
# tarik() di parent TIDAK PERLU disentuh sama sekali!
def tarik(self):
    while True:
        try:
            input_nominal = int(input("...").strip())
            ...
            berhasil = self.logic_kurangi_saldo(input_nominal)   # ⬅ ini yang di-override
            ...

# Child cukup override logic_kurangi_saldo() saja
class Britama(Rekening):
    def logic_kurangi_saldo(self, input_nominal):
        if input_nominal > self.limit_harian:
            return False
        return super().logic_kurangi_saldo(input_nominal)
```

Karena `tarik()` memanggil `self.logic_kurangi_saldo()` — bukan `Rekening.logic_kurangi_saldo()` — Python otomatis akan menjalankan versi child kalau objectnya adalah child. Ini menghindari duplikasi loop/input/try-except di setiap child class.

**Prinsipnya**: pecah method jadi bagian "alur" (loop, input, error handling) dan bagian "logic" (decision, validasi, perubahan data) — supaya bagian "logic" saja yang perlu di-override.

---

## 5. Encapsulation: Akses dari Dalam vs Luar Class

`__saldo` (private) tidak berarti harus selalu diakses lewat `@property` — itu cuma berlaku untuk akses dari **luar class**.

```python
# DARI DALAM class — boleh langsung akses private attribute
self.__saldo += input_nominal     # ✅ aman, kita yang kontrol logicnya
self.__saldo -= input_nominal     # ✅ aman

# DARI LUAR class — wajib lewat property/setter
rekening.saldo = 500000           # ✅ lewat setter, ada validasi
rekening.__saldo = 500000         # ❌ bypass — bikin attribute baru, tidak mengubah yang asli
```

Setter dirancang untuk melindungi dari akses **eksternal** yang tidak terkontrol — bukan dari kode di dalam class itu sendiri.

---

## 6. `self.saldo -= x` vs `self.__saldo -= x` — Beda yang Krusial

```python
self.saldo -= input_nominal     # ⚠️ ini LEWAT setter!
self.__saldo -= input_nominal   # ✅ ini langsung ke private attribute
```

`self.saldo -= x` setara dengan `self.saldo = self.saldo - x` — yang berarti **lewat setter**. Kalau hasilnya melanggar validasi setter (misal jadi negatif), setter akan **menolak diam-diam** tanpa error — saldo tidak berubah tapi kode tetap jalan seolah berhasil. Ini bug yang halus dan mudah terlewat.

Untuk operasi internal di dalam class, gunakan `self.__saldo` langsung agar predictable.

---

## 7. DRY: Memisahkan Bagian yang Berulang

Logic konfirmasi `y/n` muncul di banyak tempat (setor, tarik, transfer). Solusinya: ekstrak jadi 1 method privat yang dipakai ulang.

```python
def _konfirmasi(self, input_nominal):
    while True:
        jawaban = input(f"Nominal {input_nominal}, benar? y/n: ").strip().lower()
        if jawaban == "y":
            return True
        elif jawaban == "n":
            return False
        else:
            print("Pastikan ketik y/n")
            continue
```

Lalu dipakai di method lain:
```python
def logic_kurangi_saldo(self, input_nominal):
    if self._konfirmasi(input_nominal):
        ...
```

**Catatan**: DRY adalah prinsip, bukan hukum mutlak. Duplikasi kecil kadang lebih baik daripada abstraksi berlebihan yang justru bikin kode susah dibaca (*premature abstraction*).

---

## 8. `return` vs `break` vs `continue` — Scope yang Berbeda

- **`continue`** → mengulang loop **tempat dia berada saja**
- **`break`** → keluar dari loop, tapi masih di dalam function/method
- **`return`** → keluar dari **seluruh method**, sekaligus keluar dari loop manapun di dalamnya

```python
def _konfirmasi(self, input_nominal):
    while True:
        jawaban = input("...").strip().lower()
        if jawaban == "y":
            return True    # keluar dari while DAN dari method
        elif jawaban == "n":
            return False   # sama
        else:
            continue        # hanya ulang while, masih di dalam method
```

**Best practice**: kalau method dirancang untuk return boolean, selalu `return True`/`return False` secara eksplisit — jangan andalkan `break` yang menghasilkan `None` secara implisit (meskipun `None` dan `False` sama-sama falsy, ini tidak jelas/eksplisit).

---

## 9. Early Return Pattern

```python
# Kurang disukai — nesting lebih dalam
def kurangi_saldo(self, nominal):
    if konfirmasi:
        ...
        return True
    else:
        return False

# Early return — lebih flat dan bersih ✅
def kurangi_saldo(self, nominal):
    if konfirmasi:
        ...
        return True
    return False
```

Di industri, early return dianjurkan karena mengurangi nesting dan membuat alur logic lebih mudah diikuti.

---

## 10. Type Hints — Bukan Cuma untuk Tipe Dasar

Type hint bisa dipakai untuk custom class juga, termasuk class yang sedang didefinisikan sendiri (pakai string untuk forward reference):

```python
def transfer(self, rekening_tujuan: 'Rekening') -> None:
    ...
```

Kenapa pakai string `'Rekening'`? Karena saat baris itu dibaca Python, class `Rekening` belum selesai didefinisikan sepenuhnya — pakai string menghindari error referensi.

**Type hint tidak mempengaruhi runtime** — murni informasi untuk IDE dan developer lain. Python tidak akan menolak data dengan tipe yang salah hanya karena ada type hint.

---

## 11. Mutable Default Argument — Jebakan Klasik Python

```python
# ⚠️ BERBAHAYA
def __init__(self, keranjang_default={}):
    self.keranjang = keranjang_default
```

Default value `{}` hanya dibuat **SEKALI** saat function didefinisikan — bukan setiap kali dipanggil. Karena dict bersifat mutable, semua object yang tidak diberi argumen akan **berbagi dict yang sama** secara diam-diam.

**Solusi:**
```python
def __init__(self, keranjang_default=None):
    self.keranjang = keranjang_default if keranjang_default is not None else {}
```

---

## 12. Mutable vs Immutable — Dampak ke Parameter Function/Method

- **Mutable** (dict, list) → perubahan pada isi struktur data, walau lewat parameter, akan **terasa di luar** karena keduanya menunjuk ke "alamat memory" yang sama
- **Immutable** (int, str, tuple) → mengganti nilai = membuat binding baru, **tidak memengaruhi** variable di luar

Yang menentukan aman/tidaknya bukan tipe data isinya (int/str/dll), tapi **apakah operasi yang dilakukan memodifikasi struktur data mutable yang dipinjam** (seperti `dict[key] = value`) atau hanya membuat variable baru yang independen.

**Solusi untuk menghindari "kebocoran" data tidak sengaja**: `copy.deepcopy()` untuk membuat salinan independen sepenuhnya (beda dengan `copy.copy()` yang shallow — hanya menyalin lapisan terluar).

---

## 13. Name Mangling — `__saldo` Tidak 100% Private

```python
class Rekening:
    def __init__(self):
        self.__saldo = 100   # Python ubah jadi _Rekening__saldo di balik layar
```

- `rekening.__saldo = -9999` dari luar → membuat attribute **baru** yang terpisah, tidak menyentuh `self.__saldo` asli
- `rekening._Rekening__saldo = -9999` dari luar → **benar-benar mengubah** data asli, bypass validasi setter

Python menganut filosofi **"we are all consenting adults"** — `__` hanya mempersulit akses, bukan mencegah sepenuhnya. Beda dengan `private` di Java yang benar-benar tidak bisa ditembus.

---

## 14. `@property` dan `@setter` — Pintu Resmi untuk Akses Data Private

```python
class Rekening:
    def __init__(self):
        self.__saldo = 100

    @property
    def saldo(self):              # method bisa dipanggil seperti attribute (tanpa ())
        return self.__saldo

    @saldo.setter
    def saldo(self, nilai):
        if nilai < 0:
            print("Saldo tidak boleh negatif")
            return
        self.__saldo = nilai
```

Tanpa setter, validasi yang ditulis di method biasa (`set_saldo()`) masih bisa di-bypass karena attribute publik tetap bisa diubah langsung. Dengan `@property` + private attribute, **satu-satunya jalan resmi** untuk mengubah data adalah lewat setter — itu esensi encapsulation yang sesungguhnya.

---

## 15. Separation of Concerns: Input vs Logic

Ada trade-off antara:
- **Input di dalam method** → simpel, self-contained, tapi susah di-test dan di-reuse
- **Input di luar method (main program)**, method hanya proses data → lebih mudah di-test, tapi struktur program lebih kompleks

Untuk program CLI sederhana, input di dalam method masih bisa diterima. Tapi ini jadi masalah nyata ketika butuh **override sebagian logic** (seperti cek limit harian) — karena child class butuh tau nominal SEBELUM logic pengurangan saldo dieksekusi, padahal nominal baru didapat di dalam method itu sendiri.

**Solusi yang dipakai**: pecah method jadi 2 — bagian yang urus input/alur (`tarik()`) dan bagian yang urus logic murni dengan parameter eksplisit (`logic_kurangi_saldo(nominal)`). Bagian logic inilah yang di-override oleh child, bagian alur tidak perlu disentuh sama sekali.

---

*Catatan ini dibuat setelah menyelesaikan project Rekening Bank dengan Nasabah, Rekening (parent), Britama & Simpedes (child).*
*Next: lanjut eksplorasi project OOP lainnya atau perdalam konsep lain* 🚀
