# Pemrograman Fungsional (FP) di Python

## 1. Apa itu Pemrograman Fungsional?
Paradigma atau gaya berpikir dalam pemrograman di mana kita membangun aplikasi dengan menyusun fungsi-fungsi murni (*pure functions*) dan menjaga prinsip **Immutability** (data asli tidak boleh diubah). Fokus utamanya adalah pada *apa yang ingin dihasilkan*, bukan mendikte langkah demi langkah *bagaimana komputer melakukannya*.

### Fungsi dan Peran Utama dalam Kode
1. **Menghindari Bug (Bebas Side Effects):** Data asli tidak akan berubah atau rusak di tengah jalan secara tidak sengaja oleh fungsi lain karena fungsinya terisolasi dengan baik.
2. **Mudah Diuji (Testable):** Fungsi bersifat mandiri. Jika diberi input "A", nilainya akan selalu "B", tidak peduli kondisi aplikasi di luar fungsi tersebut.
3. **Mendukung Kerja Paralel (Concurrency):** Sangat cocok untuk arsitektur modern karena setiap inti CPU (*multi-core*) bisa memproses data secara bersamaan tanpa perlu mengantre (*locking*) akibat berebutan variabel yang sama.

### Insight Penting: Trade-off RAM vs CPU
* **Mitos:** Banyak yang mengira pemrograman fungsional membuat penggunaan RAM menjadi lebih hemat.
* **Faktanya:** FP justru **lebih boros RAM** karena Python dipaksa membuat objek/salinan data baru di memori setiap kali sebuah fungsi memproses sesuatu (untuk menjaga data asli tetap utuh).
* **Kesimpulan:** Di industri modern, sengaja mengorbankan sedikit ruang RAM (karena harga RAM murah) demi memotong waktu tunggu CPU (yang sangat berharga). Hasilnya, proses eksekusi kode menjadi jauh lebih singkat, efisien secara waktu, dan yang paling penting: aplikasi stabil serta aman dari korupsi data.

### Contoh Kode Sederhana (Gaya Pythonic)
Dibanding menggunakan modifikasi di dalam *looping* biasa, gaya fungsional di Python memanfaatkan fitur seperti *List Comprehension* untuk menjaga keutuhan data asli:

```python
# Data asli yang tetap konstan/tidak berubah
angka = [1, 2, 3, 4, 5]

# Proses fungsional: menghasilkan objek baru langsung di memori berbeda
hasil_fungsional = [x * 2 for x in angka]

print(hasil_fungsional) # Output: [2, 4, 6, 8, 10]
print(angka)            # Output data asli tetap aman: [1, 2, 3, 4, 5]
```
---

## 2. Apa itu Pure Function?

**Pure Function** bukan sekadar "teknik" menulis kode atau "jenis" fungsi tertentu, melainkan sebuah **karakteristik wajib** dalam Pemrograman Fungsional. Sebuah fungsi baru sah disebut murni jika memenuhi dua syarat mutlak:

1. **Hasilnya Selalu Konsisten (Deterministic):** Jika kita memasukkan input (argumen) yang sama, fungsi tersebut harus selalu mengembalikan hasil yang sama, kapan pun dan berapa kali pun dijalankan.
2. **Tidak Memiliki Efek Samping (No Side Effects):** Fungsi tidak boleh mengubah status, data, atau variabel apa pun di luar dirinya. Ia tidak merusak data asli yang dimasukkan, tidak mengubah variabel global, bahkan tidak memicu fungsi I/O seperti menulis file atau menampilkan `print()` ke terminal (karena itu mengubah status layar).

---

### Peran dan Fungsinya dalam Aplikasi

* **Mudah Diuji (Testable):** Karena fungsinya terisolasi, kita tidak perlu repot melakukan *setup* database palsu atau memanipulasi variabel global saat melakukan *testing*. Cukup beri input, lalu cek outputnya.
* **Aman dari Bug Misterius:** Kita bisa yakin 100% bahwa memanggil fungsi ini di bagian mana pun tidak akan merusak data di bagian aplikasi yang lain secara tidak sengaja.
* **CPU Efisien (Dukungan Concurrency):** Karena sifatnya yang tidak mengubah data secara langsung (*immutability*), banyak core CPU bisa memproses fungsi ini secara bersamaan tanpa ada drama antrean data (*locking*).

---

### Contoh Kode: Kontras Impure vs Pure

