with open('input.txt') as file:
    citations = list(map(int, file.read().replace(',', ' ').split()))

n = len(citations)
counts = [0] * (n + 1)

for value in citations:
    counts[min(value, n)] += 1

articles = 0
h_index = 0

for h in range(n, 0, -1):
    articles += counts[h]
    if articles >= h:
        h_index = h
        break

with open('output.txt', 'w') as file:
    file.write(str(h_index))
