# Tipe data dasar

## 1. numeric
- Integer `3` -> bilangan bulat.
- float `3.14` -> bilangan desimal.
- complex number `a = 1 + 1i` -> bilangan kompleks dengan bagian real dan imajiner.

## 2. Sequence
kumpulan data yang terurut dan dapat diakses berdasarkan indeks.
- string `"hallo"` -> urutan karakter.
- list `[]` -> daftar elemen yang bisa berbeda tipe.
    - list = [1, 2, 3, 4, 5]
    - list.insert(len(list), 6)
    - list.append(6)
    - list.extend([6, 7, 8, 9])
    - list.pop(4)
    - del list[2]
- tuple `()` -> mirip list tapi tidak bisa diubah.
    - tuple = (1, "strings", 4.5, True)
    - print(tuple.count('strings')) #output 1
    - print(tuple.index(4.5)) #output 2


## 3. Dictionary `{}`
Menyimpan data dalam pasangan {`"key"`: `value`} yang dapat diakses langsung melalui key. Dictionary menerima key dengan type string, integer, tuple `(2, 3)`. Jika kunci duplikat, isi kunci lama akan tertimpa dengan isi kunci baru. 
```python
kamus = {1: "kopi", 2: "teh", 3: "roti" }
kamus[2] = "susu" #ubah value
del kamus[1] #menghapus dict
kamus[3] = "indomie" #update value key 3
print(kamus)
#output
#{2: 'susu', 3: 'indomie'}
```
```python
kamus = {}  #deklarasi dict kosong, secara default ini typenya dict bukan set
kamus[6] = "kucing"
kamus[3] = "anjing"
kamus[2] = "kelinci"
kamus["nama"] = "kuda"
kamus[10] = "kepiting"
kamus[(2, 3)] = "kerbau"
del kamus[3]

for i in kamus:
  print(i, kamus[i], sep=" -> ")

#output
#6 -> kucing
#2 -> kelinci
#nama -> kuda
#10 -> kepiting
#(2, 3) -> kerbau
```
Ketika ingin melakukan perulangan (looping/iterating) pada dictionary, python menyediakan beberapa cara tergantung pada bagian data mana yang ingin kita ambil.
- `Standard Iteration` / `.key()`
  
    Secara default, jika langsung memasukkan objek dictionary ke dalam perulangan for, Python hanya akan mengambil key dari dictionary tersebut.
```python
stok_buah = {'Apel': 10, 'Jeruk': 5, 'Mangga': 8}
for buah in stok_buah:
    print(buah)
#Output
#Apel
#Jeruk
#Mangga
```
- `.items()`
  
    Metode `.items()` mengembalikan objek view yang berisi pasangan key dan value dalam bentuk tuple (key, value).
```python
stok_buah = {'Apel': 10, 'Jeruk': 5, 'Mangga': 8}

for buah, jumlah in stok_buah.items():
    print(f"Stok buah {buah} tinggal {jumlah} biji.")

#Output
#Stok buah Apel tinggal 10 biji.
#Stok buah Jeruk tinggal 5 biji.
#Stok buah Mangga tinggal 8 biji.
```
- `.values()`
- 
    Metode `.values()` hanya mengembalikan objek view yang berisi nilai (value) saja dari dictionary, tanpa memedulikan apa kuncinya.
```python
stok_buah = {'Apel': 10, 'Jeruk': 5, 'Mangga': 8}

total_stok = 0
for jumlah in stok_buah.values():
    total_stok += jumlah

print(f"Total semua buah: {total_stok}")

#Output
#Total semua buah: 23
```

## 4. Boolean
hanya memiliki dua nilai, ` true ` atau ` false `  digunakan untuk kondisi logika.

## 5. set `{}`
kumpulan data unik yang tidak berurutan, tidak memiliki indeks, dan immutable.
- set = {1, 2, 3, 4, 5, 5} set tidak bisa menerima nilai duplikat
  - set.add(6)
  - set.remove(2)
  - set.discard(2)

