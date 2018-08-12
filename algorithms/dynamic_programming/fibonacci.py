def fibonacci(n, cache={1: 0, 2: 1}):
    '''
    return nth number of fibonacci series

    :param n: nth term of fibonacci series
    :param cache: dictionary for caching / memoization
    :type n: int
    :type cache: dict
    '''
    if n < 1:
        raise Exception('It should be greater than 0')
    if n in cache.keys():
        return cache[n]
    cache[n] = fibonacci(n-1) + fibonacci(n-2)
    return cache[n]


if __name__ == '__main__':
    print(fibonacci(int(input())))
