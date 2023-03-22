# python3


def last_digit_of_fibonacci_number_naive(n):
    assert 0 <= n <= 10 ** 7

    if n <= 1:
        return n

    return (last_digit_of_fibonacci_number_naive(n - 1) + last_digit_of_fibonacci_number_naive(n - 2)) % 10


def last_digit_of_fibonacci_number(n):
    assert 0 <= n <= 10 ** 7

    arr = [*range(0, n)]
    if n < 2:
        return n

    arr[0] = 0
    arr[1] = 1

    for i in range(2, n):
        if i == 2:
            continue
        arr[i] = arr[i-1] + arr[i - 2]

    return arr[-1] % 10




if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_fibonacci_number(input_n))
