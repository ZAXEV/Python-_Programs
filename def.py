#ALEX's MONEY CONVERTER
import sys
import time

print("Selamat datang di money converter!")
print("Pilih opsi: ")
while True: 
    print("----------------------------------")
    print("1. Konversikan mata uang")
    print("2. Keluar program")
    user_input = int(input("Pilihan anda: "))

    if user_input == 1:
        print("----------------------------------")
        print("1. Konversikan Dollar ke Rupiah")
        print("2. Konversikan Rupiah ke Dollar")
        user_input2 = int(input("Masukkan pilihan anda (1/2): "))
        if user_input2 == 1:
            print("----------------------------------")
            print("Masukkan nominal Dollar yang ingin anda konverikan ke Rupiah: ")
            user_nominal = int(input("Masukkan nominal: "))
            print("Hasil rupiahnya adalah: Rp.",user_nominal * 15000)
        elif user_input2 == 2:
            print("----------------------------------")
            print("Masukkan nominal Rupiah yang ingin anda konveresikan menjadi Dollar: ")
            user_nominal = int(input("Masukkan nominal: "))
            print("Hasil Dollarnya adalah: $", user_nominal / 15000)
        else:
            print("----------------------------------")
            print("Masukkan angka 1 atau 2 saja!")
    elif user_input == 2:
        print("----------------------------------")
        print("Keluar dari program...")
        time.sleep(2)
        sys.exit()

