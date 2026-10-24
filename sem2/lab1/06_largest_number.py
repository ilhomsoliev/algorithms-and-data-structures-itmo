from functools import cmp_to_key

with open('input.txt') as file:
    data = file.read().split()

n = int(data[0])
numbers = data[1:n + 1]


def compare(a, b):
    if a + b > b + a:
        return -1
    if a + b < b + a:
        return 1
    return 0


numbers.sort(key=cmp_to_key(compare))

with open('output.txt', 'w') as file:
    file.write(''.join(numbers))
