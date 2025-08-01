# ========================================
# PERTEMUAN 2: VARIABEL DAN TIPE DATA
# ========================================

print("Selamat datang di pelajaran ke-2!")
print("Hari ini kita akan belajar tentang variabel dan tipe data")

print("\n=== Apa itu Variabel? ===")
print("Variabel adalah 'kotak' untuk menyimpan data")
print("Seperti loker sekolah yang bisa kita isi dengan barang-barang")

print("\n=== Input dari Pengguna ===")
print("Kita bisa meminta pengguna memasukkan data dengan input()")

# Mengumpulkan data dari siswa
nama = input("Masukkan nama kamu: ")
kelas = input("Masukkan kelas kamu (contoh: 7A): ")
umur = input("Masukkan umur kamu: ")

print(f"\nHalo {nama}!")
print(f"Kamu dari kelas {kelas} dan berumur {umur} tahun")

print("\n" + "="*50)
print("KONSEP PENTING: TIPE DATA")
print("="*50)

print("\n1. STRING (str) - untuk teks")
print(f"   Nama kamu: {nama}")
print(f"   Tipe data: {type(nama)}")

print("\n2. INTEGER (int) - untuk bilangan bulat")
print("   Tapi input() selalu menghasilkan string!")
print("   Kita perlu mengubahnya dengan int()")

umur_angka = int(umur)  # Mengubah string ke integer
print(f"   Umur sebagai angka: {umur_angka}")
print(f"   Tipe data: {type(umur_angka)}")

print("\n3. BOOLEAN (bool) - untuk True/False")
sudah_mengerjakan_pr = True
print(f"   Sudah mengerjakan PR: {sudah_mengerjakan_pr}")
print(f"   Tipe data: {type(sudah_mengerjakan_pr)}")

print("\n" + "="*50)
print("LATIHAN MATEMATIKA SEDERHANA")
print("="*50)

nilai_matematika = 85
nilai_ipa = 90

print(f"Nilai Matematika: {nilai_matematika}")
print(f"Nilai IPA: {nilai_ipa}")

rata_rata = (nilai_matematika + nilai_ipa) / 2
print(f"Nilai rata-rata: {rata_rata}")

print("\n📝 TUGAS UNTUK KAMU:")
print("1. Buat variabel untuk menyimpan mata pelajaran favorit")
print("2. Buat variabel untuk menyimpan jumlah teman di kelas")
print("3. Tampilkan semua variabel yang sudah kamu buat")

# Area untuk siswa berlatih:
# Tulis kode kamu di bawah ini:

# mata_pelajaran_favorit = "..."
# jumlah_teman = ...
# print(f"Mata pelajaran favorit: {mata_pelajaran_favorit}")
# print(f"Jumlah teman di kelas: {jumlah_teman}")