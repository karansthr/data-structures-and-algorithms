def prime_sieve(limit):
    arr = [True] * (limit+1)
    arr[0] = arr[1] = False
    for (number, is_prime) in enumerate(arr):
        if is_prime:
            yield number
            for i in range(number, limit + 1, number):
                arr[i] = False


if __name__ == '__main__':
    primes = prime_sieve(int(input('Enter a limit upto which you find prime numbers : ')))
    print(*primes)
