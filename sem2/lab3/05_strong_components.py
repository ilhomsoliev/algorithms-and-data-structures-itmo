with open('input.txt') as file:
    n, m = map(int, file.readline().split())
    graph = [[] for _ in range(n + 1)]
    reversed_graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v = map(int, file.readline().split())
        graph[u].append(v)
        reversed_graph[v].append(u)

visited = [False] * (n + 1)
order = []

for start in range(1, n + 1):
    if visited[start]:
        continue

    visited[start] = True
    stack = [(start, 0)]

    while stack:
        vertex, position = stack[-1]

        if position == len(graph[vertex]):
            order.append(vertex)
            stack.pop()
        else:
            stack[-1] = (vertex, position + 1)
            neighbor = graph[vertex][position]
            if not visited[neighbor]:
                visited[neighbor] = True
                stack.append((neighbor, 0))

visited = [False] * (n + 1)
components = 0

for start in reversed(order):
    if visited[start]:
        continue

    components += 1
    visited[start] = True
    stack = [start]

    while stack:
        vertex = stack.pop()
        for neighbor in reversed_graph[vertex]:
            if not visited[neighbor]:
                visited[neighbor] = True
                stack.append(neighbor)

with open('output.txt', 'w') as file:
    file.write(str(components))
