# ========================================
# MINGGU 3 - SESI 1: LIST DAN TUPLE
# Durasi: 30 menit
# ========================================

print("Selamat datang di minggu ke-3!")
print("Hari ini kita akan belajar tentang List dan Tuple")

print("\n=== Apa itu List? ===")
print("List adalah 'keranjang' yang bisa menyimpan banyak data")
print("Seperti daftar belanja yang bisa ditambah dan dikurangi")

print("\n" + "="*40)
print("CONTOH 1: MEMBUAT DAN MENGGUNAKAN LIST")
print("="*40)

# Membuat list
teman_sekelas = ["Andi", "Budi", "Citra", "Dina"]
print("Daftar teman sekelas:")
print(teman_sekelas)

print(f"\nJumlah teman: {len(teman_sekelas)}")
print(f"Teman pertama: {teman_sekelas[0]}")
print(f"Teman terakhir: {teman_sekelas[-1]}")

print("\n" + "="*40)
print("MENAMBAH DAN MENGHAPUS DATA")
print("="*40)

# Menambah data ke list
teman_baru = input("Masukkan nama teman baru: ")
teman_sekelas.append(teman_baru)
print(f"Setelah ditambah: {teman_sekelas}")

# Menghapus data dari list
print(f"Menghapus {teman_sekelas[0]} dari list...")
teman_sekelas.remove(teman_sekelas[0])
print(f"Setelah dihapus: {teman_sekelas}")

print("\n" + "="*40)
print("CONTOH 2: LIST ANGKA")
print("="*40)

nilai_ujian = [85, 90, 78, 92, 88]
print(f"Nilai ujian: {nilai_ujian}")
print(f"Nilai tertinggi: {max(nilai_ujian)}")
print(f"Nilai terendah: {min(nilai_ujian)}")
print(f"Rata-rata: {sum(nilai_ujian) / len(nilai_ujian)}")

print("\n" + "="*40)
print("CONTOH 3: TUPLE (DATA YANG TIDAK BISA DIUBAH)")
print("="*40)

koordinat = (10, 20)  # tuple menggunakan kurung ()
print(f"Koordinat: {koordinat}")
print(f"X: {koordinat[0]}, Y: {koordinat[1]}")

# Tuple tidak bisa diubah, berbeda dengan list
print("Tuple tidak bisa ditambah atau dikurangi seperti list")

print("\n" + "="*40)
print("LATIHAN: DAFTAR MATA PELAJARAN")
print("="*40)

mata_pelajaran = []  # list kosong
print("Mari buat daftar mata pelajaran favorit!")

# Menambah 3 mata pelajaran
for i in range(3):
    mapel = input(f"Masukkan mata pelajaran ke-{i+1}: ")
    mata_pelajaran.append(mapel)

print(f"\nDaftar mata pelajaran favorit:")
for i, mapel in enumerate(mata_pelajaran, 1):
    print(f"{i}. {mapel}")

print("\n" + "="*40)
print("LATIHAN: MENCARI DATA DALAM LIST")
print("="*40)

buah_favorit = ["apel", "pisang", "jeruk", "mangga", "anggur"]
print(f"Daftar buah tersedia: {buah_favorit}")

cari_buah = input("Buah apa yang kamu cari? ").lower()
if cari_buah in buah_favorit:
    posisi = buah_favorit.index(cari_buah)
    print(f"{cari_buah} ada di posisi ke-{posisi + 1}")
else:
    print(f"{cari_buah} tidak ada dalam daftar")

print("\n📝 TUGAS UNTUK KAMU:")
print("1. Buat list berisi nama 5 hewan favorit kamu")
print("2. Tambahkan 2 hewan lagi ke dalam list")
print("3. Cetak semua hewan dengan nomor urutnya")

# Area untuk siswa berlatih:
# hewan_favorit = ["kucing", "anjing", "hamster", "kelinci", "burung"]
# hewan_favorit.append("ikan")
# hewan_favorit.append("kura-kura")
# 
# for i, hewan in enumerate(hewan_favorit, 1):
#     print(f"{i}. {hewan}")
