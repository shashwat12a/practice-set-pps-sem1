str_digits = ""
for digit in "0165031806510":
    if digit == "0":
        str_digits = str_digits + "x"
    else:
        str_digits = str_digits + digit

print(str_digits)
