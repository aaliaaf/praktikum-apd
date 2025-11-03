from bersih import clear

pengguna = {
    "alia": {"password": "015", "akses": "admin"}
}

def login():
    clear()
    print("=== LOGIN ===")
    username = input("Masukkan Username: ").strip()
    password = input("Masukkan Password: ").strip()

    if username in pengguna and pengguna[username]["password"] == password:
        print(f"Login berhasil sebagai {pengguna[username]['akses']}")
        input("Tekan Enter untuk melanjutkan...")
        return username  
    else:
        print("Username atau password salah! Coba lagi.\n")
        ulang = input("Apakah ingin login ulang? (y/n): ").strip().lower()
        if ulang == "y":
            return login() 
        else:
            input("Tekan Enter untuk kembali ke menu...")
            return None