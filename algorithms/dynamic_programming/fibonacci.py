def fibonacci(number, cache={1: 0, 2: 1}):
    if number in cache.keys():
        return cache[number]
    cache[number] = fibonacci(number-1) + fibonacci(number-2)
    return cache[number]


if __name__ == '__main__':
    print(fibonacci(int(input())))
