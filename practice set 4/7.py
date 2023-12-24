num = int(input("Enter num: "))

rev = 0
while num > 0:
    rem = num % 10
    rev = rev * 10 + int(rem)
    num = int(num / 10)

print("num reversed is:", rev)