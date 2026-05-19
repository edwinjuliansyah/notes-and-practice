# Conditional statement 

## If statement

Digunakan untuk mengecek kondisi berdasarkan nilai Boolean (True/False). Python mengevaluasi dari atas ke bawah dan akan berhenti di kondisi pertama yang terpenuhi.

- if: Kondisi utama yang pertama kali dicek.

- elif (else if): Kondisi tambahan jika if sebelumnya salah. Bisa ada banyak elif.

- else: "Pilihan terakhir" jika semua kondisi di atas tidak ada yang benar.
```python
status = 404

if status == 200:
    print("OK")
elif status == 404:
    print("Not Found")
elif status == 500:
    print("Server Error")
else:
    print("Unknown status")
#output
#Not Found
```

## Match statement

Diperkenalkan pada Python 3.10. Lebih bersih dan efisien daripada if-elif yang panjang jika kamu hanya ingin mencocokkan nilai spesifik atau pola tertentu.

- case: Nilai yang dicocokkan.

- case _: Wildcard (seperti else). Menangkap apa pun yang tidak cocok dengan case sebelumnya.
```python
status = 404

match status:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
    case 500:
        print("Server Error")
    case _:
        print("Unknown status")
#output
#Not Found
```

## Loop statement 

untuk mengeksekusi blok kode secara berulang sampai kondisi tertentu terpenuhi.

- for: digunakan untuk perulangan yang sudah diketahui angka akhirnya
```python
#basic code
for i in range(10):
    print(i) #output 0-9

#for juga bisa digunakan untuk type sting, list, set, tuple, dan dictonary
favorit = 'pisang', 'apel', 'anggur', 'jeruk', 'pepaya'
for i in favorit:
    print(i)

favorit = ['pisang', 'apel', 'anggur', 'jeruk', 'pepaya']
for i in favorit:
    print(i)

favorit = {'pisang', 'apel', 'anggur', 'jeruk', 'pepaya'}
for i in favorit:
    print(i)

favorit = ('pisang', 'apel', 'anggur', 'jeruk', 'pepaya')
for i in favorit:
    print(i)
#output
#pisang
#apel
#anggur
#jeruk
#pepaya

favorit = {1:'pisang', 2:'apel', 3:'anggur', 4:'jeruk', 5:'pepaya'}
for i in favorit:
    print(i, favorit[i], sep=" -> ")
#output
#1 -> pisang
#2 -> apel
#3 -> anggur
#4 -> jeruk
#5 -> pepaya
```    
jika ingin mencari suatu item dalam dafar, bisa menggunakan if dalam for
```python
favorit = ['pisang', 'apel', 'anggur', 'jeruk', 'pepaya']
for buah in favorit:
    if buah == 'anggur':
        print('Ya, buah', buah, "ada dalam daftar") 
    else:
        print('tidak, buah itu tidak ada dalam daftar')
#output
#tidak, buah itu tidak ada dalam daftar
#tidak, buah itu tidak ada dalam daftar
#Ya, buah anggur ada dalam daftar
#tidak, buah itu tidak ada dalam daftar
#tidak, buah itu tidak ada dalam daftar
```

outputnya adalah "tidak" akan dicetak sebanyak 4 kali dan "ya" 1 kali karna fungsi for tetap memutar, ia akan mengecek semua list sampai selesai. untuk mengatasi hal ini gunakan for-else cukup sejajarkan saja identasi for dengan else dan tambakan break di Bawah baris print dalam if.

```python
favorit = ['pisang', 'apel', 'anggur', 'jeruk', 'pepaya']
for buah in favorit:
  if buah == 'anggur':
    print('Ya, buah', buah, "ada dalam daftar")
    break
else:
    print('tidak, buah itu tidak ada dalam daftar')
#output
#Ya, buah anggur ada dalam daftar  
```
- while: digunakan untuk melakukan perulangan ketika jumlah akhir perulangannya tidak diketahui secara pasti. loop akan terus berjalan selama kondisi yang ditentukan bernilai `True`.
```python
# Contoh: Membaca data antrean sampai habis
antrean = ["Pelanggan A", "Pelanggan B", "Pelanggan C"]

while len(antrean) > 0:
    proses = antrean.pop(0)  # Mengambil elemen pertama
    print(f"Melayani: {proses}")

print("Semua antrean selesai diproses!")
```
- enumerate: digunakan untuk menambahkan indeks atau penomoran otomatis pada saat melakukan perulangan (looping) pada sebuah data koleksi (seperti list atau tuple).
```python
fitur_bot = ["Kirim Pesan", "Update Sheets", "Cek Status", "Log Out"]

# Menggunakan enumerate untuk membuat menu bernomor
for nomor, fitur in enumerate(fitur_bot, start=1):
    print(f"{nomor}. Fitur: {fitur}")
```
- break: digunakan untuk menghentikan paksa seluruh jalannya perulangan saat sebuah kondisi tertentu terpenuhi (True), tanpa memedulikan sisa iterasi berikutnya.
```python
# Mencari angka tertentu dalam data
angka_dicari = 7
kumpulan_data = [1, 3, 5, 7, 9, 11]

for angka in kumpulan_data:
    print(f"Memeriksa: {angka}")
    if angka == angka_dicari:
        print("Data ditemukan! Hentikan pencarian.")
        break  # Loop langsung berhenti di sini, angka 9 dan 11 tidak akan diperiksa
```
- continue: digunakan untuk melewati (skip) sisa kode di dalam loop pada iterasi saat ini, dan langsung melompat ke iterasi berikutnya jika kondisi bernilai True.
```python
# Mencetak hanya angka ganjil (melewati angka genap)
for i in range(1, 6):
    if i % 2 == 0:
        continue  # Jika genap, abaikan kode di bawah dan langsung lanjut ke angka berikutnya
    print(f"Angka Ganjil: {i}")
```
- pass: pernyataan kosong (null statement) yang tidak melakukan tindakan apa pun. digunakan sebagai tempat penampung sementara (placeholder) saat merancang struktur blok kode agar tidak memicu IndentationError ketika dites.
```python
# Menguji struktur logika tanpa menulis isinya terlebih dahulu
status_koneksi = False

if status_koneksi == True:
    # TODO: Buat fungsi kirim notifikasi ke WhatsApp di sini nanti
    pass 
else:
    print("Koneksi terputus!")
```
