from collections import deque

with open('input.txt') as file:
    n, m = map(int, file.readline().split())
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v = map(int, file.readline().split())
        graph[u].append(v)
        graph[v].append(u)

    start, finish = map(int, file.readline().split())

distance = [-1] * (n + 1)
distance[start] = 0
queue = deque([start])

while queue and distance[finish] == -1:
    vertex = queue.popleft()
    for neighbor in graph[vertex]:
        if distance[neighbor] == -1:
            distance[neighbor] = distance[vertex] + 1
            queue.append(neighbor)

with open('output.txt', 'w') as file:
    file.write(str(distance[finish]))
