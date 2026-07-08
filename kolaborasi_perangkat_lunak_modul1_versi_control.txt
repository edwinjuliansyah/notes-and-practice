# Kontrol versi dalam pengembangan perangkat lunak

## VCS (Version Control System)
Version Control System, sistem mencatat dan melacak setiap perubahan kode yang dibuat tim, sistem isolasi dengan branching, dan sistem kolaborasi dengan aman.

## Method Version Control (CI/CD)

### CI (Continuous Integration)
sistem otomatis yang mengetes setiap ada kode masuk. tujuannya memastikan semua fitur fitur yang ada sebelumnya tidak rusak akibat perubahan ini.

### CD (Continuous Delivery atau Continuous Deployment)
lanjutan dari CI setelah kode di tes, sistem otomatis membungkus dan memastikannya dalam kondisi 100% rilis. 

perbedaannya antara delivery dan deployment:
* **delivery:** membutuhkan acc manual sebelum fitur baru rilis
* **deployment:** langsung rilis secara otomatis

## Jenis Arsitektur

### CVCS (Centralized Version Control System)
model server-client. ibarat seperti membukaa docs dari drive. wajib selalu terhubung kerserver untuk melakukan apapun 

### DVCS (Decentralized Version Control System)
model client menjadi server itu sendiri. melakukan semua pull(mengunduh) dari sever, melakukan semua perubahan secara lokal dan dapat dijalankan secara offline. ibarat seperti mengunduh docs dari drive. cara ini sangan ideal untuk siklus hidup SDLC (software development life cycle)

---

## revision history

* **pelacakan detail:** mengetahui siapa, apa, kapan, dan kenapa melakukan perubahan
* **standar komunikasi:** tetapkan standar tentang bagaimana developer harus menuliskan pesan perubahan atau commit massage
* **alur kerja pull request(pr) dan peer review:** setelah melakukan perubahan, developer akan melakukan push dan membuat pull request. tim lain kemudian akan melakukan peer review untuk menyetujui, menolak, atau melakkukan perubahan sebelum di gabung.
* **merge conflicts:** ketika tidak sengaja melakukan perubahan secara bersamaan, revision history dapat menyelesaikan konflik ini.

---

## staging vs production

**staging** itu environment untuk testing tahap akhir sebelum menuju production yang akan digunakan user dan hal yang dilakukan dalam staging biasanya adalah test fitur baru dengan feature flags, test migrasi data, testing menyeluruh sampai uji beban atau kecepatan, dan configurasi changes test perubahan jika pindah server atau cloud. staging harus dilakukan ditempat yang sama sesuai dengan production agar tidak ada perbedaan diantara untuk menemukan bug

**production** sistem yang sudah jalan untuk digunakan user. jika ada masalah yang lolos dari staging resikonya sangat besar. seperti downtime, vulnerability, dan reputasi

---

## sumber daya tambahan modul 1 

* [Tentang Kontrol Versi](https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control)
* [Manfaat sistem kontrol versi terdistribusi](https://about.gitlab.com/topics/version-control/benefits-distributed-version-control-system/)
* [Apa yang dimaksud dengan Kloning?](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
