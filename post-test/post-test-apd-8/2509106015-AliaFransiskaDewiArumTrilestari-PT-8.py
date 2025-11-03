from clear import clear
from create import tambah_alat
from delete import hapus_alat
from login import login
from read import tampilkan_alat
from update import ubah_status
from login import pengguna
from warna import judul, berhasil, gagal, enter, m, gumi

login_user = ""

while True:
    clear()
    print(judul + "=== SISTEM PENGELOLA ALAT BERAT ===")
    print(m + "1. Login")
    print(m + "2. Register")
    print(m + "3. Keluar")

    menu = input(judul + "Pilih menu (1-3): ")

    if menu == "1":
        login_user = login() 
        if login_user is None:
            continue

        akses = pengguna[login_user]["akses"]

        # === MENU ADMIN ===
        if akses == "admin":
            while True:
                clear()
                print(judul + f"=== MENU ADMIN ({login_user}) ===")
                print(m + "1. Tambah alat baru")
                print(m + "2. Lihat semua alat")
                print(m + "3. Ubah status alat")
                print(m + "4. Hapus alat")
                print(m + "5. Keluar")

                pilihan = input(gumi + "Pilih menu (1-5): ")
                if pilihan == "1":
                    tambah_alat()
                elif pilihan == "2":
                    tampilkan_alat()
                elif pilihan == "3":
                    clear()
                    alat = input(gumi + "Masukkan nama alat yang mau diubah: ").strip()
                    status_baru = input(gumi + "Masukkan status baru (Siap Pakai/Rusak/Dalam Perbaikan) : ").strip()
                    ubah_status(alat, status_baru)
                elif pilihan == "4":
                    hapus_alat()
                elif pilihan == "5":
                    break
                else:
                    print(gagal + "Gunakan nomor menu yang sudah disediakan!")
                input(enter + "Tekan Enter untuk melanjutkan...")
        # === MENU USER ===
        else:
            while True:
                clear()
                print(judul + f"=== MENU USER ({login_user}) ===")
                print(menu + "1. Lihat alat berat")
                print(menu + "2. Keluar")

                pilihan = input(gumi + "Pilih menu (1-2): ")

                if pilihan == "1":
                    tampilkan_alat()
                elif pilihan == "2":
                    break
                else:
                    print(gagal + "Gunakan menu 1-3!")
                input(enter + "Tekan Enter untuk melanjutkan...")
    # === REGISTER ===
    elif menu == "2":
        clear()
        print(judul + "=== REGISTER AKUN BARU ===")
        username = input(gumi + "Masukkan username baru: ").strip()
        password = input(gumi + "Masukkan password baru: ").strip()

        if username in pengguna:
            print(gagal + "Username sudah terdaftar!")
        else:
            pengguna[username] = {"password": password, "akses": "user"}
            print(f"Akun '{username}' berhasil dibuat sebagai user!")
        input(enter + "Tekan Enter untuk melanjutkan...")

    elif menu == "3":
        clear()
        print(judul + "Program berhenti.")
        break

    else:
        clear()
        print(gagal + "Pilihan menu tidak sesuai! Gunakan nomor menu yang sudah disediakan!")
        input(enter + "Tekan Enter untuk melanjutkan...")
