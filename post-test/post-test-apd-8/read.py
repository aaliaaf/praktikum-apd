from bersih import clear
from prettytable import PrettyTable
from colorama import Fore, Style, init
init(autoreset=True)

alat_berat = {
    "Excavator": {"merek": "Hitachi", "tahun": 2010, "status": "Siap Pakai"},
    "Bulldozer": {"merek": "Caterpillar", "tahun": 2020, "status": "Rusak"},
    "Compactor": {"merek": "Bomag", "tahun": 2005, "status": "Dalam Perbaikan"}
}

def tampilkan_alat():
    clear()
    print(Fore.BLUE + Style.BRIGHT +"=== DAFTAR ALAT BERAT ===")
    table = PrettyTable()
    table.field_names = ["Nama", "Merek", "Tahun", "Status"]
    for nama, value in alat_berat.items():
        table.add_row([nama, value["merek"], value["tahun"], value["status"]])
    print(Fore.GREEN + Style.NORMAL + str(table))