with open('input.txt') as file:
    data = list(map(int, file.read().split()))

n = data[0]
a = data[1:1 + n]
positions = [1]

for i in range(1, n):
    value = a[i]
    j = i - 1
    while j >= 0 and a[j] > value:
        a[j + 1] = a[j]
        j -= 1
    a[j + 1] = value
    positions.append(j + 2)

with open('output.txt', 'w') as file:
    file.write(' '.join(map(str, positions)) + '\n')
    file.write(' '.join(map(str, a)))
