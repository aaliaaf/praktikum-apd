from bersih import clear
from read import alat_berat
from colorama import Fore, Style, init
init(autoreset=True)

def hapus_alat():
    clear()
    alat = input(Fore.MAGENTA + Style.BRIGHT + "Masukkan nama alat yang ingin dihapus: ").strip()
    if alat in alat_berat:
        alasan = input(Fore.MAGENTA + Style.BRIGHT + "Alasan dihapus (Rusak/Ingin diperbaiki): ").strip()
        alat_berat.pop(alat)
        print(Fore.GREEN + Style.BRIGHT + f"Alat '{alat}' dihapus karena '{alasan}'.")
    else:
        print(Fore.RED + Style.BRIGHT + "Tidak ada alat tersebut")
