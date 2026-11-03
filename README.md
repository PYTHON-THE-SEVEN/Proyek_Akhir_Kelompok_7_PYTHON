# Sistem Pemesanan Produk Kecantikan dan Skin Care :pouch: :shopping: 

## Anggota & Peran
1. Rafi Javier Maulana (2609116050)
   membuat flowchart, kode menu, kode sistem awal, laporan
2. Deka Rizky Fauzan (2609116052)
   Membuat fitur riwayat pemesanan, laporan
3. Dheystrin Gloria Nafisya (2609116063)
   Membuat fitur top up saldo, laporan
4. Pasha Dafa Hibatullah (2609116067)
   perbaikan kode, membuat tampilan kode menjadi lebih menarik, mencari bug/celah, laporan

## Deskripsi & Tujuan
Proyek ini merupakan program yang dikembangkan dengan bahasa pemrograman Python. Program ini merupakan simulasi sistem manajemen toko _e-commerce_ sederhana khusus produk perawatan kulit (_skincare_).
adapun tujuan dari perancangan sistem pemesanan produk kecantikan dan skin care ini adalah sebagai berikut:
1.	Merancang sistem pemesanan produk kecantikan dan skin care yang mudah digunakan oleh pelanggan sehingga dapat mempermudah proses pencarian informasi dan pemesanan produk.
2.	Menyediakan informasi produk, harga, dan ketersediaan stok secara terstruktur agar pelanggan dapat mengetahui detail produk yang tersedia.
3.	Merancang sistem yang dapat membantu pencatatan dan pengelolaan data pemesanan secara lebih terorganisasi guna mengurangi risiko kesalahan dalam pengolahan data.
4.	Memudahkan penjual dalam mengelola data produk, pelanggan, dan transaksi penjualan sehingga kegiatan operasional dapat dilakukan secara lebih efektif dan efisien.

Program ini membagi pengguna menjadi 2 role admin dan user
berikut adalah fitur apa saja yang ada di setiap rolenya:

### Fitur Admin:
1. Tambah Barang: Menambahkan produk skincare baru lengkap dengan nama, kode, harga, dan jumlah stok.
2. Lihat Barang: Menampilkan daftar seluruh produk dalam bentuk tabel.
3. Ubah Barang: Memperbarui informasi detail produk yang sudah ada.
4. Hapus Barang: Menghapus produk dari inventaris toko.
5. Lihat User: Memantau daftar akun pengguna yang terdaftar beserta saldo mereka.

### Fitur User:
1. Pesan Barang: Melakukan transaksi pembelian produk, otomatis memotong saldo akun, mengurangi stok barang, serta mencetak _invoice_ transaksi.
2. Lihat Riwayat: Memeriksa rekam jejak transaksi pembelian dan pengisian saldo sebelumnya.
3. Lihat Barang: Menampilkan daftar seluruh produk dalam bentuk tabel interaktif.
4. Top Up Saldo: Menambahkan saldo digital akun untuk keperluan transaksi.

## Flowchart Serta Penjelsan

<img width="997" height="1177" alt="1menu" src="https://github.com/user-attachments/assets/de0e811b-ca57-4699-8818-1cb91256798f" />

ini merupakan menu awal dimana pengguna dapat melakukan registrasi(membuat akun), login ke akun yang sudah ada, serta keluar dari program. Disini juga menjadi tempat pengcekan role yang akan diarahkan ke menu sesuai rolenya.

<img width="1137" height="1309" alt="1admin" src="https://github.com/user-attachments/assets/23fdaa86-a249-46ca-9c02-42851c881356" />

jika seseorang login menggunakan akun admin, maka akan diarahkan ke menu admin. Admin dapat melakukan penambahan barang/produk, melihat seluruh barang/produk yang ada, mengubah data barang/produk yang ada seperti mengubah nama,stok,kode, ataupun harganya. Selain itu admin juga bisa menghapus data barang yang ada dan juga melihat data user.

<img width="969" height="1311" alt="1users" src="https://github.com/user-attachments/assets/b59c3bb8-f26e-4036-b71e-1da5c5a0dae3" />

jika seseorang login menggunakan akun user, maka akan diarahkan ke menu user. User dapat melakukan pemesanan barang, melihat riwayat pemesanan, melihat seluruh data barang/produk yang ada, dan melakukan top up saldo.

