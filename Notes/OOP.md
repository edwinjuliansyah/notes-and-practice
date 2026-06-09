oop
- declarative
- procedural
- object-oriented
- function
- logic
- even-driven
- flow-driven
and more..

bagian oop

class ->defind with 'class' keyword
	attribute/property -> can be variable
	behavior/method -> can be function
	object -> hasilnya

konsep

- inheritance

creating a new class witch is declarative of an existing one

- polymorphism

the ability of function to change its behavior when called by different object

- encapsulation

limits access to method and variable by encasing them in a single unit of scope

- abstraction
hide implementation details for data security

other concepts

method loading

method overriding

constructors
and more...

---

public, protect, private di python

menisme dalam python ketiga fungsi ini hanya berfungsi sebagai visibilitas untuk developer. python tidak ada pembatasan akses paksa (Access Modifiers). semua properti pada dasarnya public. oleh karna itu aturan dibuat berdasarkan Konvensi Kesepakatan (Underscore).

tanpa_underscore (Public): Bebas dipanggil dan diubah dari luar kelas.

_satu_underscore (_Protected): Rambu lalu lintas. Sinyal bahwa ini untuk internal kelas dan subkelasnya saja. Jangan diakses langsung dari luar (meski Python tidak melarang).

__dua_underscore (__Private): Memicu Name Mangling. Nama variabel diubah otomatis menjadi _NamaKelas__variabel. Tujuannya bukan untuk keamanan, melainkan mencegah tabrakan nama saat kelas diturunkan (Inheritance).

---  

inherence memiliki kemampuan untuk menurunkan attribute atau method dari 1 class (induk) ke class lain (anak), class tersebut memiliki fungsi yang sama hanya saja ada sedikit perubahan 

- class induk biasanya disebut: parent/super/base class
- class anak biasanya disebut: child/sub/derived class

contoh dasar 
```python
class a:
  pass

class b(a):
  pass
```
contoh dengan pewarisan ganda
```python
class a:
  pass

class b:
  pass

class c(a, b):
  pass
```
contoh dengan pewarisan multi-level
```python
class A:
   a = 1

class B(A):
   a = 2

class C(B):
   pass

c = C()
print(c.a)

# hasil dari kode diatas bukanlah 1 melainkan 2 karna meskipun B adalah anak dari class A tetapi C mengambil nilai a dari class B.
```
dua fungsi bawaan yang dapat berguna ketika mencoba menemukan hubungan antara kelas dan objek yang berbeda: `issubclass()`  dan `isinstance()`.

`issubclass(class A, class B)`

Dua kelas diberikan sebagai argumen ke fungsi ini dan hasil Boolean dikembalikan. Contoh di atas dapat diperluas sebagai berikut. 
```python
print(issubclass(A,B))
print(issubclass(B,A))

#output 
#false 
#true
```
ini dapat dibaca sebagai: "Apakah B adalah subkelas dari A?" hasilnya adalah "True" pada kasus kedua di mana child B adalah subkelasnya.

Fungsi bawaan lain yang mirip dengan fungsi ini adalah isinstance() yang menentukan apakah suatu objek merupakan instance dari suatu kelas. contoh
```python
class A:
	pass
class B(A):
	pass

b = B()
print(isinstance(b,B))
print(isinstance(b,A))

#output
#True
#True
```
jika ingin menggunakan attribute atau method dari parent harus menggunakan fungsi python super()
```python
class Fruit():
    def __init__(self, fruit):
        print('Fruit type: ', fruit)


class FruitFlavour(Fruit):
    def __init__(self):
        super().__init__('Apple')
        print('Apple is sweet')

apple = FruitFlavour()
```
