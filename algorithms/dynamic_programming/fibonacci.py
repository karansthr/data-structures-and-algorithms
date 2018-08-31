class Memoize:
    def __init__(self, function):
        self.cache = {}
        self.function = function

    def __call__(self, number):
        if number in self.cache:
            return self.cache[number]
        self.cache[number] = self.function(number)
        return self.cache[number]


@Memoize
def fibonacci(number):
    if number < 0:
        raise Exception('Number should be greater that 0.')
    if number in (1, 2):
        return 1
    return fibonacci(number - 1) + fibonacci(number - 2)


if __name__ == '__main__':
    print(fibonacci(int(input())))
