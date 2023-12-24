# using recursion
def factorial(num):
    if num <= 1:
        return 1
    fac = num*factorial(num-1)
    return fac

num = int(input("Enter num: "))
print(factorial(num))