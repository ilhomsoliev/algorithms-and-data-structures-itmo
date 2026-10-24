import random
import time


def merge_sort(a):
    if len(a) <= 1:
        return a

    middle = len(a) // 2
    left = merge_sort(a[:middle])
    right = merge_sort(a[middle:])
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def insertion_sort(a):
    for i in range(1, len(a)):
        value = a[i]
        j = i - 1
        while j >= 0 and a[j] > value:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = value
    return a


random.seed(42)

for n in (100, 1000, 3000):
    numbers = random.sample(range(-10**9, 10**9), n)
    for name, a in (
        ('отсортированный', sorted(numbers)),
        ('случайный', numbers),
        ('обратный', sorted(numbers, reverse=True))
    ):
        start = time.perf_counter()
        merged = merge_sort(a)
        merge_time = time.perf_counter() - start

        start = time.perf_counter()
        inserted = insertion_sort(a.copy())
        insertion_time = time.perf_counter() - start

        assert merged == inserted
        print(f'n={n}, {name}: слияние {merge_time:.6f} с, вставки {insertion_time:.6f} с')
