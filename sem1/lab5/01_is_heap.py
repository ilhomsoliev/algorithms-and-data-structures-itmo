with open('input.txt') as file:
    data = list(map(int, file.read().split()))

n = data[0]
a = data[1:n + 1]
answer = 'YES'

for i in range(1, n):
    if a[(i - 1) // 2] > a[i]:
        answer = 'NO'
        break

with open('output.txt', 'w') as file:
    file.write(answer)
