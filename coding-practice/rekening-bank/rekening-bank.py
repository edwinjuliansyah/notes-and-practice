class Nasabah:
    def __init__ (self, nama):
        self.nama = nama
        self.daftar_rekening = []

    def __str__(self):
        return f"{self.nama}"

    def tambah_rekening(self, jenis_rekening):
        self.daftar_rekening.append(jenis_rekening)

    def tampilkan_daftar_rekening(self):
        print(f"\n{self.nama} kamu memiliki rekening:")
        for rekening in self.daftar_rekening:
            print(rekening)

class Rekening:
    def __init__ (self, nomor_rekening, nasabah: 'Nasabah'):
        self.nomor_rekening = nomor_rekening
        self.nasabah = nasabah
        self.__saldo = 0
        self.riwayat = []
        nasabah.tambah_rekening(self)

    def __str__(self):
        jenis = type(self).__name__
        return f"{jenis} No. {self.nomor_rekening} a.n. {self.nasabah} (Saldo: Rp{self.saldo:,})"

    def tambah_saldo(self, input_nominal):
        self.__saldo += input_nominal

    def _konfirmasi(self, input_nominal):
        while True:
            jawaban = input(f"Anda telah memasukkan nominal sebesar {input_nominal}\nApakah benar? y/n: ").strip().lower()
           
            if jawaban == "y":
                return True
            elif jawaban == "n":
                return False
            else:
                print("Pastikan ketik y/n\n")
                continue

    def logic_tambah_saldo(self, input_nominal):
        if self._konfirmasi(input_nominal):
            self.tambah_saldo(input_nominal)
            return True
        return False

    def setor(self):
        while True:
            try:
                input_nominal = int(input("Masukkan nominal uang setor: ").strip())                
               
                if input_nominal < 1:
                    print("input tidak boleh kurang dari 1")
                    continue
                else:
                    berhasil = self.logic_tambah_saldo(input_nominal)
                    if berhasil:                
                        break
           
            except ValueError:
                print("Input hanya boleh angka")
                continue

        self.riwayat.append(f"Setor tunai sebanyak +{input_nominal}")    
        print(f"Saldo sebesar {input_nominal} telah ditambahkan ke rekening.\nSaldo saat ini {self.__saldo}\n")

    def logic_kurangi_saldo(self, input_nominal):
        if self._konfirmasi(input_nominal):
            if input_nominal > self.__saldo:
                print("Saldo tidak cukup")
                return False
            self.__saldo -= input_nominal
            return True
        return False

    def tarik(self):
        while True:
            try:
                input_nominal = int(input("Masukkan nominal uang penarikan: ").strip())
                
                if input_nominal < 1:
                    print("input tidak boleh kurang dari 1")
                    continue
                else:
                    berhasil = self.logic_kurangi_saldo(input_nominal)
                    if berhasil:
                        break            
            
            except ValueError:
                print("Input hanya boleh angka")
                continue
        
        self.riwayat.append(f"Tarik tunai -{input_nominal}")
        print(f"Sisa saldo {self.__saldo}\n")
        
    def transfer(self, rekening_tujuan: 'Rekening'):
        while True:
            try:
                input_nominal = int(input("Masukkkan nominal transfer: "))

                if input_nominal < 1:
                        print("input tidak boleh kurang dari 1")
                        continue
                    
                berhasil = self.logic_kurangi_saldo(input_nominal)

                if berhasil:
                    rekening_tujuan.tambah_saldo(input_nominal)
                    self.riwayat.append(f"Transfer keluar -{input_nominal} ke rekening {rekening_tujuan.nomor_rekening}")
                    rekening_tujuan.riwayat.append(f"Transfer masuk +{input_nominal} dari rekening {self.nomor_rekening}")
                    print(f"Sisa saldo: {self.saldo}")
                    break
                else:
                    print("Transfer gagal")
                    continue

            except ValueError:
                print("Input hanya boleh angka")
                continue
                
    def tampilkan_riwayat(self):
        print(f"Riwayat {type(self).__name__} kamu:")
        for i in self.riwayat:
            print(i)
    
    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, nilai):
        if nilai < 0:
            print("saldo tidak boleh minus")
            return
        self.__saldo = nilai    
    
class Britama(Rekening):
    def __init__(self, nomor_rekening, nasabah):
        super().__init__(nomor_rekening, nasabah)
        self.limit_harian = 20_000_000
        self.biaya_admin_bulanan = 15_000
        self.akses_internasional = True

    def logic_kurangi_saldo(self, input_nominal):
        if input_nominal > self.limit_harian:
            print(f"Melebihi limit harian Rp{self.limit_harian}")
            return False
        return super().logic_kurangi_saldo(input_nominal)

class Simpedes(Rekening):
    def __init__(self, nomor_rekening, nasabah):
        super().__init__(nomor_rekening, nasabah)
        self.limit_harian = 5_000_000
        self.biaya_admin_bulanan = 5_000
        self.akses_internasional = False

    def logic_kurangi_saldo(self, input_nominal):
        if input_nominal > self.limit_harian:
            print(f"Melebihi limit harian Rp{self.limit_harian}")
            return False
        return super().logic_kurangi_saldo(input_nominal)
    

riko = Nasabah('Riko')
riko_britama = Britama(123, riko)
riko_simpedes = Simpedes(456, riko)


danang = Nasabah('Danang')
danang_britama = Britama(789, danang)

riko_britama.setor()
riko_britama.transfer(danang_britama)
riko_britama.transfer(riko_simpedes)

danang_britama.tarik()

riko.tampilkan_daftar_rekening()
riko_britama.tampilkan_riwayat()
riko_simpedes.tampilkan_riwayat()

danang.tampilkan_daftar_rekening()
danang_britama.tampilkan_riwayat()
