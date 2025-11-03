from bersih import clear
from read import alat_berat
from colorama import Fore, Style, init
init(autoreset=True)


def ubah_status(alat, status_baru):
    if alat in alat_berat:
        alat_berat[alat]["status"] = status_baru
        print(Fore.GREEN + Style.BRIGHT + f"Status alat '{alat}' berhasil diubah menjadi '{status_baru}'")
    else:
        print(Fore.RED + Style.BRIGHT + "Tidak ada alat tersebut")
