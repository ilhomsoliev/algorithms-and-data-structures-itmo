import random

with open('input.txt') as file:
    data = list(map(int, file.read().split()))

n = data[0]
a = data[1:n + 1]
parts = [(0, n - 1)]

while parts:
    left, right = parts.pop()

    while left < right:
        pivot = a[random.randint(left, right)]
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

        if smaller - left < right - greater:
            if greater + 1 < right:
                parts.append((greater + 1, right))
            right = smaller - 1
        else:
            if left < smaller - 1:
                parts.append((left, smaller - 1))
            left = greater + 1

with open('output.txt', 'w') as file:
    file.write(' '.join(map(str, a)))
