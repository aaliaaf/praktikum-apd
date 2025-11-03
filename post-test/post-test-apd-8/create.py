from clear import clear
from read import alat_berat
from warna import judul, berhasil, gagal, enter, m, gumi

def tambah_alat():
    try:
        clear()
        print(judul + "=== TAMBAH ALAT BARU ===")
        nama = input(gumi + "Masukkan nama alat: ").strip()
        if nama in alat_berat:
            print(gagal + "Alat sudah ada!")
            return
        merek = input(gumi + "Masukkan merek: ").strip()
        tahun = int(input(gumi + "Masukkan tahun alat: "))
        status = input(gumi + "Masukkan status (Siap Pakai/Rusak/Dalam Perbaikan): ").strip()
        alat_berat[nama] = {"merek": merek, "tahun": tahun, "status": status}
        print(berhasil + f"Alat '{nama}' berhasil ditambahkan.")
    except ValueError:
        print(gagal + "Tahun harus berupa angka!")
    except Exception as e:
        print(gagal + f"Terjadi kesalahan: {e}")
