with open('input.txt') as file:
    n, k = map(int, file.readline().split())
    points = [tuple(map(int, file.readline().split())) for _ in range(n)]

points.sort(key=lambda point: point[0] ** 2 + point[1] ** 2)

with open('output.txt', 'w') as file:
    file.write(','.join(f'[{x},{y}]' for x, y in points[:k]))
