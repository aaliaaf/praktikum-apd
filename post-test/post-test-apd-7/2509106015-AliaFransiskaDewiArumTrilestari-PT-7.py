from prettytable import PrettyTable
import os

pengguna = {
    "alia": {"password": "015", "akses": "admin"}
}
alat_berat = {
    "Excavator": {"merek": "Hitachi", "tahun": 2010, "status": "Siap Pakai"},
    "Bulldozer": {"merek": "Caterpillar", "tahun": 2020, "status": "Rusak"},
    "Compactor": {"merek": "Bomag", "tahun": 2005, "status": "Dalam Perbaikan"}
}

login_user = ""

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def tampilkan_alat():
    clear()
    print("=== DAFTAR ALAT BERAT ===")
    table = PrettyTable()
    table.field_names = ["Nama", "Merek", "Tahun", "Status"]
    for nama, value in alat_berat.items():
        table.add_row([nama, value["merek"], value["tahun"], value["status"]])
    print(table)

def ubah_status(alat, status_baru):
    if alat in alat_berat:
        alat_berat[alat]["status"] = status_baru
        print(f"Status alat '{alat}' berhasil diubah menjadi '{status_baru}'")
    else:
        print("Tidak ada alat tersebut")

def tambah_alat():
    try:
        clear()
        print("=== TAMBAH ALAT BARU ===")
        nama = input("Masukkan nama alat: ").strip()
        if nama in alat_berat:
            print("Alat sudah ada!")
            return
        merek = input("Masukkan merek: ").strip()
        tahun = int(input("Masukkan tahun alat: "))
        status = input("Masukkan status (Siap Pakai/Rusak/Dalam Perbaikan): ").strip()
        alat_berat[nama] = {"merek": merek, "tahun": tahun, "status": status}
        print(f"Alat '{nama}' berhasil ditambahkan.")
    except ValueError:
        print("Tahun harus berupa angka!")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

def hapus_alat():
    clear()
    alat = input("Masukkan nama alat yang ingin dihapus: ").strip()
    if alat in alat_berat:
        alasan = input("Alasan dihapus (Rusak/Ingin diperbaiki): ").strip()
        alat_berat.pop(alat)
        print(f"Alat '{alat}' dihapus karena '{alasan}'.")
    else:
        print("Tidak ada alat tersebut")

def login():
    clear()
    print("=== LOGIN ===")
    username = input("Masukkan Username: ").strip()
    password = input("Masukkan Password: ").strip()

    if username in pengguna and pengguna[username]["password"] == password:
        print(f"Login berhasil sebagai {pengguna[username]['akses']}")
        input("Tekan Enter untuk melanjutkan...")
        return username  
    else:
        print("Username atau password salah! Coba lagi.\n")
        ulang = input("Apakah ingin login ulang? (y/n): ").strip().lower()
        if ulang == "y":
            return login() 
        else:
            input("Tekan Enter untuk kembali ke menu...")
            return None

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

                pilihan = input("Pilih menu (1-5): ")
                if pilihan == "1":
                    tambah_alat()
                elif pilihan == "2":
                    tampilkan_alat()
                elif pilihan == "3":
                    clear()
                    alat = input("Masukkan nama alat yang mau diubah: ").strip()
                    status_baru = input("Masukkan status baru (Siap Pakai/Rusak/Dalam Perbaikan) : ").strip()
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
                print("1. Lihat alat berat")
                print("2. Keluar")

                pilihan = input("Pilih menu (1-3): ")

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
        username = input("Masukkan username baru: ").strip()
        password = input("Masukkan password baru: ").strip()

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
