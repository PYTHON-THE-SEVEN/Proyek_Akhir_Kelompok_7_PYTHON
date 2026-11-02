import json
import pwinput
from prettytable import PrettyTable
from datetime import datetime
import os

RESET = "\033[0m"
TEBAL = "\033[1m"
MERAH = "\033[91m"
HIJAU = "\033[92m"
KUNING = "\033[93m"
BIRU = "\033[94m"
UNGU = "\033[95m"
CYAN = "\033[96m"

def input_aman(prompt=""):
    while True:
        try:
            return input(prompt)
        except KeyboardInterrupt:
            print("\nInput dibatalkan. Silakan masukkan lagi pada bagian ini.")

def password_aman(prompt=""):
    while True:
        try:
            return pwinput.pwinput(prompt)
        except KeyboardInterrupt:
            print("\nInput password dibatalkan. Silakan masukkan lagi.")
pengguna_aktif = None

#PERDATAAN
def bersih():
    os.system('cls' if os.name == 'nt' else 'clear')

def jalankan_aman(perintah):
    try:
        perintah()
    except KeyboardInterrupt:
        print("\nPerintah dibatalkan. Kembali ke menu.")
def load_data1():
    try:
        with open("users (1).json", "r", encoding="utf-8-sig") as file:
            data = json.load(file)
            if not isinstance(data, list):
                print(f"{MERAH}❌ Format users harus berupa daftar akun.{RESET}")
                return []
            return data
    except FileNotFoundError:
        print(f"{MERAH}❌ File users (1).json tidak ditemukan.{RESET}")
        return []
    except json.JSONDecodeError as error:
        print(f"{MERAH}❌ Isi users (1).json tidak valid: {error}{RESET}")
        return []
    except OSError as error:
        print(f"{MERAH}❌ Gagal membaca file users: {error}{RESET}")
        return []


def load_data2():
    try:
        with open("produk (1).json", "r", encoding="utf-8-sig") as file:
            data = json.load(file)
            if not isinstance(data, list):
                print(f"{MERAH}❌ Format produk harus berupa daftar barang.{RESET}")
                return []
            return data
    except FileNotFoundError:
        print(f"{MERAH}❌ File produk (1).json tidak ditemukan.{RESET}")
        return []
    except json.JSONDecodeError as error:
        print(f"{MERAH}❌ Isi produk (1).json tidak valid: {error}{RESET}")
        return []
    except OSError as error:
        print(f"{MERAH}❌ Gagal membaca file produk: {error}{RESET}")
        return []


