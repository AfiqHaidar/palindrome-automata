**👥 Anggota Kelompok**

- Afiq Fawwaz Haidar
- Java Kanaya Prada

---

**💡 Penjelasan Program**

1. Fungsi `is_palindrome(s)` bertugas menyaring karakter dalam string agar hanya menyisakan huruf dan angka menggunakan `isalnum()`, lalu mengubah semua huruf menjadi huruf kecil (`lower()`) agar pengecekan tidak sensitif terhadap kapitalisasi. String kemudian dibandingkan dengan versi terbaliknya (`[::-1]`) untuk menentukan apakah merupakan palindrom.

2. Fungsi `main()` bertanggung jawab untuk:
   - Menampilkan informasi dan petunjuk kepada pengguna.
   - Menerima input berupa beberapa string yang dipisahkan koma.
   - Membersihkan tiap string dari spasi di awal dan akhir.
   - Melakukan iterasi terhadap setiap string dan memanggil fungsi `is_palindrome()` untuk mengecek masing-masing string.

3. Program akan mencetak hasil pengecekan untuk setiap string, menandai apakah string tersebut adalah palindrom (✓) atau bukan palindrom (✗). String kosong akan diabaikan.

