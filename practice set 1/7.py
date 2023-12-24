def swap(a, b):
    tmp = a
    a = b
    b = tmp
    return a, b

num1 = int(input("Enter num 1:"))
num2 = int(input("Enter num 2:"))

print("swapped values are: num1, num2: ", swap(num1, num2))