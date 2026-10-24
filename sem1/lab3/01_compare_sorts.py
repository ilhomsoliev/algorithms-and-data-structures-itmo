import random
import time


def quick_sort(a, three_parts, randomized=True):
    parts = [(0, len(a) - 1)]

    while parts:
        left, right = parts.pop()
        if left >= right:
            continue

        pivot_index = random.randint(left, right) if randomized else right

        if three_parts:
            pivot = a[pivot_index]
            smaller = left
            current = left
            greater = right

            while current <= greater:
                if a[current] < pivot:
                    a[smaller], a[current] = a[current], a[smaller]
                    smaller += 1
                    current += 1
                elif a[current] > pivot:
                    a[current], a[greater] = a[greater], a[current]
                    greater -= 1
                else:
                    current += 1

            parts.append((left, smaller - 1))
            parts.append((greater + 1, right))
        else:
            a[pivot_index], a[right] = a[right], a[pivot_index]
            pivot = a[right]
            border = left

            for i in range(left, right):
                if a[i] <= pivot:
                    a[border], a[i] = a[i], a[border]
                    border += 1

            a[border], a[right] = a[right], a[border]
            parts.append((left, border - 1))
            parts.append((border + 1, right))

    return a


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


def check(name, a):
    expected = sorted(a)
    print(name)

    for title, method in (
        ('обычный QuickSort', lambda b: quick_sort(b, False, False)),
        ('случайный QuickSort', lambda b: quick_sort(b, False)),
        ('QuickSort с тремя частями', lambda b: quick_sort(b, True)),
        ('MergeSort', merge_sort)
    ):
        copy = a.copy()
        start = time.perf_counter()
        result = method(copy)
        elapsed = time.perf_counter() - start
        assert result == expected
        print(f'  {title}: {elapsed:.6f} с')


random.seed(42)

for n in (1000, 3000):
    numbers = random.sample(range(-10**9, 10**9), n)
    check(f'n={n}, отсортированный массив', sorted(numbers))
    check(f'n={n}, обратный порядок', sorted(numbers, reverse=True))
    check(f'n={n}, случайный массив', numbers)
    check(f'n={n}, много одинаковых чисел', [random.randint(0, 4) for _ in range(n)])
