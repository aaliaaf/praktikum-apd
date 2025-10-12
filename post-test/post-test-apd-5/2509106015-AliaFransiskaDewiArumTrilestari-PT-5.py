from prettytable import PrettyTable
import os

pengguna = [
    ["alia", "015", "admin"]
]

alat_berat = ["Excavator", "Bulldozer", "Compactor"]
tahun = [2010, 2020, 2005]
merek = ["Hitachi", "Caterpillar", "Bomag"]
status_alat = ["Siap Pakai", "Rusak", "Dalam Perbaikan"]

akses = ""

while True:
    os.system("cls" if os.name == "nt" else "clear")
    print("=== AKSES PENGELOLA ALAT BERAT ===")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")

    menu = input("Pilih menu (1-3): ")

    if menu == "1":
        print("=== LOGIN ADMIN ===")
        username = input("Masukkan Username: ").strip()
        password = input("Masukkan Password: ").strip()

        akses = ""
        for up in pengguna:
            if up[0] == username and up[1] == password:
                akses = up[2]
                break
        if akses == "":
            print("Username atau password salah")
        else:
            print(f"Login berhasil sebagai {akses}")


            while akses == "admin":
                    print("\n=== MENU PENGELOLA ALAT BERAT ===")
                    print("1. Create = Tambah alat berat baru")
                    print("2. Read = Tampilkan alat berat")
                    print("3. Update = Mengubah status alat berat")
                    print("4. Delete = Menghapus alat yang sudah tidak dipakai atau rusak")
                    print("5. Keluar")

                    pilihan = input("Pilih menu untuk pengelola alat berat (1-5): ")

                    # CREATE
                    if pilihan == "1":
                            print("\n=== TAMBAH ALAT BARU ===")
                            nama_alat_baru = input("Masukkan nama alat: ")
                            merek_alat_baru = input("Masukkan merek alat: ")
                            tahun_alat_baru = input("Masukkan tahun alat tersebut: ")
                            status_alat_baru = input("Masukkan status alat (Siap Pakai/Rusak/Dalam Perbaikan): ")
                            alat_berat.append(nama_alat_baru)
                            merek.append(merek_alat_baru)
                            tahun.append(tahun_alat_baru)
                            status_alat.append(status_alat_baru)
                            print(f'Alat: {nama_alat_baru}, Merek: {merek_alat_baru}, Tahun: {tahun_alat_baru}, Status: {status_alat_baru} Sudah Ditambahkan')
                            
                    # READ
                    elif pilihan == "2":
                            table = PrettyTable()
                            table.field_names = ["Nama", "Merek", "Tahun", "Status"]

                            for i in range(len(alat_berat)):
                                table.add_row([alat_berat[i], merek[i], tahun[i], status_alat[i]])
                            print(table)

                    # UPDATE
                    elif pilihan == "3":
                            print("\n=== UBAH STATUS ALAT ===")
                            if alat_berat == []:
                                print("Belum ada alat yang bisa diubah.")
                            else:
                                no = 0
                                for alat in alat_berat:
                                    print(no + 1, ".", alat, "-", status_alat[no])
                                    no = no + 1

                                ubah_status = int(input("Masukkan nomor alat yang ingin diubah: "))
                                status_baru = input("Masukkan status baru: ")

                                index = ubah_status - 1
                                status_alat[index] = status_baru
                                print(f"Status alat '{alat_berat[index]}' berhasil diubah")

                    # DELETE
                    elif pilihan == "4":
                            print("\n=== HAPUS ALAT BERAT ===")

                            if alat_berat == []:
                                print("Belum ada alat yang bisa dihapus.")
                            else:
                                no = 0
                                for alat in alat_berat:
                                    print(no + 1, ".", alat, "-", status_alat[no])
                                    no = no + 1
                                hapus = int(input("Masukkan nomor alat yang ingin dihapus: "))
                                status_dihapus = input("Kenapa ingin menghapus alat ini (Rusak/Ingin Diperbaiki): ")

                                index = hapus - 1 
                                dihapus = alat_berat[index]
                                del alat_berat[index]
                                del merek[index]
                                del tahun[index]
                                del status_alat[index]

                                print(f"Alat '{dihapus}' berhasil dihapus!")
                                print(f"Karena alat tersebuh {status_dihapus}")

                    elif pilihan == "5":
                            break
                    else:
                            print("Gunakan Urutan Nomor Pada Menu Yang Sudah Disediakan")
    elif menu == "2":
        print("=== MEMBUAT AKUN BARU ===")
        username = input("Masukkan username baru: ").strip()
        password = input("Masukkan password baru: ").strip()

        akses = ""
        for up in pengguna:
            if up[0] == username and up[1] == password:
                akses = up[2]
                break
        
        akses = "user"

        while akses == "user":
            print("\n=== MENU UNTUK USER ===")
            print("1. Tampilkan alat berat")
            print("2. Keluar")

            pilihan = input("Masukkan Nomor Pada Menu (1-2): ")

            if pilihan == "1":
                table = PrettyTable()
                table.field_names = ["Nama", "Merek", "Tahun", "Status"]

                for i in range(len(alat_berat)):
                    table.add_row([alat_berat[i], merek[i], tahun[i], status_alat[i]])
                print(table)
                # print("-" * 90)
                # print(f"| {'Nama Alat':<20} | {'Tahun':<10} | {'Merek':<20} | {'Status':<27} |")
                # print("-" * 90)

                # for i in range(len(alat_berat)):
                #     print(f"| {alat_berat[i]:<20} | {tahun[i]:<10} | {merek[i]:<20} | {status_alat[i]:<27} |")

                # print("-" * 90)

            elif pilihan == "2":
                break
            else:
                print("Gunakan Urutan Nomor Pada Menu Yang Sudah Disediakan")
    elif menu == "3":
            os.system("cls" if os.name == "nt" else "clear")
            print("Program berhenti")
            break
    else:
        print("Pilihan menu tidak sesuai")