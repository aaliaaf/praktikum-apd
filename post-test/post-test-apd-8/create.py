from bersih import clear
from read import alat_berat
from colorama import Fore, Style, init
init(autoreset=True)

def tambah_alat():
    try:
        clear()
        print(Fore.BLUE + Style.BRIGHT + "=== TAMBAH ALAT BARU ===")
        nama = input(Fore.MAGENTA + Style.BRIGHT + "Masukkan nama alat: ").strip()
        if nama in alat_berat:
            print(Fore.RED + Style.BRIGHT + "Alat sudah ada!")
            return
        merek = input(Fore.MAGENTA + Style.BRIGHT + "Masukkan merek: ").strip()
        tahun = int(input(Fore.MAGENTA + Style.BRIGHT + "Masukkan tahun alat: "))
        status = input(Fore.MAGENTA + Style.BRIGHT + "Masukkan status (Siap Pakai/Rusak/Dalam Perbaikan): ").strip()
        alat_berat[nama] = {"merek": merek, "tahun": tahun, "status": status}
        print(Fore.GREEN + Style.BRIGHT + f"Alat '{nama}' berhasil ditambahkan.")
    except ValueError:
        print(Fore.RED + Style.BRIGHT + "Tahun harus berupa angka!")
    except Exception as e:
        print(Fore.RED + Style.BRIGHT + f"Terjadi kesalahan: {e}")