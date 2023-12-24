non_primes = []
for i in range(2,10):
    for j in range(2,i):
        if i % j == 0:
            non_primes.append(i)

for i in range(2, 10):
    if i not in non_primes:
        print(i)