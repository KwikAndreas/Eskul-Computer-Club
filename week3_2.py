# ========================================
# MINGGU 3 - SESI 2: FUNCTION (FUNGSI)
# Durasi: 30 menit
# ========================================

print("Selamat datang di sesi terakhir!")
print("Hari ini kita akan belajar tentang Function (Fungsi)")

print("\n=== Apa itu Function? ===")
print("Function adalah 'mesin' yang menerima input dan menghasilkan output")
print("Seperti mesin kalkulator: masukkan angka, keluar hasil")

print("\n" + "="*40)
print("CONTOH 1: FUNCTION SEDERHANA")
print("="*40)

# Membuat function pertama
def sapa_teman():
    print("Halo! Selamat belajar Python!")

# Memanggil function
print("Memanggil function sapa_teman():")
sapa_teman()

print("\n" + "="*40)
print("CONTOH 2: FUNCTION DENGAN PARAMETER")
print("="*40)

def sapa_dengan_nama(nama):
    print(f"Halo {nama}! Semoga harimu menyenangkan!")

# Memanggil function dengan parameter
nama_siswa = input("Masukkan nama kamu: ")
sapa_dengan_nama(nama_siswa)

print("\n" + "="*40)
print("CONTOH 3: FUNCTION YANG MENGEMBALIKAN NILAI")
print("="*40)

def hitung_luas_persegi(sisi):
    luas = sisi * sisi
    return luas

def hitung_keliling_persegi(sisi):
    keliling = sisi * 4
    return keliling

# Menggunakan function
panjang_sisi = int(input("Masukkan panjang sisi persegi: "))
luas_hasil = hitung_luas_persegi(panjang_sisi)
keliling_hasil = hitung_keliling_persegi(panjang_sisi)

print(f"Luas persegi: {luas_hasil}")
print(f"Keliling persegi: {keliling_hasil}")

print("\n" + "="*40)
print("CONTOH 4: FUNCTION DENGAN MULTIPLE PARAMETER")
print("="*40)

def hitung_rata_rata(nilai1, nilai2, nilai3):
    total = nilai1 + nilai2 + nilai3
    rata_rata = total / 3
    return rata_rata

def tentukan_grade(nilai):
    if nilai >= 90:
        return "A"
    elif nilai >= 80:
        return "B"
    elif nilai >= 70:
        return "C"
    else:
        return "D"

# Input nilai
print("Masukkan 3 nilai ujian:")
n1 = int(input("Nilai 1: "))
n2 = int(input("Nilai 2: "))
n3 = int(input("Nilai 3: "))

# Hitung rata-rata dan tentukan grade
rata = hitung_rata_rata(n1, n2, n3)
grade = tentukan_grade(rata)

print(f"Rata-rata: {rata:.1f}")
print(f"Grade: {grade}")

print("\n" + "="*40)
print("LATIHAN: KALKULATOR SEDERHANA")
print("="*40)

def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: tidak bisa bagi dengan 0"

# Menu kalkulator
print("=== KALKULATOR SEDERHANA ===")
angka1 = float(input("Masukkan angka pertama: "))
operasi = input("Pilih operasi (+, -, *, /): ")
angka2 = float(input("Masukkan angka kedua: "))

if operasi == "+":
    hasil = tambah(angka1, angka2)
elif operasi == "-":
    hasil = kurang(angka1, angka2)
elif operasi == "*":
    hasil = kali(angka1, angka2)
elif operasi == "/":
    hasil = bagi(angka1, angka2)
else:
    hasil = "Operasi tidak valid"

print(f"Hasil: {angka1} {operasi} {angka2} = {hasil}")

print("\n" + "="*40)
print("LATIHAN: FUNCTION UNTUK LIST")
print("="*40)

def cari_nilai_tertinggi(daftar_nilai):
    return max(daftar_nilai)

def hitung_jumlah_lulus(daftar_nilai, batas_lulus=70):
    jumlah_lulus = 0
    for nilai in daftar_nilai:
        if nilai >= batas_lulus:
            jumlah_lulus += 1
    return jumlah_lulus

# Test dengan data nilai
nilai_kelas = [85, 92, 67, 78, 95, 82, 74, 88]
print(f"Nilai kelas: {nilai_kelas}")
print(f"Nilai tertinggi: {cari_nilai_tertinggi(nilai_kelas)}")
print(f"Jumlah yang lulus: {hitung_jumlah_lulus(nilai_kelas)}")

print("\n📝 TUGAS UNTUK KAMU:")
print("1. Buat function untuk menghitung luas lingkaran")
print("2. Buat function untuk mengecek apakah angka genap atau ganjil")
print("3. Buat function untuk mencari nama terpanjang dalam list")

# Area untuk siswa berlatih:
# def luas_lingkaran(jari_jari):
#     pi = 3.14159
#     return pi * jari_jari * jari_jari
#
# def cek_genap_ganjil(angka):
#     if angka % 2 == 0:
#         return "genap"
#     else:
#         return "ganjil"

print("\n🎉 SELAMAT!")
print("Kamu sudah menyelesaikan pembelajaran dasar Python!")
print("Sekarang kamu sudah bisa:")
print("- Menggunakan print() dan input()")
print("- Membuat variabel dan memahami tipe data")
print("- Menggunakan kondisi (if, elif, else)")
print("- Membuat perulangan (for, while)")
print("- Bekerja dengan list dan tuple")
print("- Membuat dan menggunakan function")
print("\nTerus berlatih dan selamat coding! 🐍✨")
