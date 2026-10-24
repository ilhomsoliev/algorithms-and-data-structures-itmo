with open('input.txt') as file:
    n = int(file.readline())
    segments = [tuple(map(int, file.readline().split())) for _ in range(n)]

segments.sort(key=lambda segment: segment[1])
points = []

for left, right in segments:
    if not points or points[-1] < left:
        points.append(right)

with open('output.txt', 'w') as file:
    file.write(str(len(points)) + '\n')
    file.write(' '.join(map(str, points)))
