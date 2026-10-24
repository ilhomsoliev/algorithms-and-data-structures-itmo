with open('input.txt') as file:
    n = int(file.read())

neighbors = (
    (4, 6),
    (6, 8),
    (7, 9),
    (4, 8),
    (0, 3, 9),
    (),
    (0, 1, 7),
    (2, 6),
    (1, 3),
    (2, 4)
)

counts = [1] * 10
counts[0] = 0
counts[8] = 0

for _ in range(n - 1):
    counts = [sum(counts[neighbor] for neighbor in neighbors[digit]) % 10**9
              for digit in range(10)]

with open('output.txt', 'w') as file:
    file.write(str(sum(counts) % 10**9))
