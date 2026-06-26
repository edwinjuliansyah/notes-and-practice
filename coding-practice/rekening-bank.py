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
    
    def setor(self):
        while True:
            try:
                input_nominal = int(input("Masukkan nominal uang setor: ").strip())                
                if input_nominal < 1:
                    print("input tidak boleh kurang dari 1")
                    continue
                
                while True:
                    konfirmasi = input(f"Anda telah memasukkan nominal sebesar {input_nominal}\nApakah benar? y/n: ").strip().lower()
                    if konfirmasi == "y":
                        self.__saldo += input_nominal
                        break
                    elif konfirmasi == "n":
                        break
                    else:
                        print("Pastikan ketik y/n\n")
                        continue

                if konfirmasi == "n":
                    continue
                break
            except ValueError:
                print("Input hanya boleh angka")
                continue

        self.riwayat.append(f"Setor tunai sebanyak +{input_nominal}")    
        print(f"Saldo sebesar {input_nominal} telah ditambahkan ke rekening.\nSaldo saat ini {self.__saldo}")

    def tarik(self):
        while True:
            try:
                input_nominal = int(input("Masukkan nominal uang penarikan: ").strip())
                if input_nominal < 1:
                    print("input tidak boleh kurang dari 1")
                    continue
                
                while True:
                    konfirmasi = input(f"Anda telah memasukkan nominal sebesar {input_nominal}\nApakah benar? y/n: ").strip().lower()
                    if konfirmasi == "y":
                        if input_nominal > self.__saldo:
                            print("Saldo tidak cukup")
                            continue
                        self.__saldo -= input_nominal
                        break
                    elif konfirmasi == "n":
                        break
                    else:
                        print("Pastikan ketik y/n\n")
                        continue

                if konfirmasi == "n":
                    continue
                break            
            except ValueError:
                print("Input hanya boleh angka")
                continue
        
        self.riwayat.append(f"Tarik tunai -{input_nominal}")
        print(f"Sisa saldo {self.__saldo}")
        
    def transfer(self):
        pass

    def tampilkan_riwayat(self):
        for i in self.riwayat:
            print(i)
    
    @property
    def saldo(self):
        return self.__saldo
    
    # @saldo.setter
    # def saldo
    # if saldo < 1:
        
    
nomor_rekening = int(input("Masukkan nomor rekening anda: "))
running = Rekening(nomor_rekening)
running.setor()
running.tarik()
print(running.saldo)
running.tampilkan_riwayat()
