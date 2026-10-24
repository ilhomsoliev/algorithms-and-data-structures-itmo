from collections import deque

queue = deque()

with open('input.txt') as source, open('output.txt', 'w') as output:
    m = int(source.readline())

    for _ in range(m):
        command = source.readline()
        if command[0] == '+':
            queue.append(int(command[1:]))
        else:
            output.write(str(queue.popleft()) + '\n')
