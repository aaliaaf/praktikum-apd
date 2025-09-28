#Menu
menu = str('SilverQueen, DairyMilk, Kinderjoy') 

#Harga menu
hargaSilverQueen = 25000
hargaDairyMilk = 27000
hargaKinderjoy = 13000

#Username and password
username = 'alia' 
password = '015'

member = input('Apakah Kamu Mempunyai Member? (punya/tidak?) :')

if member == 'punya':
    print('\n---- Menu Login Untuk Member ----')
    nama = input('Masukkan Username :')
    sandi = input('Masukkan Password :') 
    status = 'Login member berhasil!' if (nama == username and sandi == password) else 'Login member gagal!'
    print('Status :', status)

    if status == 'Login member berhasil!':
        print('\n=== Selamat Datang Di Toko Guro ===')
        print("-" * 61)
        print(f"|{' Daftar Menu dan Harga  ':<59}|")
        print("-" * 61)
        print(f"| SilverQueen   : {hargaSilverQueen:<42}|")
        print(f"| DairyMilk     : {hargaDairyMilk:<42}|")
        print(f"| Kinderjoy     : {hargaKinderjoy:<42}|")
        print("-" * 61)

        menu = input('Mau Membeli Menu Apa? (silverQueen/dairyMilk/kinderjoy) :')

        if menu == 'silverqueen':
            harga = hargaSilverQueen
        elif menu == 'dairymilk':
            harga = hargaDairyMilk
        else:
            harga = hargaKinderjoy

        diskon = harga * 0.15
        hargaSetelahDiskon = harga - diskon

        print("-" * 61)
        print(f"|{'Struk Belanja Toko Guro':^59}|")
        print("-" * 61)
        print(f"| Atas Nama            : {username:<35}|")
        print(f"| Menu                 : {menu:<35}|")
        print(f"| Harga sebelum diskon : Rp {harga:<32}|")
        print(f"| Diskon (15%)         : Rp {diskon:<32}|")
        print(f"| Harga setelah diskon : Rp {hargaSetelahDiskon:<32}|")
        print("-" * 61)

else:
    print('\n=== Selamat Datang Di Toko Guro ===')
    print("-" * 61)
    print(f"|{' Daftar Menu dan Harga  ':<59}|")
    print("-" * 61)
    print(f"| SilverQueen   : {hargaSilverQueen:<42}|")
    print(f"| DairyMilk     : {hargaDairyMilk:<42}|")
    print(f"| Kinderjoy     : {hargaKinderjoy:<42}|")
    print("-" * 61)

    menu = input('Mau Membeli Menu Apa? (silverQueen/dairyMilk/kinderjoy) :')
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




