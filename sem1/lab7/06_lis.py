from bisect import bisect_left

with open('input.txt') as file:
    data = list(map(int, file.read().split()))

n = data[0]
a = data[1:n + 1]
tails = []
tail_indices = []
previous = [-1] * n

for i, value in enumerate(a):
    position = bisect_left(tails, value)

    if position > 0:
        previous[i] = tail_indices[position - 1]

    if position == len(tails):
        tails.append(value)
        tail_indices.append(i)
    else:
        tails[position] = value
        tail_indices[position] = i

answer = []
index = tail_indices[-1]

while index != -1:
    answer.append(a[index])
    index = previous[index]

answer.reverse()

with open('output.txt', 'w') as file:
    file.write(str(len(answer)) + '\n')
    file.write(' '.join(map(str, answer)))
