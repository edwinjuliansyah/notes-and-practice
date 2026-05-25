# Pemrograman Fungsional (FP) di Python

## Apa itu Pemrograman Fungsional?
Paradigma atau gaya berpikir dalam pemrograman di mana kita membangun aplikasi dengan menyusun fungsi-fungsi murni (*pure functions*) dan menjaga prinsip **Immutability** (data asli tidak boleh diubah). Fokus utamanya adalah pada *apa yang ingin dihasilkan*, bukan mendikte langkah demi langkah *bagaimana komputer melakukannya*.

## Fungsi dan Peran Utama dalam Kode
1. **Menghindari Bug (Bebas Side Effects):** Data asli tidak akan berubah atau rusak di tengah jalan secara tidak sengaja oleh fungsi lain karena fungsinya terisolasi dengan baik.
2. **Mudah Diuji (Testable):** Fungsi bersifat mandiri. Jika diberi input "A", nilainya akan selalu "B", tidak peduli kondisi aplikasi di luar fungsi tersebut.
3. **Mendukung Kerja Paralel (Concurrency):** Sangat cocok untuk arsitektur modern karena setiap inti CPU (*multi-core*) bisa memproses data secara bersamaan tanpa perlu mengantre (*locking*) akibat berebutan variabel yang sama.

## Insight Penting: Trade-off RAM vs CPU
* **Mitos:** Banyak yang mengira pemrograman fungsional membuat penggunaan RAM menjadi lebih hemat.
* **Faktanya:** FP justru **lebih boros RAM** karena Python dipaksa membuat objek/salinan data baru di memori setiap kali sebuah fungsi memproses sesuatu (untuk menjaga data asli tetap utuh).
* **Kesimpulan:** Di industri modern, sengaja mengorbankan sedikit ruang RAM (karena harga RAM murah) demi memotong waktu tunggu CPU (yang sangat berharga). Hasilnya, proses eksekusi kode menjadi jauh lebih singkat, efisien secara waktu, dan yang paling penting: aplikasi stabil serta aman dari korupsi data.

## Contoh Kode Sederhana (Gaya Pythonic)
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

## Apa itu Pure Function?

**Pure Function** bukan sekadar "teknik" menulis kode atau "jenis" fungsi tertentu, melainkan sebuah **karakteristik wajib** dalam Pemrograman Fungsional. Sebuah fungsi baru sah disebut murni jika memenuhi dua syarat mutlak:

1. **Hasilnya Selalu Konsisten (Deterministic):** Jika kita memasukkan input (argumen) yang sama, fungsi tersebut harus selalu mengembalikan hasil yang sama, kapan pun dan berapa kali pun dijalankan.
2. **Tidak Memiliki Efek Samping (No Side Effects):** Fungsi tidak boleh mengubah status, data, atau variabel apa pun di luar dirinya. Ia tidak merusak data asli yang dimasukkan, tidak mengubah variabel global, bahkan tidak memicu fungsi I/O seperti menulis file atau menampilkan `print()` ke terminal (karena itu mengubah status layar).

---

## Peran dan Fungsinya dalam Aplikasi

* **Mudah Diuji (Testable):** Karena fungsinya terisolasi, kita tidak perlu repot melakukan *setup* database palsu atau memanipulasi variabel global saat melakukan *testing*. Cukup beri input, lalu cek outputnya.
* **Aman dari Bug Misterius:** Kita bisa yakin 100% bahwa memanggil fungsi ini di bagian mana pun tidak akan merusak data di bagian aplikasi yang lain secara tidak sengaja.
* **CPU Efisien (Dukungan Concurrency):** Karena sifatnya yang tidak mengubah data secara langsung (*immutability*), banyak core CPU bisa memproses fungsi ini secara bersamaan tanpa ada drama antrean data (*locking*).

---

## Contoh Kode: Kontras Impure vs Pure

### Contoh Impure Function (Tidak Murni)
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

### Contoh Pure Function (Murni)
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

## Bagaimana Memory (RAM) Mengelolanya?

Menulis pure function memang membuat Python sering membuat salinan data baru di RAM. Namun, ini tidak akan membuat memori komputer jebol. Python memiliki Garbage Collector otomatis yang akan langsung menghancurkan salinan data tersebut dan mengosongkan RAM kembali begitu fungsinya selesai bekerja.

Kita sengaja mengorbankan sedikit ruang RAM demi memotong waktu tunggu CPU agar aplikasi kita berjalan jauh lebih cepat secara paralel!

---

## Apa itu Rekursi?

**Rekursi** adalah sebuah teknik pemrograman di mana sebuah fungsi memanggil dirinya sendiri di dalam baris kodenya sendiri. Di dalam Pemrograman Fungsional murni (yang menghindari variabel pencacah yang berubah-ubah), rekursi merupakan alat utama untuk melakukan pengulangan menggantikan loop `for` atau `while`.

Agar komputer tidak terjebak dalam pengulangan tanpa batas yang bisa menyebabkan *crash* (**Stack Overflow**), sebuah fungsi rekursif wajib memiliki dua komponen utama:

1. **Base Case (Kondisi Berhenti):** Aturan mutlak yang memberi tahu fungsi kapan harus berhenti memanggil dirinya sendiri.
2. **Recursive Case (Langkah Rekursif):** Bagian di mana fungsi memanggil dirinya sendiri lagi, tetapi dengan nilai input yang memperkecil masalah untuk mendekati *Base Case*.

---

## Fungsi dan Peran

* **Mengolah Data Bercabang (Tree Data Structure):** Sangat unggul untuk menyisir data yang strukturnya bercabang-cabang dan kedalamannya tidak pasti, seperti sistem folder komputer, struktur menu restoran berjenjang, atau utas komentar (threaded comments) di media sosial.
* **Membongkar JSON/HTML Kompleks:** Digunakan di balik layar oleh library besar untuk memparsing data JSON yang bersarang (*nested JSON*) dari API.
* **Computational Thinking:** Menguasai rekursi melatih insting kita memahami bagaimana komputer mengelola memori (*Call Stack*).

---

## Contoh Kode

### Kasus 1: Contoh Konseptual (Menghitung Faktorial)
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

### Kasus 2: Kasus Nyata di Industri (Mencari File di Dalam Folder Bersarang)
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
