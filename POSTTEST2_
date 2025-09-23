print('\n---- Pengecekan Berat Badan ---')

#Input Data
namaPasien = str(input("masukkan nama pasien : "))
tinggiBadan = float(input("masukkan tinggi badan (cm) : "))
beratBadan = float(input("masukkan berat badan (kg) : "))

#Rumus berat ideal
beratIdeal = (tinggiBadan - 100)
isKelebihan = beratBadan > beratIdeal 

#Status list
statusList = ['Tidak kelebihan berat badan', 'Kelebihan berat badan']
status = statusList[int(isKelebihan)]

print("-" * 61)
print(f"|{'HASIL CEK BERAT BADAN':^59}|")
print("-" * 61)
print(f"| Nama Pasien      : {namaPasien:<39}|")
print(f"| Tinggi Badan     : {tinggiBadan:<4.1f} cm{'':<31}|")
print(f"| Berat Badan      : {beratBadan:<4.1f} kg{'':<32}|")
print(f"| Berat Ideal      : {beratIdeal:<4.1f} kg{'':<32}|")
print(f"| Status           : {status:<39}|")
print("-" * 61)
