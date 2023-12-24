num = int(input("Enter num: "))

if num < 151:
    print("num too low")

for i in range(1, num, int(num/150)):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)