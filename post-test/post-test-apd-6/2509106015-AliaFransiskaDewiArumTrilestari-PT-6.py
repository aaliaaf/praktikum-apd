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

while True:
    os.system("cls" if os.name == "nt" else "clear")
    print("=== SISTEM PENGELOLA ALAT BERAT ===")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")

    menu = input("Pilih menu (1-3): ")

    os.system("cls" if os.name == "nt" else "clear")

    # LOGIN
    if menu == "1":
        print("=== LOGIN ===")
        username = input("Masukkan Username: ").strip()
        password = input("Masukkan Password: ").strip()

        if username in pengguna and pengguna[username]["password"] == password:
            akses = pengguna[username]["akses"]
            print(f"Login berhasil sebagai {akses}")
            input("Tekan Enter untuk melanjutkan...")
        else:
            print("Username atau password salah!")
            input("Tekan Enter untuk melanjutkan...")
            continue #melewati sisa kode dlm loop

        # MENU ADMIN
        while akses == "admin":
            os.system("cls" if os.name == "nt" else "clear")
            print("=== MENU ADMIN ===")
            print("1. Tambah alat baru")
            print("2. Lihat semua alat")
            print("3. Ubah status alat")
            print("4. Hapus alat")
            print("5. Keluar")

            pilihan = input("Pilih menu (1-5): ")

            # CREATE
            if pilihan == "1":
                os.system("cls" if os.name == "nt" else "clear")
                print("=== TAMBAH ALAT BARU ===")
                alat = input("Masukkan nama alat: ").strip()

                if alat in alat_berat:
                    print("Alat sudah tersedia!")
                else:
                    merek = input("Masukkan merek alat: ").strip()
                    tahun_input = int(input("Masukkan tahun alat: "))
                    status = input("Masukkan status alat (Siap Pakai/Rusak/Dalam Perbaikan): ").strip()

                    alat_berat.update({
                        alat: {"merek": merek, "tahun": tahun_input, "status": status}
                    })

                    print(f"Alat '{alat}' berhasil ditambahkan.")
                input("Tekan Enter untuk melanjutkan...")

            # READ
            elif pilihan == "2":
                os.system("cls" if os.name == "nt" else "clear")
                print("=== DAFTAR ALAT BERAT ===")
                table = PrettyTable()
                table.field_names = ["Nama", "Merek", "Tahun", "Status"]
                for nama, value in alat_berat.items():
                    table.add_row([nama, value["merek"], value["tahun"], value["status"]])
                print(table)
                input("Tekan Enter untuk melanjutkan...")

            # UPDATE
            elif pilihan == "3":
                os.system("cls" if os.name == "nt" else "clear")
                print("=== UBAH STATUS ALAT ===")
                alat = input("Masukkan nama alat yang ingin diubah: ").strip()
                if alat in alat_berat:
                    status_baru = input("Masukkan status baru (Siap Pakai/Rusak/Dalam Perbaikan): ").strip()
                    alat_berat[alat].update({"status": status_baru})
                    print(f"Status alat '{alat}' berhasil diubah menjadi '{status_baru}'")
                else:
                    print("Tidak ada alat tersebut")
                input("Tekan Enter untuk melanjutkan...")

            # DELETE
            elif pilihan == "4":
                os.system("cls" if os.name == "nt" else "clear")
                print("=== HAPUS ALAT ===")
                alat = input("Masukkan nama alat yang ingin dihapus: ").strip()
                if alat in alat_berat:
                    alat_berat.pop(alat)
                    status_dihapus = input("Kenapa ingin menghapus alat ini (Rusak/Ingin Diperbaiki): ")
                    print(f"Alat '{alat}' berhasil dihapus, karena '{status_dihapus}'.")
                else:
                    print("Tidak ada alat tersebut")
                input("Tekan Enter untuk melanjutkan...")

            elif pilihan == "5":
                break
            else:
                print("Gunakan nomor menu yang sudah disediakan")
                input("Tekan Enter untuk melanjutkan...")

    # REGISTER
    elif menu == "2":
        os.system("cls" if os.name == "nt" else "clear")
        print("=== REGISTER AKUN BARU ===")
        username = input("Masukkan username baru: ").strip()
        password = input("Masukkan password baru: ").strip()

        if username in pengguna:
            print("Username sudah terdaftar!")
        else:
            pengguna[username] = {"password": password, "akses": "user"}
            print(f"Akun '{username}' berhasil dibuat sebagai user!")

        input("Tekan Enter untuk melanjutkan...")

        akses = "user"
        while akses == "user":
            os.system("cls" if os.name == "nt" else "clear")
            print("\n=== MENU USER ===")
            print("1. Tampilkan alat berat")
            print("2. Keluar")

            pilihan = input("Masukkan Nomor Pada Menu (1-2): ")

            if pilihan == "1":
                os.system("cls" if os.name == "nt" else "clear")
                print("=== DAFTAR ALAT BERAT ===")
                table = PrettyTable()
                table.field_names = ["Nama", "Merek", "Tahun", "Status"]
                for nama, data in alat_berat.items():
                    table.add_row([nama, data["merek"], data["tahun"], data["status"]])
                print(table)
                input("Tekan Enter untuk melanjutkan...")
            elif pilihan == "2":
                break
            else:
                print("Gunakan urutan nomor yang sudah disediakan.")
                input("Tekan Enter untuk melanjutkan...")

    elif menu == "3":
        os.system("cls" if os.name == "nt" else "clear")
        print("Program berhenti.")
        break
    else:
        print("Pilihan menu tidak sesuai.")
        input("Tekan Enter untuk melanjutkan...")
