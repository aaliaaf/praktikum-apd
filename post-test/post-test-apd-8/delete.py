from clear import clear
from read import alat_berat
from warna import judul, berhasil, gagal, enter, m, gumi

def hapus_alat():
    clear()
    alat = input(gumi + "Masukkan nama alat yang ingin dihapus: ").strip()
    if alat in alat_berat:
        alasan = input(gumi + "Alasan dihapus (Rusak/Ingin diperbaiki): ").strip()
        alat_berat.pop(alat)
        print(berhasil + f"Alat '{alat}' dihapus karena '{alasan}'.")
    else:
        print(gagal + "Tidak ada alat tersebut")