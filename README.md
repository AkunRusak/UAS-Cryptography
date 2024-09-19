# Jawaban 3

### Langkah-langkah perhitungan:
1. Pisahkan angka-angka dari ISBN: `6, 0, 2, 2, 9, 1, 0, 5, 5`.
2. Kalikan masing-masing angka dengan urutan penurunan dari 10 hingga 2.

### Perhitungan:
`checksum=(6×10)+(0×9)+(2×8)+(2×7)+(9×6)+(1×5)+(0×4)+(5×3)+(5×2)`

`checksum=60+0+16+14+54+5+0+15+10=174`

3. Jumlah totalnya adalah 174. Sekarang kita cari modulus 174 terhadap 11:
`174 mod 11 = 9`

4. Kurangkan hasil modulus dari 11 untuk mendapatkan check digit:
`11 − 9 = 2`

Jadi, **angka terakhir dari ISBN-10** untuk **602-291-055** adalah **2**.

### Output:
```
cek digit untuk ISBN 602-291-055 adalah: 2
```
# Jawaban 4

### Langkah-langkah perhitungan:

#### 1. Hitung Frekuensi Karakter
Teks yang akan dikompresi adalah: **"INSAN UNGGUL JAYA"**.

Kita menghitung frekuensi kemunculan setiap karakter:

| Karakter | Frekuensi |
|----------|-----------|
| I        | 1         |
| N        | 2         |
| S        | 1         |
| A        | 3         |
| U        | 2         |
| G        | 2         |
| L        | 1         |
| J        | 1         |
| Y        | 1         |
| (spasi)  | 2         |

#### 2. Buat Pohon Huffman
Berdasarkan frekuensi, kita buat pohon Huffman. Urutan prosesnya:
- Mulai dengan karakter yang paling jarang muncul.
- Gabungkan karakter dengan frekuensi terendah menjadi satu node sampai semua karakter tergabung.

Pohon Huffman ini akan terlihat seperti berikut:
- Gabungkan 'I' (1) dan 'S' (1) menjadi node dengan frekuensi 2.
- Gabungkan 'L' (1) dan 'J' (1) menjadi node dengan frekuensi 2.
- Gabungkan 'Y' (1) dan node ('I', 'S') (2) menjadi node dengan frekuensi 3.
- Gabungkan 'L', 'J' (2) dan (spasi) (2).
- Lanjutkan sampai semua node tergabung menjadi satu pohon.

Setelah membangun pohon Huffman, kita tetapkan kode biner untuk setiap karakter.

#### 3. Tetapkan Kode Huffman
Misalkan kode Huffman untuk setiap karakter dihasilkan seperti ini (kode aktual dapat bervariasi tergantung pada proses penggabungan pohon):

| Karakter | Kode Huffman |
|----------|--------------|
| I        | 1100         |
| N        | 10           |
| S        | 1101         |
| A        | 00           |
| U        | 111          |
| G        | 101          |
| L        | 0110         |
| J        | 0111         |
| Y        | 1110         |
| (spasi)  | 010          |

#### 4. Kompres Teks
Sekarang kita kompres teks menggunakan kode Huffman yang telah dihasilkan:

- **INSAN UNGGUL JAYA** akan dikompres menjadi:
  ```
  I = 1100
  N = 10
  S = 1101
  A = 00
  N = 10
  (spasi) = 010
  U = 111
  N = 10
  G = 101
  G = 101
  U = 111
  L = 0110
  (spasi) = 010
  J = 0111
  A = 00
  Y = 1110
  A = 00
  ```

Sehingga teks terkompresi adalah:  
```
1100 10 1101 00 10 010 111 10 101 101 111 0110 010 0111 00 1110 00
```

#### 5. Hitung Rasio Kompresi
- **Teks asli**: Ada 18 karakter dalam teks asli. Jika menggunakan 8-bit untuk setiap karakter (ASCII), maka ukuran asli = 18 × 8 = **144 bit**.
- **Teks terkompresi**: Jumlahkan panjang bit dari kode Huffman:
  ```
  4 + 2 + 4 + 2 + 2 + 3 + 3 + 3 + 3 + 3 + 3 + 4 + 3 + 4 + 2 + 4 + 2 = 49 bit
  ```

- **Rasio kompresi** = (Ukuran asli - Ukuran terkompresi) / Ukuran asli:
  ```
  Rasio kompresi = (144 - 49) / 144 = 95 / 144 ≈ 0.66 atau 66%
  ```

Jadi, kompresi menggunakan metode Huffman untuk teks **"INSAN UNGGUL JAYA"** menghasilkan ukuran teks yang berkurang sebesar **66%**.
