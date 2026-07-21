## 1. PERINTAH DASAR TERMINAL LINUX (UBUNTU)

### Manajemen Direktori & Navigasi
`pwd`
* **pwd** *(print working directory)* = Perintah untuk menampilkan jalur (path) absolut dari lokasi folder tempat kita berada saat ini.

`mkdir proyek-web`
* **mkdir** *(make directory)* = Perintah membuat folder baru.
* **proyek-web** = Nama folder baru yang ingin dibuat.

`cd proyek-web`
* **cd** *(change directory)* = Perintah untuk berpindah atau masuk ke folder lain.
* **proyek-web** = Nama folder tujuan yang ingin dimasuki.

`ls`
* **ls** *(list)* = Perintah untuk menampilkan daftar semua file dan folder di lokasi saat ini.

`ls -la`
* **ls** = Menampilkan daftar file.
* **-la** *(long & all)* = Opsi tambahan untuk menampilkan file secara detail (ukuran, hak akses) termasuk file tersembunyi yang diawali dengan tanda titik (seperti `.git`).

### Manajemen File (Membuat, Menyalin, Memindah, & Menghapus)
`touch belajar.txt`
* **touch** = Perintah untuk membuat file baru dalam keadaan kosong tanpa membuka text editor.
* **belajar.txt** = Nama file baru beserta ekstensinya yang ingin dibuat.

`cp belajar.txt salinan.txt`
* **cp** *(copy)* = Perintah untuk menyalin file atau folder.
* **belajar.txt** = File sumber yang ingin disalin.
* **salinan.txt** = Nama file baru hasil salinan.

`cp -r folder-lama folder-baru`
* **cp** = Perintah menyalin.
* **-r** *(recursive)* = Opsi wajib untuk menyalin folder beserta seluruh isi di dalamnya.

