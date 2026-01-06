kalkulator
while True:
    print("===== MENU KALKULATOR =====")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "5":
        print("Terima kasih, program selesai.")
        break

    if pilihan in ["1", "2", "3", "4"]:
        a = float(input("Masukkan bilangan pertama: "))
        b = float(input("Masukkan bilangan kedua: "))

        if pilihan == "1":
            hasil = a + b
            print("Hasil penjumlahan:", hasil)

        elif pilihan == "2":
            hasil = a - b
            print("Hasil pengurangan:", hasil)

        elif pilihan == "3":
            hasil = a * b
            print("Hasil perkalian:", hasil)

        elif pilihan == "4":
            if b != 0:
                hasil = a / b
                print("Hasil pembagian:", hasil)
            else:
                print("Error: Tidak bisa dibagi dengan nol!")
    else:
        print("Menu tidak valid!")

    print()  # baris kosong agar rapi
