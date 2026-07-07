# Error dan Exception
Error adalah kesalahaan sebelum kode dijalankan, kesalahan ini seperti syntax error biasanya disebebkan karna lupa( : ), indentasi, dan lainnya. 

Exception terjadi saat kode secara struktur sudah benar, tetapi ada masalah "tak terduga" saat program sedang berjalan. Misal 23/0 secara syntax munkin tidak salah tetapi secara matematika ini tidak mungkin dan akan menyebabkan ZeroDivisionError.

Ada beberapa exception yang biasanya ditemukan:
- `ZeroDivisionError` Mencoba membagi angka dengan nol.
- `FileNotFoundError` Mencoba membuka file yang tidak ada di folder.
- `TypeError` Melakukan operasi pada tipe data yang salah (misal: int + str).
- `IndexError` Mencoba mengakses indeks list yang di luar jangkauan.
- `KeyError` Mencoba mencari kunci (key) yang tidak ada di dalam dictionary.

Menangani exception bukan sekadar agar program tidak error, tapi tentang User Experience dan Keamanan:
- Mencegah Crash: User tidak akan senang jika aplikasi atau websitemu tiba-tiba mati total karena satu kesalahan input.
- Debugging: Pesan error (Traceback) membantumu menemukan baris kode mana yang bermasalah secara spesifik.
- Logging: Kamu bisa mencatat kapan error terjadi untuk diperbaiki di masa depan tanpa memperlihatkan detail teknis yang membingungkan ke user.

Agar program tidak langsung "mati" (crash) saat terjadi Exception, kita menggunakan blok penanganan/try-except.
```python
try:
    angka1 = int(input("Masukkan pertama: "))
    angka2 = int(input("Masukkan kedua: "))
    hasil = angka1 / angka2
    print(f"Hasilnya: {hasil}")
except ZeroDivisionError:
    print("Error: Kamu tidak bisa membagi dengan nol!")
except ValueError:
    print("Error: Masukkan angka yang valid, bukan huruf!")
except Exception as e:
    print(f"Terjadi kesalahan tak terduga: {e}")
```

.__class__ dalam Exception Handling

Saat menggunakan blok except Exception as e:, kita menangkap segala jenis error secara umum. Atribut .__class__ digunakan untuk mengetahui identitas kelas asli (cetak biru) dari error yang terjadi, bukan sekadar membaca pesan teksnya.

Mengapa Membutuhkan .__class__?
- Akurasi Tipe Data: Menghindari pengecekan error berbasis teks (str(e)) yang rawan berubah/salah deteksi.
- Sistem Logging / Bot: Mempermudah pengelompokan jenis error (seperti KeyError, ValueError, ZeroDivisionError) ke dalam database, file log, atau laporan otomatis.
```python
try:
    # Contoh error: mengubah teks menjadi objek angka
    hasil = int("bukan_angka")
except Exception as e:
    # Mengambil nama kelas error asli secara otomatis
    tipe_error = e.__class__  # Output: <class 'ValueError'>
    
    print(f" Terjadi Error: {tipe_error}")
    print(f" Detail Pesan: {e}")

#gunakan .__name__ untuk mengambil nama string dalam class
try:
    hasil = int("bukan_angka")
except Exception as e:
    tipe_error = e.__class__.__name__  # Output: 'ValueError'
    
    print(f" Terjadi Error: {tipe_error}")
    print(f" Detail Pesan: {e}")
```
# File Handling
- Function `open()` digunakan untuk read, write, create files. open menerima 2 argument open('file_name'/'lokasi_file', 'mode').
  - `file_name` `lokasi_name` untuk mencari file. 
  - `mode` untuk tindakan read, write ataupun create ini juga menentukan apakah output ingin dalam format teks atau biner.
    - `r` = open dan read.
    - `r+` = open file untuk reading dan writing.
    - `w` = open untuk writing(ini akan menimpa file).
    - `a` = open untuk editing dan appending data.

  Dalam python menerima 2 format text dan biner secara default file handling dengan format text, jika ingin membuka dengan format biner perlu menambahkan b diakhir (`rb`, `rb+`, `wb`, `ab`).

- Function `close()` digunakan untuk menutup koneksi file yang terbuka.

- Function `with` opsi lain jika ingin open file yaitu dengan with, keuntungan menggunakan with adalah ini akan close secara otomatis.

# Create, Write, Read
Untuk create file baru dan menulis 1 line.
```python
with open('file_baru.txt', 'w') as f:
    f.write('baris pertama')
```
Jika ingin multiple line	
```python
with open('file_baru.txt', 'w') as f:
    f.writelines(['baris pertama\n', 'baris kedua'])
```
Jika ingin menambahkan isi file tanpa menimpa gunakan append.
```python
with open('file_baru.txt', 'a') as f:
    f.writelines(['\nbaris ketiga', '\nbaris keempat'])
```
read() -> output string yang akan berisi semua karakter.
```python
with open('file_baru.txt', 'r') as f:
    content = f.read()
    print(content)
```
Dapat juga untuk mengeluarkan output beberapa karakter pertama.
```python
with open('file_baru.txt', 'r') as f:
    content = f.read(40)
    print(content)
```
readline() -> output 1 baris sebagai string.
```python
with open('file_baru.txt', 'r') as f:
    content = f.readline()
    print(content)
```
Sama seperti sebelumnya ini juga dapat mengeluarkan output beberapa karakter pertama.
```python
with open('file_baru.txt', 'r') as f:
    content = f.readline(10)
    print(content)
```
readlines() -> output semua karakter dalam bentuk order list. bisa menggunakan fungsi for untuk read file.
```python
with open('file_baru.txt', 'r') as f:
    content = f.readlines()
    print(content)
```
Contoh penanganan file dengan `try-except`
```python
try:
    with open('file123.txt', 'r') as file:
        print(file.read())
except FileNotFoundError:
    print("File tidak dapat ditemukan")

```

# Abolute and Relative Patchs
Path (jalur) adalah cara kita memberitahu komputer di mana sebuah file atau folder berada.
- Absolute Path adalah alamat lengkap dan spesifik dari sebuah file, dimulai dari akar paling dasar (Root) sistem operasi hingga ke file tujuan. Jalur ini tidak peduli di mana posisi kamu sekarang jika kamu memberikan alamat ini, komputer akan selalu bisa menemukannya. Ciri Khas: Selalu dimulai dengan `/` (di Linux/macOS) atau `C:\` (di Windows).
Contoh:
  - Linux/macOS: `/home/user/project/script.py`
  - Windows: `C:\Users\Admin\Documents\file.txt`

- Relative Path adalah alamat file yang ditentukan berdasarkan posisi kamu berada saat ini (Current Working Directory). Jalur ini sangat bergantung pada "titik awal" kamu. Ciri Khas: Tidak dimulai dengan `/` atau `C:\`. Sering menggunakan simbol khusus:
  - `.` (Satu titik): Merujuk pada folder tempat kamu berada sekarang.
  - `..` (Dua titik): Merujuk pada folder satu tingkat di atasnya (folder induk).

| Simbol | Arti | Contoh Penggunaan |
| :--- | :--- | :--- |
| `/` | **Root** (Akar paling bawah) | `cd /var/log` (Langsung ke folder log di sistem)|
| `~` | **Home Directory** (User) | `cd ~/Documents` (Ke folder dokumen milik user)|
| `.` | **Current Directory** | `./program.sh` (Jalankan program di folder ini)|
| `..` | **Parent Directory** | `cd ..` (Keluar satu tingkat ke folder atas)|
