import random

angka = random.randrange(1,50)
tebakan = 0
tebakan_anda = int(input("Masukan angka tebakan anda antara 1 sampai dengan 50 : "))
while tebakan_anda != angka:
    if tebakan_anda > angka:
        print(tebakan_anda,"telalu tinggi")
    elif tebakan_anda < angka:
        print(tebakan_anda,"telalu rendah")
    tebakan += 1
    if tebakan > 3:
        print("Kamu telah gagal")
        break
    tebakan_anda = int(input("tebak lagi : "))
if tebakan_anda == angka:
    print("Bagus! Anda menebak dalam ",tebakan,"kali tebakan")
else:
    print("Gagal! Anda menebak dalam ",tebakan,"kali tebakan")