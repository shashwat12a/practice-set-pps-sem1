n = int(input("Enter num: "))
sum = 0
for i in range(1, n):
    if n % i == 0:
        sum = sum + i
if sum == n:
    print("num is perfect")
else:
    print("num is not perfect")