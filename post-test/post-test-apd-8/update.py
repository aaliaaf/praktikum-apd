from read import alat_berat
from warna import judul, berhasil, gagal, enter, m, gumi

def ubah_status(alat, status_baru):
    if alat in alat_berat:
        alat_berat[alat]["status"] = status_baru
        print(berhasil + f"Status alat '{alat}' berhasil diubah menjadi '{status_baru}'")
    else:
        print(gagal + "Tidak ada alat tersebut")