#### Contoh Impure Function (Tidak Murni)
Fungsi di bawah ini tidak murni karena bergantung pada variabel luar dan merusak data asli:

```python
# Masalah 1: Bergantung pada variabel luar
faktor_kali = 2
def hitung_harga_impure(angka):
    return angka * faktor_kali  # Jika 'faktor_kali' berubah, hasilnya berubah

# Masalah 2: Merusak data asli yang dimasukkan (Side Effect)
def tambah_barang_impure(keranjang, barang_baru):
    keranjang.append(barang_baru)  # Mengubah list asli di luar fungsi
    return keranjang

```

#### Contoh Pure Function (Murni)
Fungsi di bawah ini murni karena semua kebutuhan diisolasi di dalam parameter dan menghasilkan data baru yang aman:

```python
# Berdiri sendiri, konsisten, dan terisolasi
def hitung_harga_pure(angka, faktor):
    return angka * faktor

# Menggunakan konsep Immutability (tidak merusak data asli)
def tambah_barang_pure(keranjang, barang_baru):
    # Kita gabungkan list lama dengan list baru untuk menciptakan objek baru di RAM
    return keranjang + [barang_baru]

# --- UJI COBA ---
keranjang_asli = ["Laptop", "Mouse"]
keranjang_baru = tambah_barang_pure(keranjang_asli, "Keyboard")

print("Keranjang Baru:", keranjang_baru)  # Output: ['Laptop', 'Mouse', 'Keyboard']
print("Keranjang Asli:", keranjang_asli)  # Output: ['Laptop', 'Mouse'] -> TETAP UTUH!
```

---

### Bagaimana Memory (RAM) Mengelolanya?

Menulis pure function memang membuat Python sering membuat salinan data baru di RAM. Namun, ini tidak akan membuat memori komputer jebol. Python memiliki Garbage Collector otomatis yang akan langsung menghancurkan salinan data tersebut dan mengosongkan RAM kembali begitu fungsinya selesai bekerja.

Kita sengaja mengorbankan sedikit ruang RAM demi memotong waktu tunggu CPU agar aplikasi kita berjalan jauh lebih cepat secara paralel!

---

## 3. Apa itu Rekursi?

**Rekursi** adalah sebuah teknik pemrograman di mana sebuah fungsi memanggil dirinya sendiri di dalam baris kodenya sendiri. Di dalam Pemrograman Fungsional murni (yang menghindari variabel pencacah yang berubah-ubah), rekursi merupakan alat utama untuk melakukan pengulangan menggantikan loop `for` atau `while`.

Agar komputer tidak terjebak dalam pengulangan tanpa batas yang bisa menyebabkan *crash* (**Stack Overflow**), sebuah fungsi rekursif wajib memiliki dua komponen utama:

1. **Base Case (Kondisi Berhenti):** Aturan mutlak yang memberi tahu fungsi kapan harus berhenti memanggil dirinya sendiri.
2. **Recursive Case (Langkah Rekursif):** Bagian di mana fungsi memanggil dirinya sendiri lagi, tetapi dengan nilai input yang memperkecil masalah untuk mendekati *Base Case*.

---

### Fungsi dan Peran

* **Mengolah Data Bercabang (Tree Data Structure):** Sangat unggul untuk menyisir data yang strukturnya bercabang-cabang dan kedalamannya tidak pasti, seperti sistem folder komputer, struktur menu restoran berjenjang, atau utas komentar (threaded comments) di media sosial.
* **Membongkar JSON/HTML Kompleks:** Digunakan di balik layar oleh library besar untuk memparsing data JSON yang bersarang (*nested JSON*) dari API.
* **Computational Thinking:** Menguasai rekursi melatih insting kita memahami bagaimana komputer mengelola memori (*Call Stack*).

---

### Contoh Kode

#### Kasus 1: Contoh Konseptual (Menghitung Faktorial)
Contoh klasik untuk melihat bagaimana fungsi memanggil dirinya sendiri secara berantai:

```python
def hitung_faktorial(n):
    # 1. BASE CASE: Berhenti jika n sudah mencapai 1
    if n <= 1:
        return 1
    # 2. RECURSIVE CASE: Panggil diri sendiri dengan n - 1
    else:
        return n * hitung_faktorial(n - 1)

print(hitung_faktorial(5)) # Output: 120 (5 * 4 * 3 * 2 * 1)
```

