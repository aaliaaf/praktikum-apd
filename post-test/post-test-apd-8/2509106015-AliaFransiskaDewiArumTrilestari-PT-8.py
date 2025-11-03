from bersih import clear
from login import login
from login import pengguna
from create import tambah_alat
from  delete import hapus_alat
from read import tampilkan_alat
from update import ubah_status
from colorama import Fore, Style, init
init(autoreset=True)

while True:
    clear()
    print(Fore.BLUE + Style.BRIGHT + "=== SISTEM PENGELOLA ALAT BERAT ===")
    print(Fore.YELLOW + Style.BRIGHT +  "1. Login")
    print(Fore.YELLOW + Style.BRIGHT + "2. Register")
    print(Fore.YELLOW + Style.BRIGHT + "3. Keluar")

    menu = input(Fore.MAGENTA + Style.BRIGHT + "Pilih menu (1-3): ")

    if menu == "1":
        login_user = login() 
        if login_user is None:
            continue

        akses = pengguna[login_user]["akses"]

        # === MENU ADMIN ===
        if akses == "admin":
            while True:
                clear()
                print(Fore.BLUE + Style.BRIGHT + f"=== MENU ADMIN ({login_user}) ===")
                print(Fore.YELLOW + Style.BRIGHT + "1. Tambah alat baru")
                print(Fore.YELLOW + Style.BRIGHT + "2. Lihat semua alat")
                print(Fore.YELLOW + Style.BRIGHT + "3. Ubah status alat")
                print(Fore.YELLOW + Style.BRIGHT + "4. Hapus alat")
                print(Fore.YELLOW + Style.BRIGHT + "5. Keluar")

                pilihan = input(Fore.MAGENTA + Style.BRIGHT + "Pilih menu (1-5): ")
                if pilihan == "1":
                    tambah_alat()
                elif pilihan == "2":
                    tampilkan_alat()
                elif pilihan == "3":
                    clear()
                    alat = input(Fore.MAGENTA + Style.BRIGHT + "Masukkan nama alat yang mau diubah: ").strip()
                    status_baru = input(Fore.MAGENTA + Style.BRIGHT + "Masukkan status baru (Siap Pakai/Rusak/Dalam Perbaikan) : ").strip()
                    ubah_status(alat, status_baru)
                elif pilihan == "4":
                    hapus_alat()
                elif pilihan == "5":
                    break
                else:
                    print(Fore.RED + Style.BRIGHT + "Gunakan nomor menu yang sudah disediakan!")
                input(Fore.CYAN + Style.BRIGHT + "Tekan Enter untuk melanjutkan...")
        # === MENU USER ===
        else:
            while True:
                clear()
                print(Fore.BLUE + Style.BRIGHT + f"=== MENU USER ({login_user}) ===")
                print(Fore.YELLOW + Style.BRIGHT + "1. Lihat alat berat")
                print(Fore.YELLOW + Style.BRIGHT + "2. Keluar")

                pilihan = input(Fore.MAGENTA + Style.BRIGHT + "Pilih menu (1-3): ")

                if pilihan == "1":
                    tampilkan_alat()
                elif pilihan == "2":
                    break
                else:
                    print(Fore.RED + Style.BRIGHT + "Gunakan menu 1-3!")
                input(Fore.CYAN + Style.BRIGHT + "Tekan Enter untuk melanjutkan...")
    # === REGISTER ===
    elif menu == "2":
        clear()
        print(Fore.BLUE + Style.BRIGHT + "=== REGISTER AKUN BARU ===")
        username = input(Fore.MAGENTA + Style.BRIGHT + "Masukkan username baru: ").strip()
        password = input(Fore.MAGENTA + Style.BRIGHT + "Masukkan password baru: ").strip()

        if username in pengguna:
            print(Fore.RED + Style.BRIGHT + "Username sudah terdaftar!")
        else:
            pengguna[username] = {"password": password, "akses": "user"}
            print(Fore.GREEN + Style.BRIGHT + f"Akun '{username}' berhasil dibuat sebagai user!")
        input(Fore.CYAN + Style.BRIGHT + "Tekan Enter untuk melanjutkan...")

    elif menu == "3":
        clear()
        print(Fore.RED + Style.BRIGHT + "Program berhenti.")
        break

    else:
        clear()
        print(Fore.RED + Style.BRIGHT + "Pilihan menu tidak sesuai! Gunakan nomor menu yang sudah disediakan!")
        input(Fore.CYAN + Style.BRIGHT + "Tekan Enter untuk melanjutkan...")