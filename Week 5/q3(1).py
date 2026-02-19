import numpy as np
numbers = np.arange(1, 101)
primes = []

for num in numbers:
    num = int(num) 
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            primes.append(num)

print("Prime Numbers from 1 to 100:")
print(primes)