#### Kasus 2: Kasus Nyata di Industri (Mencari File di Dalam Folder Bersarang)
Contoh bagaimana rekursi menyisir struktur data berbentuk pohon (Tree) yang kedalamannya tidak pasti:

```python
# Simulasi penyimpanan cloud (folder di dalam folder)
storage_drive = {
    "Dokumen": {
        "Tugas_Kuliah": {
            "skripsi_v1.docx": "File Word",
            "skripsi_final_FIX.docx": "File Word"
        },
        "biodata.txt": "File Teks"
    },
    "Musik": {
        "Pop": {
            "song.mp3": "Audio"
        }
    }
}

def cari_file(folder, target):
    for nama, isi in folder.items():
        # BASE CASE: Jika nama file langsung cocok
        if nama == target:
            return f"Ketemu! Jenis: {isi}"
        
        # RECURSIVE CASE: Jika menemukan folder lagi (dictionary), masuk lebih dalam
        if isinstance(isi, dict):
            hasil = cari_file(isi, target)
            if hasil: # Jika ketemu di dalam, oper hasilnya ke atas
                return hasil
    return None

# Uji Coba mencari file yang tersembunyi jauh di dalam folder
print(cari_file(storage_drive, "skripsi_final_FIX.docx"))
# Output: Ketemu! Jenis: File Word
```
---

# Catatan Belajar: Menguasai Trio Maut FP (Map, Filter, dan Reduce) di Python

Catatan ini saya buat untuk mendokumentasikan pemahaman saya tentang tiga fungsi legendaris dalam Pemrograman Fungsional (FP): `map()`, `filter()`, dan `reduce()`. Tiga fungsi ini bukan sekadar sintaks biasa, melainkan fondasi arsitektur yang digunakan oleh *Data Engineer* untuk mengolah data berskala raksasa (*Big Data*) di ribuan server secara paralel.

---

## Aturan Emas Trio Maut (MFR)
1. **Aturan Parameter:** Ketiganya memiliki pola yang sama: Menerima **"Aturannya/Mesinnya"** dulu di parameter pertama, baru menerima **"Datanya"** di parameter kedua.
2. **Prinsip Immutability:** Tidak ada satu pun dari fungsi ini yang merusak atau mengubah data asli. Mereka selalu menghasilkan objek/data baru di memori.
3. **Lazy Evaluation (Malas):** Secara default, `map()` dan `filter()` tidak langsung memproses data ke RAM. Mereka mengembalikan objek khusus (*Iterator*). Komputer baru akan bekerja jika kita memaksa mengubahnya menjadi list menggunakan fungsi `list()`.

---

## 1. MAP (Fungsi Transformasi / Pemeta Data)

### A. Konsep & Fungsi
`map()` digunakan ketika kita ingin **mengubah setiap elemen** di dalam sebuah koleksi data menggunakan rumus atau aturan yang sama, tanpa terkecuali. Jika inputnya ada 5 data, outputnya pasti berbentuk 5 data baru yang sudah berubah wujud. Sebenarnya penggunaan map ini mirip sekali dengan `comprehension list`

### B. Anatomi Parameter & Kode Dasar
```python
map(fungsi_pengubah, iterable)
```
* **`fungsi_pengubah`**: Fungsi (bisa pakai `def` atau `lambda`) yang bertugas mengubah data. Fungsi ini **wajib menerima 1 input** karena memproses elemen satu per satu.
* **`iterable`**: Koleksi data asal (seperti *list* atau *tuple*) yang mau diubah.

**Contoh Kode Dasar:**
Mengubah daftar kata menjadi huruf kapital semua.
```python
kata_asli = ["pagi", "siang", "malam"]

# str.upper adalah fungsi bawaan Python untuk membuat huruf kapital
hasil_kapital = list(map(str.upper, kata_asli))

print(hasil_kapital) # Output: ['PAGI', 'SIANG', 'MALAM']
```

### C. Kasus Penggunaan di Industri
* **Normalisasi Data (Data Cleansing):** Mengubah format teks dari database, seperti merapikan format nomor telepon (menghapus spasi/strip) atau mengubah semua huruf menjadi kecil sebelum dianalisis.
* **Konversi Massal Tipe Data:** Mengubah semua data string angka yang ditarik dari file CSV menjadi tipe data *integer* atau *float* agar bisa dihitung secara matematika (`map(int, list_string)`).

---

## 2. FILTER (Fungsi Penyaring Data)

