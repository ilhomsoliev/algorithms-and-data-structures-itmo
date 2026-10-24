with open('input.txt') as file:
    n = int(file.readline())
    keys = [0] * (n + 1)
    left = [0] * (n + 1)
    right = [0] * (n + 1)

    for i in range(1, n + 1):
        keys[i], left[i], right[i] = map(int, file.readline().split())

height = [0] * (n + 1)

for i in range(n, 0, -1):
    height[i] = 1 + max(height[left[i]], height[right[i]])

root = 1
child = right[root]

if height[left[child]] > height[right[child]]:
    middle = left[child]
    left[child] = right[middle]
    right[middle] = child
    right[root] = middle
    child = middle

right[root] = left[child]
left[child] = root
root = child

order = []
new_number = [0] * (n + 1)
stack = [root]

while stack:
    i = stack.pop()
    new_number[i] = len(order) + 1
    order.append(i)
    if right[i]:
        stack.append(right[i])
    if left[i]:
        stack.append(left[i])

with open('output.txt', 'w') as file:
    file.write(str(n) + '\n')
    for i in order:
        file.write(f'{keys[i]} {new_number[left[i]]} {new_number[right[i]]}\n')
