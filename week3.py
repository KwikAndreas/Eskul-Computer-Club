# ========================================
# PERTEMUAN 3: KONDISI DAN PENGAMBILAN KEPUTUSAN
# ========================================

print("Selamat datang di pelajaran ke-3!")
print("Hari ini kita akan belajar tentang kondisi dan pengambilan keputusan")

print("\n=== Apa itu Kondisi? ===")
print("Kondisi membantu program mengambil keputusan")
print("Seperti: 'Jika hujan, maka bawa payung'")

print("\n=== Mari Buat Program Sederhana ===")

# Mengumpulkan data siswa
nama = input("Masukkan nama kamu: ")
umur = int(input("Berapa umur kamu? "))

print(f"\nHalo {nama}!")

# Contoh penggunaan kondisi sederhana
print("\n" + "="*50)
print("CONTOH 1: MENENTUKAN KATEGORI UMUR")
print("="*50)

if umur >= 13:
    kategori = "Remaja"
elif umur >= 6:
    kategori = "Anak-anak"
else:
    kategori = "Balita"

print(f"Umur kamu {umur} tahun, jadi kamu termasuk kategori: {kategori}")

print("\n" + "="*50)
print("CONTOH 2: SISTEM PENILAIAN")
print("="*50)

nilai = int(input("Masukkan nilai ujian kamu (0-100): "))

print(f"Nilai kamu: {nilai}")

if nilai >= 90:
    grade = "A"
    keterangan = "Excellent! Pertahankan!"
elif nilai >= 80:
    grade = "B"
    keterangan = "Good job! Tingkatkan lagi!"
elif nilai >= 70:
    grade = "C"
    keterangan = "Cukup baik, bisa lebih baik lagi!"
elif nilai >= 60:
    grade = "D"
    keterangan = "Perlu belajar lebih giat!"
else:
    grade = "E"
    keterangan = "Jangan menyerah, terus belajar!"

print(f"Grade kamu: {grade}")
print(f"Keterangan: {keterangan}")

print("\n" + "="*50)
print("CONTOH 3: KALKULATOR SEDERHANA")
print("="*50)

print("Mari buat kalkulator sederhana!")
angka1 = float(input("Masukkan angka pertama: "))
operasi = input("Pilih operasi (+, -, *, /): ")
angka2 = float(input("Masukkan angka kedua: "))

if operasi == "+":
    hasil = angka1 + angka2
elif operasi == "-":
    hasil = angka1 - angka2
elif operasi == "*":
    hasil = angka1 * angka2
elif operasi == "/":
    if angka2 != 0:
        hasil = angka1 / angka2
    else:
        hasil = "Error: Tidak bisa dibagi dengan 0"
else:
    hasil = "Error: Operasi tidak valid"

print(f"Hasil: {angka1} {operasi} {angka2} = {hasil}")

print("\n📝 TUGAS UNTUK KAMU:")
print("1. Buat program untuk menentukan apakah suatu angka genap atau ganjil")
print("2. Buat program untuk menentukan hari sekolah atau libur berdasarkan input hari")
print("3. Buat program kalkulator yang bisa menangani lebih banyak operasi")

# Area untuk siswa berlatih:
# Tugas 1: Genap atau Ganjil
# angka = int(input("Masukkan sebuah angka: "))
# if angka % 2 == 0:
#     print("Angka genap")
# else:
#     print("Angka ganjil")