`mv belajar.txt dokumentasi/`
* **mv** *(move)* = Perintah untuk memindahkan file atau folder ke lokasi lain, atau bisa digunakan untuk mengubah nama (rename) file jika tujuan pemindahannya berada di folder yang sama dengan nama berbeda.
* **belajar.txt** = Nama file yang ingin dipindahkan/diubah namanya.
* **dokumentasi/** = Folder tujuan pemindahan.

`rm belajar.txt`
* **rm** *(remove)* = Perintah untuk menghapus file secara permanen.
* **belajar.txt** = Nama file yang ingin dihapus.

`rm -rf folder-sampah`
* **rm** = Perintah menghapus.
* **-rf** *(recursive & force)* = Opsi ekstrem untuk menghapus folder beserta seluruh isinya secara paksa tanpa konfirmasi.

### Manipulasi & Membaca Isi File
`echo "<h1>Halo</h1>" > index.html`
* **echo** = Perintah untuk menuliskan atau menampilkan teks ke layar terminal atau dialihkan ke file.
* **"<h1>Halo</h1>"** = Teks isi yang ingin dimasukkan ke dalam file.
* **>** *(Redirect Overwrite)* = Tanda untuk memasukkan teks sekaligus menghapus isi lama file tersebut jika file sudah ada.
* **index.html** = Nama file tujuan yang dibuat/ditimpa.

`echo "Baris Baru" >> index.html`
* **echo** = Perintah untuk menuliskan teks.
* **"Baris Baru"** = Teks tambahan yang ingin ditaruh di baris paling bawah.
* **>>** *(Redirect Append)* = Tanda untuk menyisipkan teks baru tanpa merusak isi lama file.
* **index.html** = Nama file yang ingin ditambahkan teksnya.

`cat index.html`
* **cat** *(concatenate)* = Perintah untuk membaca dan menampilkan seluruh isi file ke layar terminal tanpa perlu membuka text editor.
* **index.html** = Nama file yang ingin dilihat isinya.

### Utilitas Sistem
`clear`
* **clear** = Perintah untuk membersihkan layar terminal agar rapi kembali dari perintah-perintah sebelumnya.

`sudo apt update`
* **sudo** *(superuser do)* = Menjalankan perintah dengan hak akses administrator tertinggi (root).
* **apt update** = Perintah pada Ubuntu untuk memperbarui daftar paket/aplikasi dari repositori internet agar sistem mengetahui versi terbaru.

---

## 2. ALUR UTAMA MENGHUBUNGKAN & MENGUNGGAH PROYEK BARU KE GITHUB



`git init`
* **git** = Memanggil program Git di komputer.
* **init** *(initialize)* = Membuka ruang kerja baru agar folder tersebut mulai diawasi oleh sistem Version Control Git.

`git branch -m main`
* **git** = Memanggil program Git.
* **branch** = Perintah untuk mengelola cabang/alur kerja proyek.
* **-m** *(move)* = Opsi untuk mengubah nama cabang yang sedang aktif saat ini.
* **main** = Nama baru yang dipilih untuk menggantikan nama default lama (master).

`git config --global init.defaultBranch main`
* **git config** = Perintah untuk mengubah pengaturan bawaan Git.
* **--global** = Mengatur agar aturan ini berlaku untuk semua proyek masa depan di komputer ini.
* **init.defaultBranch** = Target pengaturan, yaitu mendefinisikan nama branch utama setiap kali membuat proyek baru secara otomatis.
* **main** = Nama branch standar yang dipilih.

`git remote add origin https://github.com/username/repository.git`
* **git** = Memanggil program Git.
* **remote** = Perintah untuk mengatur hubungan jarak jauh antara komputer lokal dan internet.
* **add** = Perintah untuk menambah koneksi baru.
* **origin** = Nama panggilan buatan untuk URL GitHub agar Anda tidak perlu mengetik URL panjang nantinya saat push/pull.
* **https://...** = Alamat URL repositori kosong yang Anda buat di website GitHub.

`git status`
* **git** = Memanggil program Git.
* **status** = Memeriksa kondisi folder saat ini (melihat mana file yang baru dibuat, dimodifikasi, atau siap dikunci ke Staging Area).

`git add index.html`
* **git** = Memanggil program Git.
* **add** = Memasukkan file ke antrean kerja sebelum disimpan (*Staging Area*). Di terminal, warna file akan berubah dari merah menjadi hijau.
* **index.html** = Nama file spesifik yang ingin dimasukkan ke antrean hijau.

`git add .`
* **git add** = Memasukkan file ke antrean kerja (*Staging Area*).
* **.** *(titik)* = Simbol universal yang artinya "Semua file dan folder yang ada di lokasi saat ini tanpa terkecuali".

`git commit -m "Pesan"`
* **git** = Memanggil program Git.
* **commit** = Perintah untuk mengunci dan menyimpan permanen perubahan lokal ke dalam catatan sejarah Git (*Local Repository*).
* **-m** *(message)* = Opsi wajib untuk memberikan catatan atau deskripsi singkat mengenai commit tersebut.
* **"Pesan"** = Kalimat penjelasan bebas tentang apa yang Anda ubah atau tambahkan di commit tersebut (contoh: "Fitur: Tambah halaman login").

`git push -u origin main`
* **git** = Memanggil program Git.
* **push** = Mengunggah atau mendorong catatan sejarah dari komputer lokal ke server internet (*GitHub*).
* **-u** *(upstream)* = Digunakan 1x di awal untuk mengunci hubungan permanen antara branch lokal dan GitHub.
* **origin** = Nama panggilan URL GitHub tujuan yang sudah didaftarkan sebelumnya.
* **main** = Nama branch tujuan di GitHub tempat Anda ingin menyimpan file tersebut.

---

## 3. SINKRONISASI, MENGUNDUH & MEMPERBARUI FILE

`git clone https://github.com/username/repository.git`
* **git** = Memanggil program Git.
* **clone** = Menyalin total sebuah repositori utuh dari GitHub beserta seluruh sejarah commit-nya ke dalam komputer lokal Anda.
* **https://...** = URL repositori GitHub yang ingin disalin.

`git pull origin main --rebase`
* **git** = Memanggil program Git.
* **pull** = Menarik atau mengambil file serta catatan terbaru dari GitHub ke komputer lokal Anda agar sinkron.
* **origin** = Nama panggilan server GitHub tujuan.
* **main** = Nama branch di GitHub yang ingin ditarik datanya.
* **--rebase** = Aturan khusus agar catatan sejarah komputer lokal Anda disusun rapi tepat di atas catatan terbaru dari GitHub, menghindari munculnya commit merge otomatis yang berantakan.

---

## 4. MEMBATALKAN PERUBAHAN & MENGHAPUS FILE

`git restore --staged testemail.txt`
* **git** = Memanggil program Git.
* **restore** = Memulihkan atau mengembalikan kondisi file ke posisi sebelumnya.
* **--staged** = Target pemulihan, yaitu mengeluarkan file dari antrean hijau (*Staging Area*) kembali ke antrean merah biasa (*Working Directory*).
* **testemail.txt** = Nama file yang ingin dikeluarkan dari antrean hijau.

`git rm -f testemail.txt`
* **git** = Memanggil program Git.
* **rm** *(remove)* = Perintah untuk menghapus file dari pengawasan Git.
* **-f** *(force)* = Memaksa penghapusan secara total karena file tersebut sedang tersangkut atau dimodifikasi di antrean hijau.
* **testemail.txt** = Nama file yang akan dihapus dari Git sekaligus lenyap secara fisik dari File Manager komputer Anda.

`git rm --cached testemail.txt`
* **git** = Memanggil program Git.
* **rm** *(remove)* = Perintah untuk menghapus file.
* **--cached** = Aturan khusus agar file hanya dihapus dari pelacakan Git dan web GitHub, tetapi file fisiknya TETAP AMAN di penyimpanan lokal laptop Anda (biasanya digunakan jika lupa memasukkan file ke `.gitignore`).
* **testemail.txt** = Nama file yang ingin dihapus pelacakannya di internet saja.

---

## 5. MENGHAPUS SEJARAH COMMIT (MENGHILANGKAN KOTAK HIJAU GITHUB)

`git reset --hard HEAD~1`
* **git** = Memanggil program Git.
* **reset** = Mengatur ulang atau memundurkan mesin waktu catatan sejarah proyek.
* **--hard** = Pilihan ekstrem: menghapus catatan commit terakhir DAN menghapus seluruh perubahan file fisik di komputer Anda secara permanen. File kembali persis seperti pada posisi commit sebelumnya.
* **HEAD** = Penanda posisi commit aktif saat ini (Wajib ditulis dengan huruf kapital di Linux).
* **~1** = Jumlah langkah kemunduran yang diinginkan (mundur sebanyak 1 commit ke belakang).

`git reset --soft HEAD~1`
* **git** = Memanggil program Git.
* **reset** = Mengatur ulang atau memundurkan catatan sejarah proyek.
* **--soft** = Pilihan aman: menghapus catatan commit terakhir (mengurangi kontribusi/kotak hijau), TAPI FILE FISIK HASIL KODINGAN DI LAPTOP TETAP UTUH dan masuk kembali ke status *Staging Area* (hijau).
* **HEAD~1** = Mundur sebanyak 1 commit dari posisi terakhir saat ini.

`git push origin main --force`
* **git push origin main** = Mengirimkan perubahan ke branch main di internet.
* **--force** *(atau -f)* = Memaksa server GitHub untuk menerima, menimpa, dan menghapus catatan lamanya di internet dengan catatan baru dari komputer Anda yang sudah dimundurkan penanggalannya. Digunakan untuk menghapus kesalahan kontribusi/kotak hijau yang keliru.

---

## 6. MELIHAT CATATAN SEJARAH (HISTORY LOG)

`git log`
* **git** = Menanggil program Git.
* **log** = Menampilkan riwayat catatan seluruh commit secara lengkap, detail, dan berurutan (mencakup ID commit, nama pembuat, email, tanggal, jam, beserta pesan deskripsinya).

`git log --oneline`
* **git log** = Menampilkan catatan riwayat commit.
* **--oneline** = Opsi untuk menyederhanakan tampilan riwayat agar ringkas menjadi hanya 1 baris pendek per commit (hanya menampilkan 7 karakter pertama ID commit dan pesan commit). Sangat membantu saat melacak sejarah proyek yang sudah besar.
