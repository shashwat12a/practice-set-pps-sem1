num = int(input("Enter num: "))

i = 0
while num >= 10:
    num = num/3
    i=i+1

print("num can be divided by three:", i, "times")