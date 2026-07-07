Fondasi & Esensi Software Testing

## 1. Mengapa Testing Penting? (Dampak Bisnis)
*   **Aplikasi Rusak = Kehilangan Pengguna:** Di era internet, pengguna sangat sensitif terhadap *bug*. Jika produk gagal di awal (misal: *crash* saat viral atau validasi formulir perbankan salah), pengguna akan langsung pindah ke kompetitor.
*   **Manfaat Utama:**
    *   Mendeteksi desain buruk & alur kerja yang tidak efisien.
    *   Mengatasi masalah skala besar (*scalability*) & celah keamanan (*security vulnerabilities*).
    *   Memungkinkan pengujian opsi terbaik (**A/B testing**).
    *   Menjamin kecocokan di berbagai perangkat (**compatibility**).

---

## 2. Definisi & Evolusi Paradigma
*   **Definisi:** Proses mengevaluasi produk untuk memastikan **performa, kebenaran, dan kelengkapan** sesuai dengan ekspektasi, serta menemukan *bug* atau kebutuhan yang terlewat.
*   **Evolusi:** 
    *   *Dulu (Pre-1980s):* Fokus pada *debugging* (hanya membuang error) dan dilakukan di tahap akhir pengembangan.
    *   *Sekarang:* Diintegrasikan sejak **tahap awal** pengembangan.
*   **Prinsip Efisiensi:** Tulis **tes seminimal mungkin** untuk menemukan **cacat sebanyak mungkin**.

---

## 3. Praktik Terbaik & Karakteristik Test Case
*   **Praktik Terbaik Pengujian:** Harus bisa digunakan kembali (*reusable*), dapat dilacak ke dokumen kebutuhan (*traceable to requirements*), memiliki tujuan jelas (*purpose-driven*), efisien, dan bisa diulang (*repeatable*).
*   **Anatomi Test Case:** Kumpulan tindakan yang berisi **langkah-langkah, data, serta kondisi sebelum (pre) dan sesudah (post) pengujian**. 

---

## 4. Siklus Hidup Testing (Testing Lifecycle)
Prosedur pengujian secara umum dibagi menjadi 4 tahap utama:
1.  **Planning (Perencanaan):** Strategi dan penentuan objek uji.
2.  **Preparation (Persiapan):** Menulis skrip dan pembuatan *test cases*.
3.  **Execution (Eksekusi):** Menjalankan pengujian dan kompilasi hasil.
4.  **Reporting (Pelaporan):** Memperbaiki cacat dan membuat laporan hasil akhir.

---

## 5. Kategori & Jenis Testing
*Tidak ada solusi satu ukuran untuk semua (No one-size-fits-all).* Pengujian *game* Android berbeda dengan web finansial.
*   **Berdasarkan Akses Kode Internal:**
    *   **Black Box Testing:** Menguji dari luar tanpa tahu kode di dalamnya.
    *   **White Box Testing:** Menguji dengan melihat struktur kode dan logika internal.
*   **Jenis Lain yang Sering Digunakan:** *Compatibility, Ad hoc, Usability,* dan *Regression testing*.

---

## 6. Kapan Harus Berhenti Testing?
**Fakta:** Tidak ada aplikasi yang 100% sempurna dari *bug*. Jangan mengejar kesempurnaan mutlak, melainkan gunakan **Metrik Keluar (Exit Criteria)** ini:
*   Jumlah siklus testing (*test cycles*) yang direncanakan selesai.
*   Persentase kelulusan *test case* mencapai target tertentu.
*   Tenggat waktu (*time deadline*) proyek.
*   Jeda waktu antar-kegagalan (*time intervals between failures*) semakin lebar/jarang.

> **Analogi Akhir:** Testing berfungsi seperti **jangkar kapal** atau **asuransi kendaraan**. Kita berharap semuanya mulus, tetapi testing ada sebagai pengaman dari potensi *human error*.
