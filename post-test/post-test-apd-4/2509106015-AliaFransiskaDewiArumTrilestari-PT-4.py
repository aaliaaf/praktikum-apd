import os

belilagi = 'yes'

while belilagi == 'yes':
    os.system("cls" if os.name == "nt" else "clear")

    #Menu
    menu = 'SilverQueen'
    menu = 'DairyMilk'
    menu = 'Kinderjoy'

    #Harga menu
    hargaSilverQueen = 25000
    hargaDairyMilk = 27000
    hargaKinderjoy = 13000

    #Username and password
    username = 'alia' 
    password = '015'

    #Kesempatan Login
    login = 3

    member = input('Apakah Kamu Mempunyai Member? (yes/no?) :')

    if member == 'yes':
        print('\n---- Menu Login Untuk Member ----')
        while login >0:
            nama = input('Masukkan Username :').strip()
            sandi = input('Masukkan Password :').strip()
            if not nama or not sandi:
                print('Nama dan sandi tidak boleh kosong atau spasi')
            status = 'Login member berhasil!' if (nama == username and sandi == password) else 'Login member gagal!'
            print(status)

            if status == 'Login member berhasil!':
                break
            else:
                login -= 1
                if login >0:
                    print(f'Error! Sisa percobaan login : {login}')
                else:
                    print('\n=== Kesempatan login telah mencapai batas maksimum. Silahkan berbelanja tanpa member')

        if status == 'Login member berhasil!':
            print('\n Selamat Datang Di Toko Guro Selamat Berbelanja ')
            print("-" * 61)
            print(f"|{' Daftar Menu dan Harga  ':<59}|")
            print("-" * 61)
            print(f"| SilverQueen   : {hargaSilverQueen:<42}|")
            print(f"| DairyMilk     : {hargaDairyMilk:<42}|")
            print(f"| Kinderjoy     : {hargaKinderjoy:<42}|")
            print("-" * 61)

            total = 0
            keranjang_checkout = ""
            menu = ""

            menu = input('Mau Membeli Menu Apa? (silverqueen/dairymilk/kinderjoy) :')
            if menu == 'silverqueen':
                harga = hargaSilverQueen
                total += harga
                keranjang_checkout += f'{menu}'
                print(f'{menu} sudah masuk kerangjang')
                print(f'Total sementara: Rp{total}')

            elif menu == 'dairymilk':
                harga = hargaDairyMilk
                total += harga
                keranjang_checkout += f'{menu}'
                print(f'{menu} sudah masuk kerangjang')
                print(f'Total sementara: Rp{total}')
                
            else:
                harga = hargaKinderjoy
                total += harga
                keranjang_checkout += f'{menu}'
                print(f'{menu} sudah masuk kerangjang')
                print(f'Total sementara: Rp{total}')
                
            beli = input('Apakah ada lagi yang mau dibeli lagi? (yes/no): ')
            if beli == 'yes':
                
                while menu != 'checkout':
                    menu = input('Mau Membeli Menu Apa Lagi? (silverqueen/dairymilk/kinderjoy/checkout) :')
                    if menu == 'silverqueen':
                        harga = hargaSilverQueen
                        total += harga
                        
                        keranjang_checkout += f", {menu}"
                        print(f'{menu} sudah masuk kerangjang')
                        print(f'Total sementara: Rp{total}')

                    elif menu == 'dairymilk':
                        harga = hargaDairyMilk
                        total += harga

                        keranjang_checkout += f", {menu}"
                        print(f'{menu} sudah masuk kerangjang')
                        print(f'Total sementara: Rp{total}')
                        
                    elif menu == 'kinderjoy':
                        print()
                        harga = hargaKinderjoy
                        total += harga
                        
                        keranjang_checkout += f", {menu}"
                        print(f'{menu} sudah masuk kerangjang')
                        print(f'Total sementara: Rp{total}')

                    elif menu == 'checkout':
                        print('/n=== Lagi Checkout ===')
                        break
                    else:
                        print('Silahkan pilih dari daftar menu')
            else:
                print('Silahkan langsung ke kasir')

            diskon = total * 0.15
            hargaSetelahDiskon = total - diskon

            print("-" * 70)
            print(f"|{'Struk Belanja Toko Guro':^68}|")
            print("-" * 70)
            print(f"| Atas Nama               : {username:<41}|")
            print(f"| Menu                    : {keranjang_checkout:<41}|")
            print(f"| Harga sebelum diskon    : Rp {total:<38}|")
            print(f"| Diskon (15%)            : Rp {diskon:<38}|")
            print(f"| Harga setelah diskon    : Rp {hargaSetelahDiskon:<38}|")
            print(f"| Total yang harus dibawa : Rp {hargaSetelahDiskon:<38}|")
            print("-" * 70)

        else:
            print('Anda berbelanja tanpa member ===')
            print('\n=== Selamat Datang Di Toko Guro Selamat Berbelanja ===')
            print("-" * 61)
            print(f"|{' Daftar Menu dan Harga  ':<59}|")
            print("-" * 61)
            print(f"| SilverQueen   : {hargaSilverQueen:<42}|")
            print(f"| DairyMilk     : {hargaDairyMilk:<42}|")
            print(f"| Kinderjoy     : {hargaKinderjoy:<42}|")
            print("-" * 61)

            menu = input('Mau Membeli Menu Apa? (silverqueen/dairymilk/kinderjoy) :')
            username = input('Mau Atas Nama Siapa Pesanannya? : ')
            
            if menu == 'silverqueen':
                harga = hargaSilverQueen
            elif menu == 'dairymilk':
                harga = hargaDairyMilk
            else:
                harga = hargaKinderjoy

            print("-" * 61)
            print(f"|{'Struk Belanja Toko Guro':^59}|")
            print("-" * 61)
            print(f"| Atas Nama             : {username:<34}|")
            print(f"| Menu                  : {menu:<34}|")
            print(f"| Total                 : Rp {harga:<31}|")
            print("-" * 61)


    else:
        print('\n=== Selamat Datang Di Toko Guro Selamat Berbelanja ===')
        print("-" * 61)
        print(f"|{' Daftar Menu dan Harga  ':<59}|")
        print("-" * 61)
        print(f"| SilverQueen   : {hargaSilverQueen:<42}|")
        print(f"| DairyMilk     : {hargaDairyMilk:<42}|")
        print(f"| Kinderjoy     : {hargaKinderjoy:<42}|")
        print("-" * 61)

        menu = input('Mau Membeli Menu Apa? (silverqueen/dairymilk/kinderjoy) :')
        username = input('Mau Atas Nama Siapa Pesanannya? : ')
        
        if menu == 'silverqueen':
            harga = hargaSilverQueen
        elif menu == 'dairymilk':
            harga = hargaDairyMilk
        else:
            harga = hargaKinderjoy

        print("-" * 61)
        print(f"|{'Struk Belanja Toko Guro':^59}|")
        print("-" * 61)
        print(f"| Atas Nama             : {username:<34}|")
        print(f"| Menu                  : {menu:<34}|")
        print(f"| Total                 : Rp {harga:<31}|")
        print("-" * 61)

    belilagi = input('Apakah mau membeli sesuatu lagi? (yes/no): ')

print('Program berhenti')
