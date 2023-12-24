def sum(num):
    sum = 0
    while num > 0:
        rem = num % 10
        sum = sum + int(rem)
        num = int(num / 10)
    return sum

inp = int(input())
sum = sum(inp)
print(sum)