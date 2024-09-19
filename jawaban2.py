def digitUPC(upc):
    # hapus tanda hubung dari UPC
    upc = upc.replace("-", "")
    
    # memastikan panjangnya 12 digit
    if len(upc) != 12:
        raise ValueError("UPC harus terdiri dari 12 digit")
    
    # mengonversikan ke daftar bilangan bulat
    digits = [int(char) for char in upc[:-1]]  # mengecualikan digit terakhir (cek digit)

    # memisahkan menjadi angka ganjil dan genap
    odd_digits = digits[0::2]  # posisi ganjil: 0, 2, 4, ...
    even_digits = digits[1::2]  # posisi genap: 1, 3, 5, ...

    # Langkah 1: Kalikan angka-angka yang ganjil dengan 3 dan jumlahkan
    odd_sum = sum(odd_digit * 3 for odd_digit in odd_digits)
    
    # Langkah 2: Kalikan angka genap dengan 1 dan jumlahkan
    even_sum = sum(even_digits)

    # Langkah 3: Jumlahkan jumlahnya
    total_sum = odd_sum + even_sum

    # Langkah 4: Menemukan kelipatan 10 berikutnya yang lebih besar dari atau sama dengan jumlah tersebut
    next_multiple_of_10 = (total_sum + 9) // 10 * 10

    # Langkah 5: Kurangi jumlah total dari kelipatan 10 berikutnya untuk mendapatkan digit pemeriksa
    check_digit = next_multiple_of_10 - total_sum

    # mengembalikan digit cek yang dihitung
    return check_digit


# uji fungsi dengan UPC yang disediakan
upc_code = "725272730706"  # kode UPC lengkap termasuk digit pengecekan
hasilCekDigit = digitUPC(upc_code)

# mencetak hasilnya
print(f"Digit Cek Terhitung: {hasilCekDigit}") # menghitung digit cek
print(f"Hasil cek Digit: {upc_code[-1]}")  # hasil cel digit

# verifikasi digit cek
if hasilCekDigit == int(upc_code[-1]):
    print("Digit cek benar!")
else:
    print("Digit cek salah!")
