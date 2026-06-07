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

  
