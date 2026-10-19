# Pertemuan 07: Fungsi Python

**Nama:** Aditya Setianugroho  
**NIM:** 2225250172
**Kelas:** 3F

## Tujuan

Menggunakan fungsi, parameter, return value, dan scope untuk membuat program modular.

## Cara Menjalankan

```bash
python praktik/utilitas_matematika.py
```

## Struktur Fungsi

- `luas_persegi_panjang(p, l)`: Menggunakan parameter p (panjang) dan l (lebar), berfungsi mengembalikan nilai hasil kali p dan l.

- `luas_segitiga(a, t)`: Menggunakan parameter a (alas) dan t (tinggi), berfungsi mengembalikan nilai hasil rumus 0.5 * a * t.

- `jumlah_n(n)`: Menggunakan parameter n (batas atas), berfungsi mengembalikan total penjumlahan berturut-turut dari angka 1 sampai n menggunakan perulangan.

- `faktorial(n)`: Menggunakan parameter n (bilangan batas), berfungsi mengembalikan hasil kali bilangan dari 2 hingga n.

- `tampilkan_menu()`: Tidak memiliki parameter, fungsinya hanya untuk mencetak daftar pilihan operasi matematika ke layar.

## Hasil Pengujian

### Operasi: Luas persegi panjang

**Input:** p=8, l=5

**Hasil yang diharapkan:** 40

**Hasil aktual:** 40.0

**Status:** Berhasil

### Operasi: Luas segitiga

**Input:** a=10, t=6

**Hasil yang diharapkan:** 30.0

**Hasil aktual:** 30.0

**Status:** Berhasil

### Operasi: Jumlah 1..n

**Input:** n=10

**Hasil yang diharapkan:** 55

**Hasil aktual:** 55

**Status:** Berhasil

### Operasi: Faktorial (Kasus Normal)

**Input:** n=5

**Hasil yang diharapkan:** 120

**Hasil aktual:** 120

**Status:** Berhasil

### Operasi: Faktorial (Kasus Batas)

**Input:** n=0

**Hasil yang diharapkan:** 1

**Hasil aktual:** 1

**Status:** Berhasil

## Refleksi

Pembuatan program utilitas matematika ini menjadi jauh lebih rapi dan terstruktur setelah dipisah ke dalam fungsi-fungsi. Sebagai contoh, bagian program utama tidak perlu lagi menuliskan rumus perhitungan luas atau perulangan faktorial secara berulang. Kita hanya perlu memanggil nama fungsinya saja dan memasukkan argumen yang dibutuhkan. Hal ini juga bikin proses mencari error (debugging) jadi lebih gampang kalau ada perhitungan yang meleset.