- set1 = {1, 2, 3, 4, 5}
- set2 = {4, 5, 6, 7, 8}
  - print(set1.union(set2)) # menggabungkan 2 set menjadi 1
  #or
  - print(set1 | set2)
 
  - print(set1.intersection(set2)) hasil {4, 5}
  #or
  - print(set1 & set2)

  - print(set1.difference(set2)) hasil {1, 2, 3} yang ada di 1 tidak ada di 2 
  #or 
  - print(set1 - set2)

  - print(set1.symmetric_difference(set2)) hasil {1, 2, 3, 6, 7, 8} yang ada di 1 dan 2 tidak di tampilkan
  #or 
  - print(set1 ^ set2)

## Type Casting
`implicit` sudah otomatis dari python.

`explicit` kita yang mengubahnya.

`int()` `float()` `bool()` `str()` `ord()` `hex()` `oct()` `tuple()` `dict()` `set()` `list()`

# Indexing
## Dasar
`x[0]` : Mengambil elemen pertama.

`x[1]` : Mengambil elemen kedua.

`x[-1]` : Mengambil elemen terakhir.

`x[-2]` : Mengambil elemen kedua dari belakang.

## Slicing (Mengambil Range/Rentang)
format `x[start:stop]` stop bersifat exclusive elemen di index tersebut tidak diikutkan.

`x[1:4]` : Mengambil index 1, 2, dan 3.

`x[:3]` : Mengambil dari awal sampai sebelum index 3 (index 0, 1, 2).

`x[2:]` : Mengambil dari index 2 sampai paling akhir.

`x[:]` : Mengambil seluruh elemen (copy list).

## Slicing dengan Step (Lompatan)

Formatnya `x[start:stop:step]`

`x[::2]` : Mengambil elemen dengan melompat setiap 2 langkah (index 0, 2, 4, ...).

`x[::-1]` : Membalik urutan list (reverse).

`x[::-2]` : Membalik urutan list dengan lompatan setiap 2 (index ..., 4, 2)

Note: Jika mengambil data dari belakang / reserve lalu angka `start` lebih kecil dari `stop` maka akan error `x[1:4:-1]` hasil tuple kosong

---
# list comprehension

Komprehensi dalam Python adalah cara untuk membuat urutan baru dari urutan yang sudah ada.

Ada empat jenis pemahaman utama dalam Python: 

- Pemahaman daftar `[ <expression> for x in <sequence> if <condition>]`
```python
data = [2,3,5,7,11,13,17,19,23,29,31]

# Ex1: List comprehension: updating the same list
data = [x+3 for x in data]
print("Updating the list: ", data)

# Ex2: List comprehension: creating a different list with updated values
new_data = [x*2 for x in data]
print("Creating new list: ", new_data)

# Ex3: With an if-condition: Multiples of four:
fourx = [x for x in new_data if x%4 == 0 ]
print("Divisible by four", fourx)

# Ex4: Alternatively, we can update the list with the if condition as well
fourxsub = [x-1 for x in new_data if x%4 == 0 ]
print("Divisible by four minus one: ", fourxsub)

# Ex5: Using range function:
nines = [x for x in range(100) if x%9 == 0]
print("Nines: ", nines)
```
- Pemahaman kamus `{ key:value for key, value in <sequence> if <condition> }`
```python
# Using range() function and no input list
usingrange = {x:x*2 for x in range(12)}
print("Using range(): ",usingrange)

# Lists
months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
number = [1,2,3,4,5,6,7,8,9,10,11,12]

# Using one input list
numdict = {x:x**2 for x in number}
print("Using one input list to create dict: ", numdict)

# Using two input lists
months_dict = {key:value for (key, value) in zip(number, months)}
print("Using two lists: ", months_dict)
```
- Pemahaman set 
Pemahaman set berhubungan dengan tipe data set dan sangat mirip dengan pemahaman daftar. Satu-satunya perbedaan utama adalah penggunaan tanda kurung kurawal untuk himpunan, bukan tanda kurung siku seperti pada daftar. Sebagai contoh:
```python
set_a = {x for x in range(10,20) if x not in [12,14,16]}
print(set_a)
```
- Pemahaman generator
Pemahaman Generator (atau sering disebut Generator Expression) adalah cara ringkas untuk membuat sebuah Iterator di Python. Sintaksisnya mirip dengan List Comprehension, tetapi menggunakan tanda kurung biasa ( ) bukan kurung siku [ ].