### A. Konsep & Fungsi
Sesuai namanya, `filter()` digunakan untuk **menyaring dan menyeleksi data** berdasarkan kondisi tertentu. Elemen yang lolos seleksi akan dipertahaman, sedangkan yang tidak lolos akan dibuang. Jika inputnya 5 data, outputnya bisa berkurang menjadi 3, 1, bahkan kosong jika tidak ada yang lolos.

### B. Anatomi Parameter & Kode Dasar
```python
filter(fungsi_penyaring, iterable)
```
* **`fungsi_penyaring`**: Fungsi yang **wajib mengembalikan nilai Boolean (True atau False)** dan menerima 1 input. Jika fungsi menghasilkan `True`, data tersebut lolos penyaringan.
* **`iterable`**: Koleksi data asal yang mau disaring.

**Contoh Kode Dasar:**
Menyaring angka-angka yang bernilai genap saja.
```python
deret_angka = [1, 2, 3, 4, 5, 6]

# Fungsi lambda akan mengembalikan True jika angka habis dibagi 2
angka_genap = list(filter(lambda x: x % 2 == 0, deret_angka))

print(angka_genap) # Output: [2, 4, 6]
```

### C. Kasus Penggunaan di Industri
* **Manajemen Akses Sistem:** Menyaring daftar pengguna dari database untuk mengambil pengguna yang status akunnya `"aktif"` saja atau yang memiliki peran `"admin"`.
* **Penyaringan Log Error:** Menyisir jutaan baris laporan aktivitas server (*server logs*) untuk hanya menampilkan baris data yang mengandung kode eror `500` atau kata `"ERROR"`.

---

## 3. REDUCE (Fungsi Penciutan / Akumulasi Data)

### A. Konsep & Fungsi
Berbeda dengan `map` and `filter` yang menghasilkan koleksi data baru, `reduce()` digunakan untuk **menciutkan seluruh elemen data menjadi SATU nilai tunggal saja**. Fungsi ini tidak langsung aktif di Python, kita harus mengambilnya dari modul bawaan bernama `functools`.

### B. Anatomi Parameter & Kode Dasar
```python
from functools import reduce

reduce(fungsi_akumulator, sequence, nilai_awal)
```
* **`fungsi_akumulator`**: Fungsi pengolah yang **wajib menerima 2 input** (biasanya ditulis sebagai `x` dan `y`).
    * `x` (*Accumulator*): Kotak memori sementara yang menyimpan hasil hitungan/proses dari putaran sebelumnya.
    * `y` (*Current Item*): Elemen data berikutnya dari list yang sedang antre untuk diproses.
* **`sequence`**: Koleksi data yang mau diciutkan.
* **`nilai_awal`** *(Opsional tapi Penting)*: Nilai awal untuk si `x` di putaran pertama. Jika tidak diisi, `x` akan otomatis mengambil elemen pertama dari list.

**Contoh Kode Dasar:**
Menghitung total hasil perkalian semua angka di dalam list.
```python
from functools import reduce

angka = [1, 2, 3, 4]

# x adalah hasil perkalian sementara, y adalah angka antrean berikutnya
total_kali = reduce(lambda x, y: x * y, angka)

print(total_kali) # Output: 24 (Hasil dari 1 * 2 * 3 * 4)
```

### C. Kasus Penggunaan di Industri
* **Data Aggregation (Penyatuan Data Terpisah):** Menghitung total omzet penjualan atau total performa harian dari jutaan data transaksi yang terpisah di server.
* **Mencari Nilai Ekstrem:** Menyisir jutaan data suhu secara bergulir untuk mencari mana suhu tertinggi (*Maximum*) atau terendah (*Minimum*).
* **Pembuatan Cache Memori (Nested Dictionary):** Menjahit potongan-potongan data profil pengguna (bentuk *List*) menjadi satu struktur kamus bersarang (*Nested Dictionary*) utuh berdasarkan ID uniknya, agar fitur pencarian di aplikasi bisa berjalan instan tanpa *looping* ($O(1)$ Time Complexity).

---

## Tabel Rangkuman Perbedaan

| Fungsi | Jumlah Input | Jumlah Output | Kegunaan Utama |
| :--- | :--- | :--- | :--- |
| **`map()`** | n data | n data baru | Mengubah wujud/bentuk setiap data |
| **`filter()`** | n data | <= n data | Menyaring/membuang data sampah |
| **`reduce()`** | n data | **1 nilai tunggal** | Menghitung total / menyatukan struktur data |
