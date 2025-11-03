from clear import clear
from create import tambah_alat
from delete import hapus_alat
from login import login
from read import tampilkan_alat
from update import ubah_status
from login import pengguna

login_user = ""

while True:
    clear()
    print("=== SISTEM PENGELOLA ALAT BERAT ===")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")

    menu = input("Pilih menu (1-3): ")

    if menu == "1":
        login_user = login() 
        if login_user is None:
            continue

        akses = pengguna[login_user]["akses"]

        # === MENU ADMIN ===
        if akses == "admin":
            while True:
                clear()
                print(f"=== MENU ADMIN ({login_user}) ===")
                print("1. Tambah alat baru")
                print("2. Lihat semua alat")
                print("3. Ubah status alat")
                print("4. Hapus alat")
                print("5. Keluar")

                pilihan = input( "Pilih menu (1-5): ")
                if pilihan == "1":
                    tambah_alat()
                elif pilihan == "2":
                    tampilkan_alat()
                elif pilihan == "3":
                    clear()
                    alat = input( "Masukkan nama alat yang mau diubah: ").strip()
                    status_baru = input( "Masukkan status baru (Siap Pakai/Rusak/Dalam Perbaikan) : ").strip()
                    ubah_status(alat, status_baru)
                elif pilihan == "4":
                    hapus_alat()
                elif pilihan == "5":
                    break
                else:
                    print("Gunakan nomor menu yang sudah disediakan!")
                input("Tekan Enter untuk melanjutkan...")
        # === MENU USER ===
        else:
            while True:
                clear()
                print(f"=== MENU USER ({login_user}) ===")
                print(menu + "1. Lihat alat berat")
                print(menu + "2. Keluar")

                pilihan = input( "Pilih menu (1-2): ")

                if pilihan == "1":
                    tampilkan_alat()
                elif pilihan == "2":
                    break
                else:
                    print("Gunakan menu 1-3!")
                input("Tekan Enter untuk melanjutkan...")
    # === REGISTER ===
    elif menu == "2":
        clear()
        print("=== REGISTER AKUN BARU ===")
        username = input( "Masukkan username baru: ").strip()
        password = input( "Masukkan password baru: ").strip()

        if username in pengguna:
            print("Username sudah terdaftar!")
        else:
            pengguna[username] = {"password": password, "akses": "user"}
            print(f"Akun '{username}' berhasil dibuat sebagai user!")
        input("Tekan Enter untuk melanjutkan...")

    elif menu == "3":
        clear()
        print("Program berhenti.")
        break

    else:
        clear()
        print("Pilihan menu tidak sesuai! Gunakan nomor menu yang sudah disediakan!")
        input("Tekan Enter untuk melanjutkan...")
