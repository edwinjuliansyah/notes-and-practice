# Python I/O & File Handling Basics

Catatan ringkas tentang:
- Function input()
- Parameter print (`sep`, `end`, `flush`)
- Penulisan ke file (`file=`, `with open`)
- Mode file (`w`, `a`)
- String formatting (`.format`, `f-string`)

## 1. Function input()
Untuk meminta input ke user biasanya type datanya string jika angka ubah dulu `int(input())`
### Contoh
```python
name = input("Masukan nama: ") 
print("Nama: ", name) 

#output
#Masukkan nama: Edwin
#Nama: Edwin

num1 = int(input("Masukan angka pertama: "))
num2 = int(input("Masukan angka kedua: "))
print("Hasil: ", num1 + num2)

#output
#Masukan angka pertama: 3
#Masukan angka kedua: 4
#Hasil:  7
```

## 2. Print Parameters
- `sep` → pemisah antar argumen `sup=("")` tidak perlu digunakan jika menggunakan string formatting 
- `end` → untuk mengontrol baris baru saat mencetak `end="\n\n"`
- `flush` → memaksa output muncul segera `flush=True OR flush=False`
### Contoh
```python
print("Siapa", "Nama", "Kamu", sep="-", end="\n\n", flush=True)

#output
#Siapa-Nama-Kamu
#(ada newline kosong disini)
```

## 3. File Handling
-  Penggunaan file tidak close() otomatis setelah open() `file=open("x.txt", "w")`
- Penggunaan with close() otomatis 
 ```python
  with open("x.txt", "w") as f:
      f.write("halo")
  ```
Keduanya untuk mengirimkan output ke file x

Mode:
- `w` → write (menimpa)
- `a` → append (menambah)
### Contoh 
```python
- print("Halo Kamu", file=open("x.txt", "w"))
- with open("x.txt", "w") as f:
     print("Halo Kamu", file=f)
```


## 4. String Formatting
- `"Halo {}".format(name)`
- `f"Halo {name}"`
### Contoh
```python
name1 = "Edwin"
name2 = "Jul"
print("Halo {} {}".format(name1, name2)) # bisa menggunakan indeks untuk perubahan posisi {1} {0}
print(f"Halo {name1} {name2})
```

# Full Code
```python
name1 = "Edwin"
name2 = "Jul"

- print("Halo {} {}".format(name1, name2), end="\n\n", file=open("x.txt", "w"), flush=True)
- with open("x.txt", "w") as f:
     print("Halo", "{} {}".format(name1, name2), end="\n\n", file=f, flush=True)

OR

- print(f"Halo {name1} {name2}", end="\n\n", file=open("x.txt", "w"), flush=True)
- with open("x.txt", "w") as f:
     print(f"Halo {name1} {name2}", end="\n\n", file=f, flush=True)

```
