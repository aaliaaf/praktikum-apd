from bersih import clear
from read import alat_berat

def tambah_alat():
    try:
        clear()
        print("=== TAMBAH ALAT BARU ===")
        nama = input("Masukkan nama alat: ").strip()
        if nama in alat_berat:
            print("Alat sudah ada!")
            return
        merek = input("Masukkan merek: ").strip()
        tahun = int(input("Masukkan tahun alat: "))
        status = input("Masukkan status (Siap Pakai/Rusak/Dalam Perbaikan): ").strip()
        alat_berat[nama] = {"merek": merek, "tahun": tahun, "status": status}
        print(f"Alat '{nama}' berhasil ditambahkan.")
    except ValueError:
        print("Tahun harus berupa angka!")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")