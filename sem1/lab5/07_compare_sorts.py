import random
import time


def heap_sort(a):
    def max_heapify(index, size):
        while True:
            largest = index
            left = 2 * index + 1
            right = left + 1

            if left < size and a[left] > a[largest]:
                largest = left
            if right < size and a[right] > a[largest]:
                largest = right

            if largest == index:
                break

            a[index], a[largest] = a[largest], a[index]
            index = largest

    n = len(a)
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(i, n)

    answer = []
    for end in range(n - 1, 0, -1):
        a[0], a[end] = a[end], a[0]
        answer.append(a[end])
        max_heapify(0, end)

    answer.append(a[0])
    return answer


def quick_sort(a):
    parts = [(0, len(a) - 1)]

    while parts:
        left, right = parts.pop()
        while left < right:
            pivot = a[random.randint(left, right)]
            smaller = left
            current = left
            greater = right

            while current <= greater:
                if a[current] > pivot:
                    a[smaller], a[current] = a[current], a[smaller]
                    smaller += 1
                    current += 1
                elif a[current] < pivot:
                    a[current], a[greater] = a[greater], a[current]
                    greater -= 1
                else:
                    current += 1

            if smaller - left < right - greater:
                if greater + 1 < right:
                    parts.append((greater + 1, right))
                right = smaller - 1
            else:
                if left < smaller - 1:
                    parts.append((left, smaller - 1))
                left = greater + 1

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
        if left[i] >= right[j]:
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
        while j >= 0 and a[j] < value:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = value
    return a


random.seed(42)

for n in (100, 1000, 3000):
    numbers = random.sample(range(-10**9, 10**9), n)
    for name, a in (
        ('по убыванию', sorted(numbers, reverse=True)),
        ('по возрастанию', sorted(numbers)),
        ('несколько уникальных чисел', [random.randint(0, 4) for _ in range(n)]),
        ('случайный массив', numbers)
    ):
        print(f'n={n}, {name}')
        expected = sorted(a, reverse=True)

        for title, sort in (
            ('HeapSort', heap_sort),
            ('QuickSort', quick_sort),
            ('MergeSort', merge_sort),
            ('InsertionSort', insertion_sort)
        ):
            start = time.perf_counter()
            result = sort(a.copy())
            elapsed = time.perf_counter() - start
            assert result == expected
            print(f'  {title}: {elapsed:.6f} с')
