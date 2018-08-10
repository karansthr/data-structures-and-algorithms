def count_ways(number_of_steps, possible_steps=[1, 2], cache={}):
    '''
    Given number of steps of a stair, and possible steps that one can make at a
    time, this function will return the number of possible ways one can reach
    to top of stairs

    for example:
        number_of_steps = 4
        possible_steps = [1, 2] this means one can either climb one step or two steps
        possible ways to reach to top are
            1,1,1,1
            2,1,1
            1,2,1
            1,1,2
            2,2
        so there are five ways to reach to top of stair
        so this function will return 5 for this example

    :param number_of_steps: number of steps in a stair
    :param possible_steps: possible steps one can make to climb stair
    :param cache: a dictionary for caching / memoization
    :type number_of_steps: int
    :type possible_steps: list
    :type cache: dict
    :return: number of possible ways one can climb stairs from botton to top
        with given possible steps
    :rtype: int
    '''
    if number_of_steps in cache.keys():
        return cache[number_of_steps]
    if not cache.keys():
        minimum_step = min(possible_steps)
        second_minimum_step = float('inf')
        for step in possible_steps:
            if step < second_minimum_step and step > minimum_step:
                second_minimum_step = step
        cache[minimum_step] = 1
        cache[second_minimum_step] = 2 if second_minimum_step % minimum_step == 0 else 1
    cache[number_of_steps] = 0
    for step in possible_steps:
        if step <= number_of_steps:
            cache[number_of_steps] += count_ways(number_of_steps-step)
    return cache[number_of_steps]


if __name__ == '__main__':
    for i in range(int(input())):
        print(count_ways(int(input())))
