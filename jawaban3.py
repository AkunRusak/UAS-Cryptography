def cekDigitISBN(isbn):
    # hapus tanda hubung dari ISBN
    isbn = isbn.replace("-", "")
    
    # memastikan ISBN memiliki 9 digit
    if len(isbn) != 9:
        raise ValueError("ISBN must be 9 digits long")

    # mengonversikan ke daftar bilangan bulat
    digits = [int(char) for char in isbn]

    # hitung jumlahnya
    total_sum = sum((10 - i) * digits[i] for i in range(9))

    # hitung sisanya jika dibagi 11
    remainder = total_sum % 11

    # hitung digit ceknya
    check_digit = 11 - remainder

    # jika digit pemeriksa adalah 10, seharusnya 'X'
    return 'X' if check_digit == 10 else str(check_digit)

# uji fungsinya dengan ISBN yang dibuat
isbn_code = "602-291-055"
check_digit = cekDigitISBN(isbn_code)

# cek digit terakhir
print(f"Digit terakhir ISBN {isbn_code} adalah: {check_digit}")