def save_data(data):
    try:
        with open("users (1).json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
        return True
    except OSError as error:
        print(f"{MERAH}❌ Gagal menyimpan data akun: {error}{RESET}")
        return False


def save_produk(data):
    try:
        with open("produk (1).json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
        return True
    except OSError as error:
        print(f"{MERAH}❌ Gagal menyimpan data produk: {error}{RESET}")
        return False
#AKUN
def regis():
    print(f"\n{CYAN}{TEBAL}📝 MENU REGISTRASI{RESET}")
    users = load_data1()
    if users is None:
        users = []
    while True:
        username = input_aman("Masukkan username baru: ")
        dupli = False
        for u in users:
            if u.get("user") == username:
                dupli = True
                break
        if dupli:
            print(f"{KUNING}⚠️ Username sudah terpakai.{RESET}")
        else:
            break
    password = input_aman("Masukkan password baru: ")
    if username.lower() == "admin":
        role = "admin"
    else:
        role = "user"
    new_user = {
        "user": username, 
        "pw": password, 
        "role": role, 
        "saldo": 0,
        "riwayat": []
    }
    users.append(new_user)
    save_data(users)
    print(f"{HIJAU}✅ Registrasi berhasil! Silakan login.{RESET}")
def login():
    print(f"\n{CYAN}{TEBAL}🔐 LOGIN{RESET}")
    users = load_data1()
    if not users:
        print(f"{KUNING}⚠️ Belum ada akun. Silakan registrasi dulu.{RESET}")
        return
    username = input_aman("Masukkan Username : ")
    password = password_aman("Masukkan password : ")
    log = None 
    for u in users:
        if u.get("user") == username and u.get("pw") == password:
            log = u
            break
    if log:
        global pengguna_aktif
        pengguna_aktif = log["user"]
        print(f"{HIJAU}✅ LOGIN BERHASIL{RESET}")
        role = log.get("role", "user")
        if role == "admin":
            AdminPanel()
        else:
            UserPanel()
    else:
        print(f"{MERAH}❌ Username atau password salah.{RESET}")

#DEF ADMIN
def tambah():
    bersih()
    print(f"\n{CYAN}{TEBAL}📦 TAMBAH DATA BARANG{RESET}")
    produk = load_data2()
    nama = input_aman("Masukkan Nama Barang : ")
    kode = input_aman("Masukkan Kode Barang : ")
    while True:
        try:
            harga = int(input_aman("Masukkan Harga Barang: "))
            if harga < 0:
                print(f"{KUNING}⚠️ Harga tidak valid.{RESET}")
                continue
            break
        except ValueError:
            print(f"{KUNING}⚠️ Harga harus berupa angka.{RESET}")
        except KeyboardInterrupt:
            print(f"{KUNING}⚠️ Input dibatalkan. Silakan lanjutkan lagi.{RESET}")
    while True:
        try:
            stok = int(input_aman("Stok Barang : "))
            if stok < 0:
                print(f"{KUNING}⚠️ Jumlah stok tidak valid.{RESET}")
                continue
            break
        except ValueError:
            print(f"{KUNING}⚠️ Stok harus berupa angka.{RESET}")
        except KeyboardInterrupt:
            print(f"{KUNING}⚠️ Input dibatalkan. Silakan lanjutkan lagi.{RESET}")
        
    new_item = {
        "nama": nama,
        "kode": kode,
        "harga": harga,
        "stok": stok
    }
    produk.append(new_item)

    if not save_produk(produk):
        return

    print(f"{HIJAU}✅ Barang berhasil ditambahkan!{RESET}")
def ubah():
    produk = load_data2()
    if not produk:
        print(f"{KUNING}⚠️ Tidak ada data yang bisa diubah.{RESET}")
    else:
        lihat()
        while True:
                try:
                    pili = int(input_aman("Pilih data yang mau di ubah: ")) - 1
                    if 0 <= pili < len(produk):
                        nama = input_aman("Masukkan Nama Barang baru : ")
                        kode = input_aman("Masukkan Kode baru : ")
                        while True:
                            try:
                                harga = int(input_aman("Masukkan Harga Baru : "))
                                if harga < 0:
                                    print(f"{KUNING}⚠️ Harga tidak valid.{RESET}")
                                    continue
                                break
                            except ValueError:
                                print(f"{KUNING}⚠️ Masukkan angka yang benar.{RESET}")
                        while True:
                            try:
                                stok = int(input_aman("Masukkan Stok Baru : "))
                                if stok < 0:
                                    print(f"{KUNING}⚠️ Masukkan angka yang benar.{RESET}")
                                    continue
                                break
                            except ValueError:
                                print(f"{KUNING}⚠️ Masukkan angka yang benar.{RESET}")
                        produk[pili] = {"nama": nama, "kode": kode, "harga": harga, "stok": stok}
                        save_produk(produk)
                        print(f"{HIJAU}✅ Data berhasil diperbarui.{RESET}")
                        break
                    else:
                        print(f"{KUNING}⚠️ Nomor data tidak tersedia.{RESET}")
                except ValueError:
                    print(f"{KUNING}⚠️ Nomor data tidak tersedia.{RESET}")
def lihat():
    bersih()
    print(f"\n{CYAN}{TEBAL}🛍️ DAFTAR BARANG{RESET}")
    produk = load_data2()
    if not produk:
        print(f"{KUNING}📭 Belum ada barang yang tersedia.{RESET}")
    else:
        tabel = PrettyTable()
        tabel.field_names = ["No", "Nama Barang", "Kode", "Harga", "Stok"]
        for i, p in enumerate(produk, 1):
            tabel.add_row([i, p["nama"], p["kode"], p["harga"], p["stok"]])
        print(f"{CYAN}{tabel}{RESET}")
def hapus():
    bersih()
    produk = load_data2()
    if not produk:
        print(f"{KUNING}⚠️ Tidak ada data yang bisa diubah.{RESET}")
    else:
        lihat()
        try:
            hapus = int(input_aman("Pilih data yang mau dihapus : ")) - 1
            if 0 <= hapus < len(produk):
                produk.pop(hapus)
                save_produk(produk)
            else:
                print(f"{KUNING}⚠️ Data tidak ditemukan.{RESET}")
        except ValueError:
            print(f"{KUNING}⚠️ Masukkan angka yang benar.{RESET}")

        lihat()
def lihat_user():
    bersih()
    print(f"\n{CYAN}{TEBAL}👥 DAFTAR PENGGUNA{RESET}")
    akun = load_data1()

    if not akun:
        print(f"{KUNING}📭 Belum ada data pengguna.{RESET}")
        return

    tabel = PrettyTable()
    tabel.field_names = ["No", "Username", "Role", "Saldo"]

    for nomor, user in enumerate(akun, 1):
        tabel.add_row([
            nomor,
            user.get("user", "-"),
            user.get("role", "-"),
            user.get("saldo", 0)
        ])

    print(f"{CYAN}{tabel}{RESET}")
#DEF USER
def pesan():
    # Memuat data terbaru agar saldo, stok, dan riwayat tetap sinkron.
    users = load_data1() or []
    produk = load_data2() or []

    if not pengguna_aktif:
        print(f"{KUNING}🔐 Silakan login terlebih dahulu.{RESET}")
        return

    akun = None
    for user in users:
        if user.get("user") == pengguna_aktif:
            akun = user
            break

    if akun is None:
        print(f"{MERAH}❌ Data akun tidak ditemukan.{RESET}")
        return

    if not produk:
        print(f"{KUNING}📭 Belum ada barang yang tersedia.{RESET}")
        return

    tabel = PrettyTable()
    tabel.field_names = ["No", "Nama Barang", "Kode", "Harga", "Stok"]
    for nomor, barang in enumerate(produk, 1):
        tabel.add_row([
            nomor, barang.get("nama", "-"), barang.get("kode", "-"),
            barang.get("harga", 0), barang.get("stok", 0)
        ])
    print(f"{CYAN}{tabel}{RESET}")
    print(f"{HIJAU}💳 Saldo Anda: Rp {akun.get('saldo', 0):,}".replace(",", ".") + RESET)

    try:
        pilihan = int(input_aman("Pilih nomor barang yang ingin dibeli: "))
        if pilihan < 1 or pilihan > len(produk):
            print(f"{KUNING}⚠️ Nomor barang tidak tersedia.{RESET}")
            return

        barang = produk[pilihan - 1]
        jumlah = int(input_aman("Masukkan jumlah yang ingin dibeli: "))
        if jumlah <= 0:
            print(f"{KUNING}⚠️ Jumlah pembelian harus lebih dari 0.{RESET}")
            return
        if jumlah > barang.get("stok", 0):
            print(f"{KUNING}⚠️ Stok barang tidak mencukupi.{RESET}")
            return

        total = barang.get("harga", 0) * jumlah
        if total > akun.get("saldo", 0):
            print(f"{KUNING}💳 Saldo tidak cukup. Silakan top up terlebih dahulu.{RESET}")
            return

        # Transaksi berhasil: perbarui saldo, stok, dan riwayat.
        akun["saldo"] -= total
        barang["stok"] -= jumlah
        transaksi = {
            "tanggal": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            "nama_barang": barang.get("nama", "-"),
            "kode_barang": barang.get("kode", "-"),
            "jumlah": jumlah,
            "harga_satuan": barang.get("harga", 0),
            "total_harga": total,
            "status": "Berhasil"
        }
        if not isinstance(akun.get("riwayat"), list):
            akun["riwayat"] = []
        akun["riwayat"].append(transaksi)

        save_data(users)
        save_produk(produk)

        print(f"\n{HIJAU}{TEBAL}╔══════════════════════════════════════╗{RESET}")
        print(f"{HIJAU}{TEBAL}║          🧾 INVOICE PEMESANAN         ║{RESET}")
        print(f"{HIJAU}{TEBAL}╚══════════════════════════════════════╝{RESET}")
        print(f"👤 Nama pengguna : {akun['user']}")
        print(f"📅 Tanggal       : {transaksi['tanggal']}")
        print(f"📦 Nama barang   : {transaksi['nama_barang']}")
        print(f"🔖 Kode barang   : {transaksi['kode_barang']}")
        print(f"🔢 Jumlah        : {jumlah}")
        print(f"💵 Harga satuan  : Rp {transaksi['harga_satuan']:,}".replace(",", "."))
        print(f"💳 Total bayar   : Rp {total:,}".replace(",", "."))
        print(f"💰 Sisa saldo    : Rp {akun['saldo']:,}".replace(",", "."))
        print(f"✅ Status        : {transaksi['status']}")
        print(f"{HIJAU}{TEBAL}🎉 Terima kasih sudah berbelanja!{RESET}")
    except ValueError:
        print(f"{KUNING}⚠️ Input harus berupa angka.{RESET}")
    except FileNotFoundError:
        print(f"{MERAH}❌ File data tidak ditemukan. Periksa file JSON.{RESET}")


def riwayat():
    users = load_data1() or []

    if not pengguna_aktif:
        print(f"{KUNING}🔐 Silakan login terlebih dahulu.{RESET}")
        return

    akun = None
    for user in users:
        if user.get("user") == pengguna_aktif:
            akun = user
            break

    if akun is None:
        print(f"{MERAH}❌ Data akun tidak ditemukan.{RESET}")
        return

    daftar_riwayat = akun.get("riwayat", [])
    print("\n=== RIWAYAT PEMESANAN ===")
    if not daftar_riwayat:
        print(f"📭 Anda belum memiliki riwayat pemesanan.")
        return

    tabel = PrettyTable()
    tabel.field_names = [
        "No", "Tanggal", "Nama Barang", "Kode", "Jumlah",
        "Harga Satuan", "Total", "Status"
    ]

    total_belanja = 0
    for nomor, transaksi in enumerate(daftar_riwayat, 1):
        if transaksi.get("tipe") == "topup":
            tabel.add_row([
                nomor,
                transaksi.get("waktu", "-"),
                "Top up saldo",
                "-",
                "-",
                "-",
                f"Rp {transaksi.get('jumlah', 0):,}",
                "Berhasil"
            ])
        else:
            total = transaksi.get("total_harga", 0)
            total_belanja += total
            tabel.add_row([
                nomor,
                transaksi.get("tanggal", "-"),
                transaksi.get("nama_barang", "-"),
                transaksi.get("kode_barang", "-"),
                transaksi.get("jumlah", 0),
                f"Rp {transaksi.get('harga_satuan', 0):,}",
                f"Rp {total:,}",
                transaksi.get("status", "-")
            ])
    print(f"{CYAN}{tabel}{RESET}")
    print(f"{CYAN}🧾 Total seluruh pembelian: Rp {total_belanja:,}{RESET}")


def topup():
    bersih()
    print(f"\n{CYAN}{TEBAL}💰 TOP UP SALDO{RESET}")

    if not pengguna_aktif:
        print(f"{KUNING}🔐 Silakan login terlebih dahulu.{RESET}")
        return

    users = load_data1() or []
    akun = next(
        (user for user in users if user.get("user") == pengguna_aktif),
        None
    )

    if akun is None:
        print(f"{MERAH}❌ Data akun tidak ditemukan.{RESET}")
        return

    print(f"Saldo saat ini: Rp {akun.get('saldo', 0):,}".replace(",", "."))

    while True:
        try:
            jumlah = int(input_aman("Masukkan nominal top up (0 untuk batal): "))

            if jumlah == 0:
                print(f"{KUNING}↩️ Top up dibatalkan.{RESET}")
                return

            if jumlah < 0:
                print(f"{KUNING}⚠️ Nominal harus lebih dari 0.{RESET}")
                continue

            break
        except ValueError:
            print(f"{KUNING}⚠️ Nominal harus berupa angka.{RESET}")

    akun["saldo"] = akun.get("saldo", 0) + jumlah
    akun.setdefault("riwayat", []).append({
        "tipe": "topup",
        "jumlah": jumlah,
        "waktu": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

    try:
        save_data(users)
        print(
            f"{HIJAU}✅ Top up berhasil! Saldo sekarang: Rp {akun['saldo']:,}".replace(",", ".") + RESET
        )
    except OSError as error:
        print(f"{MERAH}❌ Gagal menyimpan top up: {error}{RESET}")
#ADMIN PANEL/MENU
def AdminPanel():
    bersih()
    while True:
        print(f"\n{UNGU}{TEBAL}╔══════════════════════════════╗{RESET}")
        print(f"{UNGU}{TEBAL}║          🛠️ MENU ADMIN       ║{RESET}")
        print(f"{UNGU}{TEBAL}╚══════════════════════════════╝{RESET}")
        print("1. ➕ Tambah Barang\n2. 📦 Lihat Barang\n3. ✏️ Ubah Barang\n4. 🗑️ Hapus Barang\n5. 👥 Lihat User\n6. 🚪 Logout\n7. ❌ Exit")
        try:
            p = input_aman("Pilih menu: ")
        except KeyboardInterrupt:
            print(f"{KUNING}Input dibatalkan. Tetap di menu admin.{RESET}")
            continue
        if p == "1":
            jalankan_aman(tambah)
        elif p == "2":
            jalankan_aman(lihat)
        elif p == "3":
            jalankan_aman(ubah)
        elif p == "4":
            jalankan_aman(hapus)
        elif p == "5":
            jalankan_aman(lihat_user)
        elif p == "6":
            break
        elif p == "7":
            exit()
        else:
            print(f"{KUNING}⚠️ Pilihan tidak valid. Coba lagi.{RESET}")

#USER PANEL/MENU
def UserPanel():
    bersih()
    while True:
        print(f"\n{BIRU}{TEBAL}╔══════════════════════════════╗{RESET}")
        print(f"{BIRU}{TEBAL}║           👤 MENU USER       ║{RESET}")
        print(f"{BIRU}{TEBAL}╚══════════════════════════════╝{RESET}")
        print("1. 🛍️ Pesan Barang\n2. 📜 Lihat Riwayat\n3. 📦 Lihat Barang\n4. 💰 Top Up Saldo\n5. 🚪 Logout\n6. ❌ Exit")
        try:
            p = input_aman("Pilih menu: ")
        except KeyboardInterrupt:
            print(f"{KUNING}Input dibatalkan. Tetap di menu user.{RESET}")
            continue
        if p == "1":
            jalankan_aman(pesan)
        elif p == "2":
            jalankan_aman(riwayat)
        elif p == "3":
            jalankan_aman(lihat)
        elif p == "4":
            jalankan_aman(topup)
        elif p == "5":
            break
        elif p == "6":
            exit()
        else:
            print(f"{KUNING}⚠️ Pilihan tidak valid. Coba lagi.{RESET}")

#MENU AWAL
bersih()
while True:
    print(f"\n{CYAN}{TEBAL}╔══════════════════════════════╗{RESET}")
    print(f"{CYAN}{TEBAL}║        🛒 TOKO SKINCARE      ║{RESET}")
    print(f"{CYAN}{TEBAL}╚══════════════════════════════╝{RESET}")
    print("1. 📝 Registrasi\n2. 🔐 Login\n3. ❌ Keluar")
    try:
        p = input_aman("Pilih menu: ")
    except KeyboardInterrupt:
        print(f"{KUNING}Input dibatalkan. Tetap di menu utama.{RESET}")
        continue
    if p == "1":
        jalankan_aman(regis)
    elif p == "2":
        jalankan_aman(login)
    elif p == "3":
        exit()
    else:
        print(f"{KUNING}⚠️ Pilihan tidak valid. Coba lagi.{RESET}")
