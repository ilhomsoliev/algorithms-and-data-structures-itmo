with open('input.txt') as file:
    n = int(file.readline())
    nodes = [tuple(map(int, file.readline().split())) for _ in range(n)]

inorder = []
stack = []
current = 0

while stack or current != -1:
    while current != -1:
        stack.append(current)
        current = nodes[current][1]

    current = stack.pop()
    inorder.append(nodes[current][0])
    current = nodes[current][2]

preorder = []
stack = [0]

while stack:
    current = stack.pop()
    preorder.append(nodes[current][0])
    if nodes[current][2] != -1:
        stack.append(nodes[current][2])
    if nodes[current][1] != -1:
        stack.append(nodes[current][1])

postorder = []
stack = [(0, False)]

while stack:
    current, visited = stack.pop()
    if visited:
        postorder.append(nodes[current][0])
    else:
        stack.append((current, True))
        if nodes[current][2] != -1:
            stack.append((nodes[current][2], False))
        if nodes[current][1] != -1:
            stack.append((nodes[current][1], False))

with open('output.txt', 'w') as file:
    file.write(' '.join(map(str, inorder)) + '\n')
    file.write(' '.join(map(str, preorder)) + '\n')
    file.write(' '.join(map(str, postorder)))
