# 1. Implementasi kelas Mahasiswa, Jurusan, dan Universitas

# Kelas Mahasiswa
class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
    
    def tampilkan_info(self):
        print("Nama: ", self.nama)
        print("NIM: ", self.nim)
        print("Jurusan: ", self.jurusan.NamaJurusan)

# Kelas Jurusan
class Jurusan:
    def __init__(self, nama_jurusan):
        self.NamaJurusan = nama_jurusan
        self.DaftarMahasiswa = []
    
    def add_mahasiswa(self, mahasiswa):
        self.DaftarMahasiswa.append(mahasiswa)
    
    def show_daftar_mahasiswa(self):
        print("Daftar Mahasiswa di Jurusan", self.NamaJurusan)
        for mahasiswa in self.DaftarMahasiswa:
            print("Nama: ", mahasiswa.nama)
            print("NIM: ", mahasiswa.nim)
            print("--------------------")

# Kelas Universitas
class Universitas:
    def __init__(self, nama_universitas):
        self.NamaUniversitas = nama_universitas
        self.DaftarJurusan = []
    
    def add_jurusan(self, jurusan):
        self.DaftarJurusan.append(jurusan)
    
    def show_daftar_jurusan(self):
        print("Daftar Jurusan di Universitas", self.NamaUniversitas)
        for jurusan in self.DaftarJurusan:
            print(jurusan.NamaJurusan)
            print("--------------------")


# 2. Membuat objek Universitas dengan nama "XYZ University"
universitas_xyz = Universitas("XYZ University")

# 3. Membuat objek Jurusan dengan nama "Teknik Informatika" dan menambahkannya ke dalam Universitas XYZ
jurusan_ti = Jurusan("Teknik Informatika")
universitas_xyz.add_jurusan(jurusan_ti)

# 4. Membuat objek Mahasiswa dengan nama dan NIM masing-masing, dan memasukkannya ke dalam Jurusan Teknik Informatika di Universitas XYZ
mahasiswa1 = Mahasiswa("Saniyyah Zhafirah", "G1A022081", jurusan_ti)
jurusan_ti.add_mahasiswa(mahasiswa1)

# 5. Menampilkan daftar jurusan yang ada di Universitas XYZ
universitas_xyz.show_daftar_jurusan()

# 6. Menampilkan daftar mahasiswa yang terdaftar dalam Jurusan Teknik Informatika di Universitas XYZ
jurusan_ti.show_daftar_mahasiswa()
