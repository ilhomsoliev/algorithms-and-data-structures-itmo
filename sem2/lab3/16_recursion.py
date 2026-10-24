with open('input.txt') as file:
    n = int(file.readline())
    names = []
    calls = []

    for _ in range(n):
        names.append(file.readline().strip())
        count = int(file.readline())
        calls.append([file.readline().strip() for _ in range(count)])
        file.readline()

numbers = {name: i for i, name in enumerate(names)}
graph = [[numbers[name] for name in row] for row in calls]
answers = []

for start in range(n):
    stack = graph[start].copy()
    visited = [False] * n
    recursive = False

    while stack:
        current = stack.pop()
        if current == start:
            recursive = True
            break
        if not visited[current]:
            visited[current] = True
            stack.extend(graph[current])

    answers.append('YES' if recursive else 'NO')

with open('output.txt', 'w') as file:
    file.write('\n'.join(answers))
