# Variabel pertama - konsep kotak penyimpanan
print("=== PENGHITUNGAN UANG JAJAN ===")

# Membuat "kotak" untuk menyimpan data
uang_senin = 5000
uang_selasa = 7000  
uang_rabu = 6000
uang_kamis = 8000
uang_jumat = 5000

# Menghitung total
total_uang = uang_senin + uang_selasa + uang_rabu + uang_kamis + uang_jumat

# Menampilkan hasil
print("Uang jajan Senin  : Rp", uang_senin)
print("Uang jajan Selasa : Rp", uang_selasa)
print("Uang jajan Rabu   : Rp", uang_rabu)
print("Uang jajan Kamis  : Rp", uang_kamis)
print("Uang jajan Jumat  : Rp", uang_jumat)
print("-" * 30)
print("Total uang jajan  : Rp", total_uang)
print("Rata-rata per hari: Rp", total_uang / 5)