Berbeda dengan List yang langsung membuat semua data di memori (Eager Evaluation), Generator menggunakan prinsip Lazy Evaluation—ia hanya menyimpan rumus/algoritma dan baru memproduksi data satu per satu saat diminta.
```python
# Sintaksis Dasar
(expression for item in iterable if condition)
```
Generator vs Tuple vs List

Meskipun menggunakan tanda kurung (), Generator bukan Tuple!

- List [] & Tuple (): Adalah kontainer data statis. Datanya sudah ada di dalam RAM saat didefinisikan.

- Generator (): Bukan kontainer penyimpan data, melainkan sebuah mesin pencetak data otomatis yang berjalan satu arah. Generator tidak bisa diubah (immutable) karena memang tidak ada data menetap di dalamnya untuk diubah.

4 Cara Memanggil/Mengambil Data dari Generator
Karena generator tidak menyimpan data dalam bentuk barisan fisik, kamu tidak bisa memanggil data menggunakan indeks seperti gen[0]. Berikut adalah 4 cara resmi untuk mengambil datanya:

1. Menggunakan for Loop (Paling Sering & Paling Aman)
Python akan otomatis mengambil data satu per satu dan berhenti sendiri tanpa memicu error saat data habis.
```python
kuadrat_gen = (x**2 for x in range(1, 4)) # Rumus untuk angka: 1, 4, 9

for angka in kuadrat_gen:
    print(angka)
# Output: 1, 4, 9
```
2. Menggunakan Fungsi next() (Secara Manual)
Digunakan jika kamu ingin mengontrol penuh kapan data selanjutnya harus diproduksi di dalam logika backend.
```python
antrian = (x for x in ["Budi", "Joko"])

print(next(antrian))  # Output: Budi
# ... jalankan logika backend lain ...
print(next(antrian))  # Output: Joko

# Jika dipanggil next(antrian) sekali lagi, akan memicu: Error StopIteration
```
3. Mengubahnya Menjadi List/Tuple (Casting)
Memaksa generator memproduksi semua datanya saat itu juga dan menyimpannya ke memori.Gunakan cara ini hanya jika jumlah datanya kecil. Jika datanya jutaan, RAM server bisa jebol.
```python
gen_huruf = (char.upper() for char in "abc")
list_hasil = list(gen_huruf)
print(list_hasil)  # Output: ['A', 'B', 'C']
```
4. Dimasukkan Langsung ke Fungsi Agregat Python
Sangat berguna untuk operasi matematika atau pemrosesan teks tanpa membuang memori.

```python
# Menghitung total 1 sampai 1 juta tanpa memakan RAM
total = sum(x for x in range(1, 1_000_001)) 

# Menggabungkan teks/string
kata = (k for k in ["Python", "Backend"])
print("-".join(kata))  # Output: Python-Backend
```
2 Karakteristik Mutlak Generator

- Sifat Sekali Pakai (One-time stream): Generator bergerak satu arah dan tidak bisa di-rewind (mundur). Begitu seluruh data sudah diproduksi/dibaca hingga habis, generator tersebut akan menjadi kosong (mati). Jika ingin digunakan lagi, kamu harus mendefinisikannya ulang.
- Efisiensi Memori Skala Tinggi (O(1)): Ukuran memori sebuah generator selalu konstan (sangat kecil, sekitar 100 bytes), tidak peduli apakah rumus tersebut ditujukan untuk menghasilkan 5 data atau 50 juta data.
