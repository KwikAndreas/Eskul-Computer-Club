# Bermain dengan string methods
nama = "budi santoso"
sekolah = "SMP NEGERI 1 JAKARTA"

print("=== BERMAIN DENGAN STRING ===")
print("Nama asli:", nama)
print("Sekolah asli:", sekolah)
print()

# Methods untuk mengubah case
print("=== MENGUBAH HURUF ===")
print("Nama dengan huruf kapital:", nama.upper())
print("Nama dengan huruf kecil:", nama.lower())
print("Nama dengan huruf kapital di awal:", nama.title())
print("Nama dengan huruf kapital di awal kata:", nama.capitalize())

print()
print("Sekolah dengan huruf kecil:", sekolah.lower())
print("Sekolah dengan huruf kapital di awal:", sekolah.title())

# Methods untuk manipulasi
print()
print("=== MANIPULASI STRING ===")
print("Jumlah huruf dalam nama:", len(nama))
print("Mengganti 'budi' dengan 'andi':", nama.replace("budi", "andi"))
print("Apakah ada kata 'santoso'?", "santoso" in nama)