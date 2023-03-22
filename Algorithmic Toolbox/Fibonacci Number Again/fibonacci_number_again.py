# python3


def fibonacci_number_again_naive(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current



def pisano(m):
    p, c = 0, 1

    for i in range(0, m*m):
        p, c = c, (p + c) % m
        if p == 0 and c == 1:
            return i + 1


def fibonacci_number_again(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3
    n = n % pisano(m)

    p, c = 0, 1
    if n == 0:
        return 0
    elif n == 1:
        return 1

    for i in range(n - 1):
        p, c = c, p + c

    return c % m


if __name__ == '__main__':
    input_n, input_m = map(int, input().split())
    print(fibonacci_number_again(input_n, input_m))
