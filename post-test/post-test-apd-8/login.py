from clear import clear
from warna import judul, peringatan, berhasil, gagal, enter, m

pengguna = {
    "alia": {"password": "015", "akses": "admin"}
}

def login():
    clear()
    print(judul + "=== LOGIN ===")
    username = input("Masukkan Username: ").strip()
    password = input("Masukkan Password: ").strip()

    if username in pengguna and pengguna[username]["password"] == password:
        print(judul + f"Login berhasil sebagai {pengguna[username]['akses']}")
        input(enter + "Tekan Enter untuk melanjutkan...")
        return username  
    else:
        print(gagal + "Username atau password salah!")
        ulang = input("Apakah ingin login ulang? (y/n): ").strip().lower()
        if ulang == "y":
            return login() 
        else:
            input(enter + "Tekan Enter untuk kembali ke menu...")
            return None

