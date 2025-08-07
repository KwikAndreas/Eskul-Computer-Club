# Belajar mengubah tipe data
print("=== KONVERSI TIPE DATA ===")

# Input sebagai string
input_umur = input("Masukkan umur kamu: ")
input_tinggi = input("Masukkan tinggi badan (cm): ")

print("Sebelum konversi:")
print("Umur (string):", input_umur, "- Tipe:", type(input_umur))
print("Tinggi (string):", input_tinggi, "- Tipe:", type(input_tinggi))

# Konversi ke angka
umur = int(input_umur)
tinggi = float(input_tinggi)

print()
print("Setelah konversi:")
print("Umur (integer):", umur, "- Tipe:", type(umur))
print("Tinggi (float):", tinggi, "- Tipe:", type(tinggi))

# Operasi dengan data yang sudah dikonversi
umur_10_tahun_lagi = umur + 10
tinggi_dalam_meter = tinggi / 100

print()
print("=== HASIL PERHITUNGAN ===")
print("Umur 10 tahun lagi:", umur_10_tahun_lagi, "tahun")
print("Tinggi dalam meter:", tinggi_dalam_meter, "m")