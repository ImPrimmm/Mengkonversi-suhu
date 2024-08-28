print("\n===MENGKONVERSI SUHU===\n")
suhu = str(input("Pilih suhu antara C,R,F,K:"))
nilai = float(input("Masukan Nilai:"))

if suhu == "C":
  
  print("\n===MENGKONVERSI SUHU CELCIUS KE===\n===REAMUR,FAHRENHEIT,DAN KELVIN===\n")
  
  hasil = (9 / 5 * nilai) + 32
  print("Mengkonversi ke Fahrenheit:",hasil)
  hasil = nilai + 273.15
  print("Mengkonversi ke Kelvin:",hasil)
  hasil = 4 / 5 * nilai
  print("Mengkonversi ke Reamur:",hasil)
  
elif suhu == "R":
  
  print("\n===MENGKONVERSI SUHU REAMUR KE===\n==CELCIUS,FAHRENHEIT,DAN KELVIN==\n")
  
  hasil = 5 / 4 * nilai
  print("Mengkonversi ke Celcius:",hasil)
  hasil = (9 / 4 * nilai) + 32
  print("Mengkonversi ke Fahrenheit:",hasil)
  hasil = 5 / 4 * nilai + 273.15
  print("Mengkonversi ke Kelvin:",hasil)
  
elif suhu == "F":
  
  print("\n===MENGKONVERSI SUHU FAHRENHEIT KE===\n======CELCIUS,REAMUR,DAN KELVIN======\n")
  
  hasil = 5 / 9 * (nilai - 32)
  print("Mengkonversi ke Celcius:",hasil)
  hasil = 4 / 9 * (nilai - 32)
  print("Mengkonversi ke Reamur:",hasil)
  hasil = (5 / 9 * (nilai - 32)) + 273.15
  print("Mengkonversi ke Kelvin:",hasil)
  
elif suhu == "K":
  
  print("\n===MENGKONVERSI SUHU KELVIN KE===\n==CELCIUS,REAMUR,DAN FAHRENHEIT==\n")
  
  hasil = nilai - 273.15
  print("Mengkonversi ke Celcius:",hasil)
  hasil = 4 / 5 * (nilai - 273.15)
  print("Mengkonversi ke Reamur:",hasil)
  hasil = (9 / 5 * (nilai - 273.1)) + 32
  print("Mengkonversi ke Fahrenheit:",hasil)
  
else:
  print("Input suhu salah")
  