## Penjelasan output

1. Fungsi Tambah Barang `def tambah()`

<img width="332" height="253" alt="image" src="https://github.com/user-attachments/assets/a960f0e0-9d1e-4dbb-9839-179c56273f05" />

Fungsi tambah() digunakan oleh admin untuk menambahkan barang baru ke dalam daftar produk toko skincare. Admin diminta memasukkan nama barang, kode barang, harga, dan stok yang tersedia.

Sebelum menambahkan barang, program membaca data produk yang sudah tersimpan di file `produk (1).json`. Harga dan stok harus berupa angka dan tidak boleh bernilai negatif. Jika input tidak sesuai, program akan menampilkan pesan peringatan dan meminta admin memasukkan data kembali.

Setelah semua data diisi, program menyimpan data barang ke dalam bentuk dictionary. Kemudian, `append()` digunakan untuk menambahkan barang tersebut ke daftar produk. Data yang sudah diperbarui disimpan kembali ke file JSON agar barang baru tetap tersimpan.

Contoh output:

<img width="347" height="155" alt="image" src="https://github.com/user-attachments/assets/4f1913a4-51d3-4b18-be7b-eaf3e7dc3a16" />

2. Fungsi Ubah Barang `def ubah()`

<img width="332" height="253" alt="image" src="https://github.com/user-attachments/assets/b73553c9-ccbb-4bb0-9811-418088502736" />

Fungsi ubah() digunakan oleh admin untuk memperbarui data barang yang sudah ada. Program terlebih dahulu membaca daftar produk dan menampilkannya agar admin bisa memilih barang yang ingin diubah.

Setelah memilih nomor barang, admin memasukkan nama, kode, harga, dan stok yang baru. Program memeriksa input harga dan stok agar berupa angka dan tidak bernilai negatif. Jika nomor barang yang dimasukkan tidak tersedia, program akan menampilkan pesan peringatan.

Data barang diperbarui menggunakan `produk[pili]`, yaitu dengan mengganti data pada posisi barang yang dipilih. Setelah itu, `save_produk()` digunakan untuk menyimpan perubahan ke file `produk (1).json`.

Pada fungsi ini, seluruh data barang diganti berdasarkan input baru, sehingga admin perlu memasukkan kembali nama, kode, harga, dan stok barang.

Contoh output:

<img width="413" height="285" alt="image" src="https://github.com/user-attachments/assets/028fd521-7884-489f-ad99-8f5dcf044ab5" />

3. Fungsi Riwayat Pemesanan `def riwayat()`

<img width="337" height="236" alt="image" src="https://github.com/user-attachments/assets/d9da7d66-1f60-44e2-9902-02745d409f63" />


Fungsi riwayat() digunakan oleh pengguna untuk melihat transaksi yang pernah dilakukan, termasuk top up saldo dan pembelian barang. Program mengambil data akun dari file `users (1).json`, kemudian mencari akun yang sesuai dengan username pengguna yang sedang login.

Jika pengguna belum login, program akan meminta pengguna untuk login terlebih dahulu. Jika akun tidak ditemukan atau belum memiliki riwayat transaksi, program akan menampilkan pesan yang sesuai.

Data transaksi ditampilkan menggunakan `PrettyTable` agar lebih mudah dibaca. Tabel tersebut berisi nomor transaksi, tanggal, nama barang, kode barang, jumlah, harga satuan, total, dan status transaksi.

Program juga membedakan transaksi top up dan pembelian barang. Transaksi top up ditampilkan sebagai penambahan saldo, sedangkan transaksi pembelian digunakan untuk menghitung total seluruh pembelian. Perhitungan tersebut menggunakan variabel `total_belanja`, yang awalnya bernilai nol dan bertambah setiap kali program menemukan transaksi pembelian.

Contoh output:

<img width="930" height="207" alt="image" src="https://github.com/user-attachments/assets/41d367d2-c9c8-44a0-9878-85c19f07dc89" />

4. Fungsi regis `def regis()`

    <img width="300" height="230" alt="Screenshot 2026-11-02 231237" src="https://github.com/user-attachments/assets/68274629-8529-4a75-ba5e-31443411b4e4" />
  <br>Menu 1 adalah registrasi, ketika kita memilih menu 1, kita akan diminta untuk memasukkan username baru dan password baru. Setelahnya data username dan password akan tersimpan di file `users (1).json` lalu program akan kembali menampilkan menu 1-3
