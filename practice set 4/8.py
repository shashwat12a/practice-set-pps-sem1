num = int(input("Enter num: "))

initial = num
rev = 0

while num > 0:
    rem = num % 10
    rev = rev * 10 + int(rem)
    num = int(num / 10)

if initial == rev:
    print("num is palindrome")
else:
    print("num is not palindrome")