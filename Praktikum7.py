class mahasiswa:
    def __init__(self):
        self.data_mahasiswa = {}
    
    def tambah(self):
        print("\n" + "=" * 40)
        print("TAMBAH DATA MAHASISWA".center(40))
        print("=" * 40)
        
        nama = input("Masukkan Nama: ").title()
        
        if nama in self.data_mahasiswa:
            print(f"Mahasiswa dengan nama '{nama}' sudah ada!")
            ulangi = input("Apakah Anda ingin mengupdate data? (y/n): ").lower()
            if ulangi == 'y':
                return self.ubah(nama)
            return
        
        try:
            nilai = float(input("Masukkan Nilai: "))
        except ValueError:
            print("Nilai harus berupa angka!")
            return
        
        self.data_mahasiswa[nama] = nilai
        print(f"Data mahasiswa '{nama}' dengan nilai {nilai} berhasil ditambahkan!")
    
    def tampilkan(self):
        print("\n" + "=" * 50)
        print("DAFTAR NILAI MAHASISWA".center(50))
        print("=" * 50)
        
        if not self.data_mahasiswa:
            print("Belum ada data mahasiswa.")
            return
        
        print("-" * 50)
        print(f"{'No':<5} {'Nama':<25} {'Nilai':<10}")
        print("-" * 50)
        
        for i, (nama, nilai) in enumerate(self.data_mahasiswa.items(), 1):
            print(f"{i:<5} {nama:<25} {nilai:<10.2f}")
        
        print("-" * 50)
        print(f"Total Mahasiswa: {len(self.data_mahasiswa)}")
    
    def hapus(self, nama):
        nama = nama.title()
        
        if nama in self.data_mahasiswa:
            nilai = self.data_mahasiswa.pop(nama)
            print(f"Data mahasiswa '{nama}' dengan nilai {nilai} berhasil dihapus!")
            return True
        else:
            print(f"Mahasiswa dengan nama '{nama}' tidak ditemukan!")
            return False
    
    def ubah(self, nama=None):
        if nama is None:
            print("\n" + "=" * 40)
            print("UBAH DATA MAHASISWA".center(40))
            print("=" * 40)
            nama = input("Masukkan Nama yang akan diubah: ").title()
        
        nama = nama.title()
        
        if nama in self.data_mahasiswa:
            nilai_lama = self.data_mahasiswa[nama]
            print(f"Data saat ini: {nama} - Nilai: {nilai_lama}")
            
            try:
                nilai_baru = float(input("Masukkan Nilai Baru: "))
            except ValueError:
                print("Nilai harus berupa angka!")
                return False
            
            self.data_mahasiswa[nama] = nilai_baru
            print(f"Data mahasiswa '{nama}' berhasil diubah dari {nilai_lama} menjadi {nilai_baru}!")
            return True
        else:
            print(f"Mahasiswa dengan nama '{nama}' tidak ditemukan!")
            return False


def main():
    mhs = mahasiswa()
    
    while True:
        print("\n" + "=" * 40)
        print("SISTEM MANAJEMEN NILAI MAHASISWA".center(40))
        print("=" * 40)
        print("1. Tambah Data")
        print("2. Tampilkan Data")
        print("3. Hapus Data")
        print("4. Ubah Data")
        print("5. Keluar")
        print("=" * 40)
        
        try:
            pilihan = int(input("Masukkan pilihan (1-5): "))
        except ValueError:
            print("Masukkan angka antara 1-5!")
            continue
        
        if pilihan == 1:
            mhs.tambah()
        elif pilihan == 2:
            mhs.tampilkan()
        elif pilihan == 3:
            print("\n" + "=" * 40)
            print("HAPUS DATA MAHASISWA".center(40))
            print("=" * 40)
            nama = input("Masukkan Nama yang akan dihapus: ")
            mhs.hapus(nama)
        elif pilihan == 4:
            mhs.ubah()
        elif pilihan == 5:
            print("Terima kasih telah menggunakan program!")
            break
        else:
            print("Pilihan tidak valid! Masukkan angka 1-5.")


if __name__ == "__main__":
    main()