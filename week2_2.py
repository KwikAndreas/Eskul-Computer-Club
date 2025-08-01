# ========================================
# MINGGU 2 - SESI 2: PERULANGAN
# Durasi: 30 menit
# ========================================

print("Selamat datang di sesi ke-2 minggu kedua!")
print("Hari ini kita akan belajar tentang perulangan (loop)")

print("\n=== Apa itu Perulangan? ===")
print("Perulangan membantu kita menjalankan kode berulang-ulang")
print("Seperti: mencetak nama 10 kali tanpa menulis print() 10 kali")

print("\n" + "="*40)
print("CONTOH 1: PERULANGAN FOR")
print("="*40)

print("Mari cetak angka 1 sampai 5:")
for i in range(1, 6):
    print(f"Angka: {i}")

print("\nMari cetak nama kamu 3 kali:")
nama = input("Masukkan nama kamu: ")
for i in range(3):
    print(f"Halo {nama}! (ke-{i+1})")

print("\n" + "="*40)
print("CONTOH 2: PERULANGAN DENGAN LIST")
print("="*40)

buah_buahan = ["apel", "pisang", "jeruk", "mangga"]
print("Daftar buah-buahan:")
for buah in buah_buahan:
    print(f"- {buah}")

print("\n" + "="*40)
print("CONTOH 3: PERULANGAN WHILE")
print("="*40)

print("Hitung mundur dari 5:")
hitung = 5
while hitung > 0:
    print(f"Hitung mundur: {hitung}")
    hitung = hitung - 1  # atau bisa ditulis: hitung -= 1
print("Selesai!")

print("\n" + "="*40)
print("LATIHAN: TABEL PERKALIAN")
print("="*40)

angka = int(input("Masukkan angka untuk tabel perkalian: "))
print(f"\nTabel perkalian {angka}:")

for i in range(1, 6):  # hanya sampai 5 agar tidak terlalu panjang
    hasil = angka * i
    print(f"{angka} x {i} = {hasil}")

print("\n" + "="*40)
print("LATIHAN: MENGHITUNG JUMLAH")
print("="*40)

print("Mari hitung jumlah angka 1 + 2 + 3 + 4 + 5:")
total = 0
for i in range(1, 6):
    total = total + i
    print(f"Sekarang total = {total}")

print(f"Jumlah akhir: {total}")

print("\n📝 TUGAS UNTUK KAMU:")
print("1. Buat perulangan untuk mencetak nama teman-teman di kelas")
print("2. Buat hitung mundur dari 10 ke 1")
print("3. Hitung jumlah semua angka genap dari 2 sampai 10")

# Area untuk siswa berlatih:
# print("Contoh jawaban tugas 2:")
# for i in range(10, 0, -1):
#     print(f"Hitung mundur: {i}")
# print("Habis!")