<br>
5. Fungsi login `def login()`

   <img width="287" height="138" alt="Screenshot 2026-11-02 231408" src="https://github.com/user-attachments/assets/f9f5ce07-7aa4-4322-b27a-df857ec7edd0" />
   <br><img width="281" height="146" alt="Screenshot 2026-11-02 231423" src="https://github.com/user-attachments/assets/564ca457-b5c8-4849-b487-00adadf2a3bd" />
<br>
   menu 2 adalah login, ketika kita memilih menu 2, kita akan diminta untuk memasukkan nama dan password yang telah diregistrasi atau telah tersimpan pada file `users (1).json` lalu saat menekan enter program akan membersihkan terminal lalu menampilkan menu 1-3<br>

6. Fungsi top up `def topup()`

  <img width="344" height="230" alt="Screenshot 2026-11-02 230909" src="https://github.com/user-attachments/assets/3a36d07c-0410-46d8-af23-73458c43f82e" />
   <br><img width="290" height="194" alt="Screenshot 2026-11-02 231013" src="https://github.com/user-attachments/assets/824d01b3-2311-4287-8b22-cc4914df221f" />
  <br>
  setelah login program akan menampilkan menu user karena pengguna login dengan role user, lalu pilihan menu 4 untuk top up saldo. Menu top up saldo menampilkan total saldo saat ini, user diminta memasukkan nominal top up (0 untuk batal), ketika top up berhasil program menampilkan "top up berhasil saldo anda sekarang.." lalu program menampilkan kembali menu user.

7. Fungsi pesan `def pesan()`

   <img width="380" height="371" alt="Screenshot 2026-11-03 200552" src="https://github.com/user-attachments/assets/9e7c3618-7c40-4e0c-9ab9-c25ed093ccb1" />

   Pada menu pemesanan, pengguna dapat memilih lebih dari satu produk dan memasukkan jumlah setiap produk. Program menampilkan jumlah barang serta total harga sementara setelah produk ditambahkan ke keranjang. Setelah pengguna selesai memilih, program menampilkan ringkasan pesanan dan meminta konfirmasi. Jika pesanan berhasil, saldo pengguna dan stok produk akan diperbarui, lalu program menampilkan invoice.

8. Fungsi lihat  `def lihat()`
   
   <img width="194" height="76" alt="Screenshot 2026-11-03 201216" src="https://github.com/user-attachments/assets/575fc729-cc96-4f80-af86-afc43048d21d" />

   Menu lihat barang digunakan untuk menampilkan daftar produk yang tersimpan di file JSON. Informasi yang ditampilkan meliputi nomor barang, nama barang, kode, harga, dan jumlah stok. Jika belum ada produk yang tersimpan, program akan menampilkan pesan bahwa barang belum tersedia.

9. Fungsi hapus  `def hapus()`

<img width="251" height="97" alt="Screenshot 2026-11-03 201559" src="https://github.com/user-attachments/assets/194287cf-edeb-41e3-bfd3-da92634dc27c" />
<img width="241" height="65" alt="Screenshot 2026-11-03 201612" src="https://github.com/user-attachments/assets/4048ba4a-9f0d-4bbd-a5dd-305ebe8320a5" />

   Menu hapus barang digunakan untuk menghapus produk dari daftar. Program menampilkan daftar barang terlebih dahulu, lalu admin memilih nomor produk yang ingin dihapus. Jika nomor yang dimasukkan tersedia, produk akan dihapus dari file JSON. Jika nomor tidak ditemukan atau input bukan angka, program akan menampilkan pesan kesalahan.

10. Fungsi lihat_user `def lihat_user()`

    <img width="168" height="97" alt="Screenshot 2026-11-03 201819" src="https://github.com/user-attachments/assets/3911fe74-4008-4a26-878b-9a3617913205" />

   Menu lihat pengguna digunakan admin untuk melihat daftar akun yang terdaftar. Informasi yang ditampilkan meliputi nomor, username, role, dan saldo pengguna. Jika belum ada data pengguna, program akan menampilkan pesan bahwa data pengguna belum tersedia.
