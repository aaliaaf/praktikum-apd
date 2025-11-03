from bersih import clear
from read import alat_berat


def ubah_status(alat, status_baru):
    if alat in alat_berat:
        alat_berat[alat]["status"] = status_baru
        print(f"Status alat '{alat}' berhasil diubah menjadi '{status_baru}'")
    else:
        print("Tidak ada alat tersebut")
