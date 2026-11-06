jumlah = int(input("Masukkan jumlah mahasiswa: "))

total = 0

for i in range(jumlah):
    nilai = float(input(f"Masukkan nilai mahasiswa ke-{i+1}: "))
    total += nilai

rata_rata = total / jumlah

print("\nJumlah mahasiswa:", jumlah)
print("Total nilai:", total)
print("Nilai rata-rata:", rata_rata)
