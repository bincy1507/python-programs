# python program to print nth prime number

def nth_prime(n):
    primes = [2]
    num = 3
    while len(primes) < n:
        if all(num % i != 0 for i in primes):
            primes.append(num)
        num += 2
    return primes[-1]


print(nth_prime(6))
