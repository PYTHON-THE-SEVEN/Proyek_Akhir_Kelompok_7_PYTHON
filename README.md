# Sistem Pemesanan Produk Kecantikan dan Skin Care

Anggota & Peran
1. Rafi Javier Maulana (2609116050)
   membuat flowchart, kode menu, kode sistem awal, laporan
2. Deka Rizky Fauzan (2609116052)
   
3. Dheystrin Gloria Nafisya (2609116063)
   
4. Pasha Dafa Hibatullah (2609116067)


Deskripsi Program
Proyek ini merupakan program yang dikembangkan dengan bahasa pemrograman Python. Program ini merupakan simulasi sistem manajemen toko e-commerce sederhana khusus produk perawatan kulit (skincare).
adapun tujuan dari perancangan sistem pemesanan produk kecantikan dan skin care ini adalah sebagai berikut:
1.	Merancang sistem pemesanan produk kecantikan dan skin care yang mudah digunakan oleh pelanggan sehingga dapat mempermudah proses pencarian informasi dan pemesanan produk.
2.	Menyediakan informasi produk, harga, dan ketersediaan stok secara terstruktur agar pelanggan dapat mengetahui detail produk yang tersedia.
3.	Merancang sistem yang dapat membantu pencatatan dan pengelolaan data pemesanan secara lebih terorganisasi guna mengurangi risiko kesalahan dalam pengolahan data.
4.	Memudahkan penjual dalam mengelola data produk, pelanggan, dan transaksi penjualan sehingga kegiatan operasional dapat dilakukan secara lebih efektif dan efisien.

Program ini membagi pengguna menjadi 2 role admin dan user
berikut adalah fitur apa saja yang ada di setiap rolenya:

Fitur Admin:
1. Tambah Barang: Menambahkan produk skincare baru lengkap dengan nama, kode, harga, dan jumlah stok.
2. Lihat Barang: Menampilkan daftar seluruh produk dalam bentuk tabel.
3. Ubah Barang: Memperbarui informasi detail produk yang sudah ada.
4. Hapus Barang: Menghapus produk dari inventaris toko.
5. Lihat User: Memantau daftar akun pengguna yang terdaftar beserta saldo mereka.

Fitur User:
1. Pesan Barang: Melakukan transaksi pembelian produk, otomatis memotong saldo akun, mengurangi stok barang, serta mencetak invoice transaksi.
2. Lihat Riwayat: Memeriksa rekam jejak transaksi pembelian dan pengisian saldo sebelumnya.
3. Lihat Barang: Menampilkan daftar seluruh produk dalam bentuk tabel interaktif.
4. Top Up Saldo: Menambahkan saldo digital akun untuk keperluan transaksi.

Flowchart Serta Penjelsan

<img width="997" height="1177" alt="1menu" src="https://github.com/user-attachments/assets/de0e811b-ca57-4699-8818-1cb91256798f" />

ini merupakan menu awal dimana pengguna dapat melakukan registrasi(membuat akun), login ke akun yang sudah ada, serta keluar dari program. Disini juga menjadi tempat pengcekan role yang akan diarahkan ke menu sesuai rolenya.

<img width="1137" height="1309" alt="1admin" src="https://github.com/user-attachments/assets/23fdaa86-a249-46ca-9c02-42851c881356" />

jika seseorang login menggunakan akun admin, maka akan diarahkan ke menu admin. Admin dapat melakukan penambahan barang/produk, melihat seluruh barang/produk yang ada, mengubah data barang/produk yang ada seperti mengubah nama,stok,kode, ataupun harganya. Selain itu admin juga bisa menghapus data barang yang ada dan juga melihat data user.

<img width="969" height="1311" alt="1users" src="https://github.com/user-attachments/assets/b59c3bb8-f26e-4036-b71e-1da5c5a0dae3" />

jika seseorang login menggunakan akun user, maka akan diarahkan ke menu user. User dapat melakukan pemesanan barang, melihat riwayat pemesanan, melihat seluruh data barang/produk yang ada, dan melakukan top up saldo.


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


