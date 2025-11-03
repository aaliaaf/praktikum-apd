from bersih import clear
from colorama import Fore, Style, init
init(autoreset=True)

pengguna = {
    "alia": {"password": "015", "akses": "admin"}
}

def login():
    clear()
    print(Fore.BLUE + Style.BRIGHT + "=== LOGIN ===")
    username = input(Fore.MAGENTA + Style.BRIGHT + "Masukkan Username: ").strip()
    password = input(Fore.MAGENTA + Style.BRIGHT + "Masukkan Password: ").strip()

    if username in pengguna and pengguna[username]["password"] == password:
        print(Fore.GREEN + Style.BRIGHT + f"Login berhasil sebagai {pengguna[username]['akses']}")
        input(Fore.CYAN + Style.BRIGHT + "Tekan Enter untuk melanjutkan...")
        return username  
    else:
        print(Fore.RED + Style.BRIGHT + "Username atau password salah! Coba lagi.")
        ulang = input(Fore.MAGENTA + Style.BRIGHT + "Apakah ingin login ulang? (y/n): ").strip().lower()
        if ulang == "y":
            return login() 
        else:
            input(Fore.CYAN + Style.BRIGHT + "Tekan Enter untuk kembali ke menu...")
            return None