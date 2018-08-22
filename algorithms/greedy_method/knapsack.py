def knapsack(capacity, items):
    '''
    :param capacity: capacity of sack
    :param items: list of tuples containing weight and value of item
    :type capacity: int
    :type items: list
    :return: maximum profit that one can gain with sack of given capacity
    :rtype: float
    '''
    arr = sorted(items, key=lambda x: x[1]/x[0])
    profit = 0
    for value, weight in arr:
        if capacity > weight:
            profit += value
            capacity -= weight
        else:
            profit += value*capacity/weight
            break
    return profit


if __name__ == "__main__":
    CAPACITY = int(input("Enter total capacity of sack : "))
    N = int(input("Enter number of items : "))
    arr = []
    for i in range(N):
        print("Enter weight and values of item #", i + 1, ' : ', end="")
        arr.append(tuple(map(int, input().split())))
    profit = knapsack(CAPACITY, arr)
    print(profit)
