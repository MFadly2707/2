nilai = []
jumlah = int(input("Masukkan jumlah nilai: "))
for i in range(jumlah):
    nilai.append(int(input("Masukkan nilai ke-{}: ".format(i+1))))


print("Nilai dalam urutan ascending:", sorted(nilai))


print("Nilai dalam urutan descending:", sorted(nilai, reverse=True))


print("Nilai minimum:", min(nilai))


print("Nilai maksimum:", max(nilai))


rata_rata = sum(nilai) / len(nilai)
print("Rata-rata nilai:", rata_rata)