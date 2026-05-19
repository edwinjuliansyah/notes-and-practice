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
