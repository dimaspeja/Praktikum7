# Penjelasan Program Sistem Manajemen Nilai Mahasiswa
Program ini adalah aplikasi sederhana berbasis Python yang memanfaatkan class (OOP) untuk mengelola data nilai mahasiswa. Data mahasiswa disimpan dalam bentuk dictionary, dengan nama sebagai key dan nilai sebagai value.

Program ini memiliki fitur:

- Menambah data mahasiswa
- Menampilkan seluruh data
- Menghapus data berdasarkan nama
- Mengubah data berdasarkan nama
- Menu interaktif untuk memudahkan pengguna

## Penjelasan Bagian-Bagian Program
### 1. Class mahasiswa
Class ini berisi semua method untuk mengelola data mahasiswa.
#### a. __init__(self)
```python
def __init__(self):
    self.data_mahasiswa = {}
```
- Membuat dictionary kosong bernama data_mahasiswa.
- Dictionary ini digunakan untuk menyimpan data mahasiswa dalam format:
```python
{"Nama": nilai}
```
### 2. Method tambah(self)
Method ini digunakan untuk menambahkan data baru.

Fitur method:
- Menampilkan form input nama dan nilai.
- Mengecek apakah nama sudah ada dalam data.
- Jika sudah ada → tanya apakah ingin mengupdate datanya.
- Validasi agar nilai harus berupa angka.

Contoh penyimpanan:
```python
data_mahasiswa["Dimas"] = 85.0
```
### 3. Method tampilkan(self)
Method untuk menampilkan seluruh data mahasiswa dalam bentuk tabel.

Fitur:
- Menampilkan header dan garis pembatas.
- Menampilkan daftar mahasiswa dengan format:
```python
No | Nama | Nilai
```
- Jika data kosong → tampilkan pesan "Belum ada data mahasiswa".
### 4. Method hapus(self, nama)
Menghapus data berdasarkan nama.

Fitur:
-Mengubah nama menjadi Title Case (.title()).
-Mengecek apakah nama ada dalam dictionary.
-Jika ada → hapus data dan menampilkan nilai yang terhapus.
-Jika tidak ditemukan → menampilkan pesan error.

Contoh:
```python
mhs.hapus("Dimas")
```
### 5. Method ubah(self, nama=None)
Digunakan untuk mengubah nilai mahasiswa.

Fitur:
-Jika nama tidak diberikan saat pemanggilan, maka user diminta memasukkan nama.
-Validasi apakah nama ada dalam data.
-Menampilkan data lama sebelum diubah.
-Menginput nilai baru dan memperbarui data.

Contoh output:
```python
Data mahasiswa 'Dimas' berhasil diubah dari 85 menjadi 90!
```
### 6. Fungsi main()
Merupakan fungsi utama yang menjalankan menu program.

Isi menu:
```python
1. Tambah Data
2. Tampilkan Data
3. Hapus Data
4. Ubah Data
5. Keluar
```
Fitur:
-Pengguna wajib memasukkan angka 1–5.
-Jika salah input, ditampilkan pesan error.
-Memanggil method sesuai pilihan user.

Contoh:
```python
if pilihan == 1:
    mhs.tambah()
```
### 7. Blok Eksekusi Program
```python
if __name__ == "__main__":
    main()
```
Digunakan agar program hanya berjalan ketika file dijalankan secara langsung, bukan ketika di-import.
## Alur Kerja Program
1. Sistem membuat objek class mahasiswa
2. Program menampilkan menu utama
3. Pengguna memilih menu
4. Program memanggil method sesuai pilihan (tambah, tampilkan, hapus, ubah)
5. Program berjalan terus sampai user memilih opsi Keluar
