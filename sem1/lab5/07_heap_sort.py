with open('input.txt') as file:
    data = list(map(int, file.read().split()))

n = data[0]
a = data[1:n + 1]


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


for i in range(n // 2 - 1, -1, -1):
    max_heapify(i, n)

answer = []

for end in range(n - 1, 0, -1):
    a[0], a[end] = a[end], a[0]
    answer.append(a[end])
    max_heapify(0, end)

answer.append(a[0])

with open('output.txt', 'w') as file:
    file.write(' '.join(map(str, answer)))
