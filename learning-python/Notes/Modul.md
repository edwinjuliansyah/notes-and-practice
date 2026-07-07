modul

modul adalah kumpulan fungsi yang dapat langsung digunakan tanpa membuatnya dari 0. jenis modul ada yang bult-in atau bisa kita buat sendiri.

Mengakses Modul

Interpreter Python mencari modul berdasarkan urutan lokasi berikut:
- Direktori/folder saat ini (current directory).
- Direktori modul bawaan Python (built-in module directory).
- Variabel lingkungan path Python (sys.path).
- Direktori default instalasi.
---
Pernyataan Impor

Modul Bawaan (Built-in): Sudah tersedia langsung di Python (contoh: import json, import sys, import math).

Paket (Packages): Kumpulan modul di dalam sebuah folder. Folder tersebut harus memiliki file khusus bernama __init__.py agar Python menganggapnya sebagai paket.

Paket Eksternal: Diunduh dari Python Package Index (PyPI) menggunakan manajer paket seperti pip (contoh: pip install numpy).

---
Cara Menulis Pernyataan Impor

```python
import math #mengambil semua fungsi yang berada di dalam modul math
root = math.sqrt(9) 
print(root)
#output 3
```
```python
from math import sqrt #hanya mengambil fungsi sqrt dalam modul math
root = sqrt(9) 
print(root)
#output 3
```

menggunakan alias 
```python
import math as m
from math import sqrt as s
```

import banyak fungsi dalam 1 modul
```python
from math import sqrt, log10, factorial
from math import * #jarang digunakan karna bisa membuat bingung untuk mengetahui sebuah fungsi berasal dari modul apa
```
---
Namespace dan Pelingkupan (Scoping)

Namespace adalah sistem yang memetakan nama variabel ke objeknya (seperti kamus/ dictionary). Scope atau pelingkupan adalah area di mana namespace tersebut bisa diakses.

Python menggunakan aturan resolusi LEGB untuk mencari variabel:
- Local: Variabel di dalam fungsi saat ini.
- Enclosed: Variabel di dalam fungsi yang membungkus (jika ada fungsi bersarang).
- Global: Variabel di luar fungsi (tingkat teratas file).
- Built-in: Kata kunci bawaan Python.

Kata kunci khusus untuk mengubah scope:
- global: Digunakan di dalam fungsi jika kamu ingin mengubah nilai variabel yang berada di area global.
- nonlocal: Digunakan di dalam fungsi bersarang (nested function) untuk mengubah nilai variabel dari fungsi induknya (area enclosed).
---
cara cepat menguji kode tanpa keluar dari interpreter menggunakan fungsi reload(). 
import importlib memiliki fungsi reload() dan import file yang ingin di test

contoh
```python
import importlib
import filetest

for i in range(5)
    importlib.reload(filetest)
    input("klik apapun untuk lanjut...")

#buat perubahan pada filetest sebelum klik

```
