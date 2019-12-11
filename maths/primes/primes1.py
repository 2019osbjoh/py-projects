# Sieve of Eratosthenes
# Calculates primes by removing multiples from a list

primes = []

for i in range(2, 100):
    for j in range(2, 100):
        if i % j != 0:
            primes.append(j)

print(primes)
