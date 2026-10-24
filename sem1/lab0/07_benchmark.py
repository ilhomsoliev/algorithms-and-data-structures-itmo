import time


def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


def last_digit(n):
    a, b = 0, 1
    for i in range(n % 60):
        a, b = b, (a + b) % 10
    return a


for name, func, values in (
    ('Число Фибоначчи', fibonacci, (1, 20, 45)),
    ('Последняя цифра', last_digit, (1, 100_000, 10_000_000))
):
    print(name)
    for n in values:
        start = time.perf_counter()
        for i in range(10000):
            func(n)
        seconds = (time.perf_counter() - start) / 10000
        print(f'n = {n}: {seconds:.9f} с')
