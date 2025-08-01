# ========================================
# MINGGU 2 - SESI 1: KONDISI
# Durasi: 30 menit
# ========================================

print("Selamat datang di minggu ke-2!")
print("Hari ini kita akan belajar tentang kondisi dan pengambilan keputusan")

print("\n=== Apa itu Kondisi? ===")
print("Kondisi membantu program mengambil keputusan")
print("Seperti: 'Jika hujan, maka bawa payung'")

# Mengumpulkan data siswa
nama = input("Masukkan nama kamu: ")
umur = int(input("Berapa umur kamu? "))

print(f"\nHalo {nama}!")

print("\n" + "="*40)
print("CONTOH 1: MENENTUKAN KATEGORI UMUR")
print("="*40)

if umur >= 13:
    kategori = "Remaja"
elif umur >= 6:
    kategori = "Anak-anak"
else:
    kategori = "Balita"

print(f"Umur kamu {umur} tahun, jadi kamu termasuk kategori: {kategori}")

print("\n" + "="*40)
print("CONTOH 2: SISTEM PENILAIAN SEDERHANA")
print("="*40)

nilai = int(input("Masukkan nilai ujian kamu (0-100): "))

print(f"Nilai kamu: {nilai}")

if nilai >= 80:
    grade = "A"
    keterangan = "Excellent!"
elif nilai >= 70:
    grade = "B"
    keterangan = "Good job!"
elif nilai >= 60:
    grade = "C"
    keterangan = "Cukup baik!"
else:
    grade = "D"
    keterangan = "Perlu belajar lebih giat!"

print(f"Grade kamu: {grade}")
print(f"Keterangan: {keterangan}")

print("\n" + "="*40)
print("LATIHAN: GENAP ATAU GANJIL")
print("="*40)

angka = int(input("Masukkan sebuah angka: "))

if angka % 2 == 0:
    print(f"{angka} adalah angka genap")
else:
    print(f"{angka} adalah angka ganjil")

print("\n📝 TUGAS UNTUK KAMU:")
print("1. Buat program untuk menentukan apakah hari ini hari sekolah")
print("2. Buat program untuk menentukan kategori cuaca (panas/dingin)")
print("3. Coba buat kondisi dengan 3 pilihan atau lebih")

# Area untuk siswa berlatih:
# hari = input("Masukkan nama hari: ").lower()
# if hari in ["senin", "selasa", "rabu", "kamis", "jumat"]:
#     print("Hari sekolah!")
# else:
#     print("Hari libur!")
