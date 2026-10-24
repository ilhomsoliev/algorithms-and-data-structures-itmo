with open('input.txt') as file:
    n = int(file.readline())
    nodes = [tuple(map(int, file.readline().split())) for _ in range(n)]

correct = True
stack = [(0, None, None)] if n else []

while stack:
    index, lower, upper = stack.pop()
    key, left, right = nodes[index]

    if (lower is not None and key <= lower) or (upper is not None and key >= upper):
        correct = False
        break

    if left != -1:
        stack.append((left, lower, key))
    if right != -1:
        stack.append((right, key, upper))

with open('output.txt', 'w') as file:
    file.write('CORRECT' if correct else 'INCORRECT')
