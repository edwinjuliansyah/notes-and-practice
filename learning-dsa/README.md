# Catatan Belajar DSA Pondasi

## 1. Struktur Data Linear (Berurutan)

Cara menyusun data di memori komputer secara berurutan, baris demi baris.

### Array / List
*   **Konsep:** Kotak memori yang berjejer dan setiap kotak punya nomor urut (**Indeks**).
*   **Analogi Nyata:** Daftar menu tetap di warkop. Komputer bisa langsung melompat ke nomor tertentu dengan cepat.

### Linked List (Daftar Berantai)
*   **Konsep:** Kotak data (*node*) yang terpisah di memori, tetapi saling terhubung karena masing-masing memegang "alamat" kotak berikutnya. Sangat fleksibel untuk menambah/menghapus data di tengah.
*   **Analogi Nyata:** Fitur lagu *Next* dan *Previous* di Spotify.

### Stack (Tumpukan)
*   **Konsep:** Aturan **LIFO** (*Last In, First Out*). Data yang terakhir masuk justru menjadi yang pertama keluar.
*   **Analogi Nyata:** Tombol *Undo* (Ctrl+Z) di VS Code atau tumpukan piring.

### Queue (Antrean)
*   **Konsep:** Aturan **FIFO** (*First In, First Out*). Data yang pertama kali datang akan diproses pertama kali.
*   **Analogi Nyata:** Antrean printer atau antrean alokasi orderan penumpang ojol.

---

## 2. Struktur Data Non-Linear (Bercabang/Jaringan)

Digunakan ketika hubungan antar-data tidak bisa digambarkan secara lurus.

### Binary Search Tree (BST)
*   **Konsep:** Struktur pohon hierarki bertingkat. Aturan mainnya: cabang sebelah kiri nilainya selalu lebih kecil, dan cabang kanan selalu lebih besar dari pusatnya. Tujuannya memotong setengah waktu pencarian data.
*   **Analogi Nyata:** Sistem struktur folder di dalam komputer (Drive C -> Folder -> File).

### Graph (Graf)
*   **Konsep:** Jaringan kompleks yang menghubungkan titik-titik (*Vertex*) menggunakan garis (*Edge*). Hubungannya bisa satu arah atau bolak-balik.
*   **Analogi Nyata:** Peta rute jalan raya di Google Maps atau jaringan pertemanan media sosial.

### Hash Table (Dictionary)
*   **Konsep:** Memasangkan data menggunakan *Key* (Kunci) dan *Value* (Nilai) via rumus matematika. Pencarian data bisa langsung ketemu secara instan tanpa menyisir dari awal.
*   **Analogi Nyata:** Mencari nomor HP berdasarkan nama kontak di kontak HP.

---

## 3. Algoritma Fundamental & Paradigma Berpikir

Langkah logis untuk memanipulasi struktur data di atas.

### Searching (Pencarian)
*   **Linear Search:** Mencari satu per satu dari awal (lambat kalau datanya jutaan).
*   **Binary Search:** Langsung membelah data jadi dua di bagian tengah secara terus-menerus (sangat cepat, tapi syaratnya data wajib sudah urut).
*   **Analogi:** Mencari kata di kamus cetak tebal langsung dengan membelah halaman tengah.

### Sorting (Pengurutan)
*   Mengurutkan data acak (Bubble Sort, Merge Sort, Quick Sort).
*   **Analogi:** Fitur filter "Harga Termurah ke Termahal" di e-commerce.

### Paradigma Pemecahan Masalah
*   **Brute Force:** Mencoba semua kemungkinan tanpa taktik (Analogi: Menebak PIN gembok dari 0000 sampai 9999).
*   **Greedy:** Mengambil keputusan terbaik di setiap langkah saat itu juga tanpa mikir masa depan (Analogi: Mesin ATM yang selalu menghabiskan pecahan uang terbesar dulu untuk kembalian).
*   **Divide and Conquer:** Memecah masalah besar menjadi sub-masalah kecil, diselesaikan satu-satu, lalu digabung lagi (Analogi: Penghitungan suara pemilu dari tingkat TPS baru dijumlahkan ke pusat).
*   **Dynamic Programming:** Sifatnya mirip *Divide and Conquer*, tapi punya memori untuk mengingat hasil yang sudah pernah dihitung agar tidak usah menghitung ulang dari nol (Analogi: Aplikasi maps mengingat rute macet harian).

---

## 4. Tolok Ukur Efisiensi (Big O Notation)

*   **Tujuan:** Mengukur seberapa boros atau efisiennya kode yang saya tulis dari segi **Waktu** dan **Memori RAM** seiring bertambahnya jumlah data.
*   **Pola Pikir:** Kode yang berjalan cepat dengan 5 data belum tentu aman saat menangani 10.000.000 data. Big O membantu saya menilai skala kelayakan kode sebelum di-deploy ke server.

---

> **Reminder:** 
> *Jangan dihafal rumusnya! Pahami cara kerja visualnya, bayangkan analogi nyatanya, lalu tulis kodenya pelan-pelan sampai paham.*
