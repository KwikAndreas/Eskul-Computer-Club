# Input
angka1 = input("Masukkan angka pertama: ")
angka2 = input("Masukkan angka kedua: ")

# Konversi string ke integer
num1 = int(angka1)
num2 = int(angka2)

# Perhitungan
hasil_tambah = num1 + num2
hasil_kurang = num1 - num2
hasil_kali = num1 * num2
hasil_bagi = num1 / num2

# Output hasil
print()
print("=== HASIL PERHITUNGAN ===")
print(num1, "+", num2, "=", hasil_tambah)
print(num1, "-", num2, "=", hasil_kurang)
print(num1, "×", num2, "=", hasil_kali)
print(num1, "÷", num2, "=", hasil_bagi)