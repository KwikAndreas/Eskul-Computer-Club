# ========================================
# MINGGU 1 - SESI 2: VARIABEL DAN TIPE DATA
# Durasi: 30 menit
# ========================================

print("Selamat datang di sesi ke-2!")
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

print("\n" + "="*40)
print("KONSEP PENTING: TIPE DATA")
print("="*40)

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

print("\n" + "="*40)
print("LATIHAN SEDERHANA")
print("="*40)

# Contoh operasi sederhana
print("Mari hitung umur kamu tahun depan:")
umur_tahun_depan = umur_angka + 1
print(f"Umur kamu tahun depan: {umur_tahun_depan} tahun")

print("\n📝 TUGAS UNTUK KAMU:")
print("1. Buat variabel untuk menyimpan mata pelajaran favorit")
print("2. Buat variabel untuk menyimpan jumlah teman di kelas")
print("3. Tampilkan semua variabel yang sudah kamu buat")

# Area untuk siswa berlatih:
# mata_pelajaran_favorit = "..."
# jumlah_teman = ...
# print(f"Mata pelajaran favorit: {mata_pelajaran_favorit}")
# print(f"Jumlah teman di kelas: {jumlah_teman}")
