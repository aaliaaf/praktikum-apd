from bersih import clear
from read import alat_berat

def hapus_alat():
    clear()
    alat = input("Masukkan nama alat yang ingin dihapus: ").strip()
    if alat in alat_berat:
        alasan = input("Alasan dihapus (Rusak/Ingin diperbaiki): ").strip()
        alat_berat.pop(alat)
        print(f"Alat '{alat}' dihapus karena '{alasan}'.")
    else:
        print("Tidak ada alat tersebut")
