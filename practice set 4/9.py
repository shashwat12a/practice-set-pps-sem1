num = int(input("Enter num: "))

order = len(str(num))
num1 = num
num2 = 0

while num > 0:
    rem = num % 10
    num2 = num2 + (rem**order)
    num = int(num / 10)

if num2 == num1:
    print("it is a armstrong number")
else:
    print("not an armstrong number")