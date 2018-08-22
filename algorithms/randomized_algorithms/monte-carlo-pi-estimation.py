import random


def estimate_pi(n):
    data = {
            'inside_circle': 0,
            'outside_circle': 0
    }
    for i in range(n):
        x, y = random.random(), random.random()
        if x**2 + y**2 <= 1:
            data['inside_circle'] += 1
        else:
            data['outside_circle'] += 1

    return 4*(data['inside_circle']/(data['inside_circle'] + data['outside_circle']))


if __name__ == "__main__":
    print(estimate_pi(int(input())))
