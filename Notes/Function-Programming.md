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


