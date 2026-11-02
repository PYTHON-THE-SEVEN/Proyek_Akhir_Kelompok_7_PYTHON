# Sistem Pemesanan Produk Kecantikan dan Skin Care

3. Fungsi Tambah Barang (def tambah())

<img width="896" height="675" alt="image" src="https://github.com/user-attachments/assets/cdb4819d-d75c-408d-a8db-f2994ce7f412" />


Fungsi tambah() digunakan oleh admin untuk menambahkan barang baru ke dalam daftar produk toko skincare. Admin diminta memasukkan nama barang, kode barang, harga, dan stok yang tersedia.

Sebelum menambahkan barang, program membaca data produk yang sudah tersimpan di file produk (1).json. Harga dan stok harus berupa angka dan tidak boleh bernilai negatif. Jika input tidak sesuai, program akan menampilkan pesan peringatan dan meminta admin memasukkan data kembali.

Setelah semua data diisi, program menyimpan data barang ke dalam bentuk dictionary. Kemudian, append() digunakan untuk menambahkan barang tersebut ke daftar produk. Data yang sudah diperbarui disimpan kembali ke file JSON agar barang baru tetap tersimpan.

Contoh output:

📦 TAMBAH DATA BARANG
Masukkan Nama Barang : moisturizer
Masukkan Kode Barang : ms001
Masukkan Harga Barang: 85000
Stok Barang : 20

✅ Barang berhasil ditambahkan!

4. Fungsi Ubah Barang (def ubah())

<img width="972" height="798" alt="image" src="https://github.com/user-attachments/assets/482dbd79-f2a3-4536-a0be-dcc4c32e871f" />


Fungsi ubah() digunakan oleh admin untuk memperbarui data barang yang sudah ada. Program terlebih dahulu membaca daftar produk dan menampilkannya agar admin bisa memilih barang yang ingin diubah.

Setelah memilih nomor barang, admin memasukkan nama, kode, harga, dan stok yang baru. Program memeriksa input harga dan stok agar berupa angka dan tidak bernilai negatif. Jika nomor barang yang dimasukkan tidak tersedia, program akan menampilkan pesan peringatan.

Data barang diperbarui menggunakan produk[pili], yaitu dengan mengganti data pada posisi barang yang dipilih. Setelah itu, save_produk() digunakan untuk menyimpan perubahan ke file produk (1).json.

Pada fungsi ini, seluruh data barang diganti berdasarkan input baru, sehingga admin perlu memasukkan kembali nama, kode, harga, dan stok barang.

Contoh output:

Pilih data yang mau di ubah: 2
Masukkan Nama Barang baru : sunscreen
Masukkan Kode baru : ss001
Masukkan Harga Baru : 70000
Masukkan Stok Baru : 40

✅ Data berhasil diperbarui.

5. Fungsi Riwayat Pemesanan (def riwayat())

<img width="743" height="802" alt="image" src="https://github.com/user-attachments/assets/80896cbb-a308-4380-87cc-8d529250bad9" />


Fungsi riwayat() digunakan oleh pengguna untuk melihat transaksi yang pernah dilakukan, termasuk top up saldo dan pembelian barang. Program mengambil data akun dari file users (1).json, kemudian mencari akun yang sesuai dengan username pengguna yang sedang login.

Jika pengguna belum login, program akan meminta pengguna untuk login terlebih dahulu. Jika akun tidak ditemukan atau belum memiliki riwayat transaksi, program akan menampilkan pesan yang sesuai.

Data transaksi ditampilkan menggunakan PrettyTable agar lebih mudah dibaca. Tabel tersebut berisi nomor transaksi, tanggal, nama barang, kode barang, jumlah, harga satuan, total, dan status transaksi.

Program juga membedakan transaksi top up dan pembelian barang. Transaksi top up ditampilkan sebagai penambahan saldo, sedangkan transaksi pembelian digunakan untuk menghitung total seluruh pembelian. Perhitungan tersebut menggunakan variabel total_belanja, yang awalnya bernilai nol dan bertambah setiap kali program menemukan transaksi pembelian.

Contoh output:

=== RIWAYAT PEMESANAN ===



Output tersebut merupakan contoh berdasarkan data top up akun Asep yang tersimpan di file JSON. Total pembelian masih nol karena belum ada transaksi pembelian barang yang tercatat.

6. Fungsi regis (def regis())

    <img width="300" height="230" alt="Screenshot 2026-11-02 231237" src="https://github.com/user-attachments/assets/68274629-8529-4a75-ba5e-31443411b4e4" />
  <br>pada menu 1 yaitu registrasi saat kita memilih menu 1 kita diminta untuk memasukkan username baru dan password baru. Setelahnya program akan kembali menampilkan menu 1-3
<br>
7. Fungsi login (def login())

   <img width="287" height="138" alt="Screenshot 2026-11-02 231408" src="https://github.com/user-attachments/assets/f9f5ce07-7aa4-4322-b27a-df857ec7edd0" />
   <br><img width="281" height="146" alt="Screenshot 2026-11-02 231423" src="https://github.com/user-attachments/assets/564ca457-b5c8-4849-b487-00adadf2a3bd" />
<br>
   menu 2 yaitu login saat kita memilih menu 2, kita diminta untuk memasukkan nama dan password yang telah diregistrasi lalu saat menekan enter program akan membersihkan terminal lalu menampilkan menu 1-3<br>

8. Fungsi top up

  <img width="344" height="230" alt="Screenshot 2026-11-02 230909" src="https://github.com/user-attachments/assets/3a36d07c-0410-46d8-af23-73458c43f82e" />
   <br><img width="290" height="194" alt="Screenshot 2026-11-02 231013" src="https://github.com/user-attachments/assets/824d01b3-2311-4287-8b22-cc4914df221f" />
  <br>
  setelah login program akan menampilkan menu user karena login dengan role user, lalu pilihan menu 4 untuk top up saldo. Menu top up saldo menampilkan total saldo saat ini, user diminta memasukkan nominal top up (0 untuk batal), ketika top up berhasil program menampilkan "top up berhasil saldo anda sekarang.." lalu program menampilkan kembali menu user


