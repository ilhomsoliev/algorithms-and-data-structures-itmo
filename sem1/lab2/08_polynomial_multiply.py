with open('input.txt') as file:
    lines = file.readlines()

n = int(lines[0])
a = list(map(int, lines[1].split()))[::-1]
b = list(map(int, lines[2].split()))[::-1]

size = 1
while size < n:
    size *= 2

a += [0] * (size - n)
b += [0] * (size - n)


def multiply(a, b):
    length = len(a)
    if length == 1:
        return [a[0] * b[0]]

    half = length // 2
    low = multiply(a[:half], b[:half])
    high = multiply(a[half:], b[half:])

    sum_a = [a[i] + a[i + half] for i in range(half)]
    sum_b = [b[i] + b[i + half] for i in range(half)]
    middle = multiply(sum_a, sum_b)

    result = [0] * (2 * length - 1)
    for i in range(2 * half - 1):
        result[i] += low[i]
        result[i + half] += middle[i] - low[i] - high[i]
        result[i + 2 * half] += high[i]
    return result


answer = multiply(a, b)[:2 * n - 1][::-1]

with open('output.txt', 'w') as file:
    file.write(' '.join(map(str, answer)))
