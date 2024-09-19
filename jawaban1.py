def cekDigitISSN(issn):
    # hapus tanda hubung dari ISSN
    issn = issn.replace("-", "")
    
    # memastikan panjang ISSN 8 digit
    if len(issn) != 8:
        return "Panjang ISSN tidak valid"
    
    # ekstrak 7 digit pertama dan ubah menjadi bilangan bulat
    digits = [int(digit) for digit in issn[:7]]
    
    # bobot untuk 7 digit pertama
    weights = [8, 7, 6, 5, 4, 3, 2]
    
    # hitung jumlah tertimbangnya
    weighted_sum = sum(d * w for d, w in zip(digits, weights))
    
    # hitung digit ceknya
    remainder = weighted_sum % 11
    check_digit = 11 - remainder
    
    # jika digit pengecekannya 10 gunakan 'X', jika 11 gunakan '0'
    if check_digit == 10:
        return 'X'
    elif check_digit == 11:
        return '0'
    else:
        return str(check_digit)

# uji fungsinya dengan ISSN 2338-3585
issn = "2338-3585"
hasilCekDigit = cekDigitISSN(issn)
print(f"Hasil digit dari ISSN {issn} adalah: {hasilCekDigit}")