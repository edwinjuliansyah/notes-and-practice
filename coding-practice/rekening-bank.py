class Nasabah:
    def __init__ (self, nama):
        self.nama = nama
        self.daftar_rekening = []

    def tambah_rekening(self, jenis_rekening):
        self.daftar_rekening.append(jenis_rekening)

class Rekening:
    def __init__ (self, nomor_rekening):
        self.nomor_rekening = nomor_rekening
        self.__saldo = 0
        self.riwayat = []
    
    def tambah_saldo(self, input_nominal):
        self.__saldo += input_nominal

    def logic_saldo(self, input_nominal):
        while True:
            konfirmasi = input(f"Anda telah memasukkan nominal sebesar {input_nominal}\nApakah benar? y/n: ").strip().lower()
           
            if konfirmasi == "y":
                self.tambah_saldo(input_nominal)
                return True
            elif konfirmasi == "n":
                return False
            else:
                print("Pastikan ketik y/n\n")
                continue

    def setor(self):
        while True:
            try:
                input_nominal = int(input("Masukkan nominal uang setor: ").strip())                
               
                if input_nominal < 1:
                    print("input tidak boleh kurang dari 1")
                    continue
                else:
                    berhasil = self.logic_saldo(input_nominal)
                    if berhasil:                
                        break
           
            except ValueError:
                print("Input hanya boleh angka")
                continue

        self.riwayat.append(f"Setor tunai sebanyak +{input_nominal}")    
        print(f"Saldo sebesar {input_nominal} telah ditambahkan ke rekening.\nSaldo saat ini {self.__saldo}\n")

    def kurangi_saldo(self, input_nominal):
        while True:
            konfirmasi = input(f"Anda telah memasukkan nominal sebesar {input_nominal}\nApakah benar? y/n: ").strip().lower()
            
            if konfirmasi == "y":
                if input_nominal > self.__saldo:
                    print("Saldo tidak cukup")
                    return False
                else:
                    self.__saldo -= input_nominal
                    return True   
            elif konfirmasi == "n":
                return False
            else:
                print("Pastikan ketik y/n\n")
                continue

    def tarik(self):
        while True:
            try:
                input_nominal = int(input("Masukkan nominal uang penarikan: ").strip())
                
                if input_nominal < 1:
                    print("input tidak boleh kurang dari 1")
                    continue
                else:
                    berhasil = self.kurangi_saldo(input_nominal)
                    if berhasil:
                        break            
            
            except ValueError:
                print("Input hanya boleh angka")
                continue
        
        self.riwayat.append(f"Tarik tunai -{input_nominal}")
        print(f"Sisa saldo {self.__saldo}\n")
        
    def transfer(self, rekening_tujuan):
        while True:
            try:
                input_nominal = int(input("Masukkkan nominal transfer: "))

                if input_nominal < 1:
                        print("input tidak boleh kurang dari 1")
                        continue
                    
                berhasil = self.kurangi_saldo(input_nominal)

                if berhasil:
                    rekening_tujuan.tambah_saldo(input_nominal)
                    self.riwayat.append(f"Transfer keluar -{input_nominal} ke rekening {rekening_tujuan.nomor_rekening}")
                    rekening_tujuan.riwayat.append(f"Transfer masuk +{input_nominal} dari rekening {self.nomor_rekening}")
                    print(f"Sisa saldo: {self.saldo}")
                    break
                else:
                    print("Transfer gagal")
                    break

            except ValueError:
                print("Input hanya boleh angka")
                continue
                
    def tampilkan_riwayat(self):
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
    
# nomor_rekening = int(input("Masukkan nomor rekening anda: ").strip())
# running = Rekening(nomor_rekening)
# running.setor()
# running.tarik()
# print(running.saldo)
# rekening_tujuan = int(input("Masukkan nomor Rekening tujuan: ").strip())
# running.transfer(rekening_tujuan)
# running.tampilkan_riwayat()

danang = Rekening(123)
riko = Rekening(456)

danang.setor()
danang.transfer(riko)
danang.tampilkan_riwayat()
riko.tampilkan_riwayat()
