with open('input.txt') as file:
    numbers = list(map(int, file.read().split()))

n = numbers[0]
a = numbers[1:n + 1]
temp = [0] * n


def merge_sort(left, right):
    if right - left <= 1:
        return

    middle = (left + right) // 2
    merge_sort(left, middle)
    merge_sort(middle, right)

    i = left
    j = middle
    k = left

    while i < middle and j < right:
        if a[i] <= a[j]:
            temp[k] = a[i]
            i += 1
        else:
            temp[k] = a[j]
            j += 1
        k += 1

    while i < middle:
        temp[k] = a[i]
        i += 1
        k += 1

    while j < right:
        temp[k] = a[j]
        j += 1
        k += 1

    a[left:right] = temp[left:right]
    output.write(f'{left + 1} {right} {a[left]} {a[right - 1]}\n')


with open('output.txt', 'w') as output:
    merge_sort(0, n)
    output.write(' '.join(map(str, a)))
