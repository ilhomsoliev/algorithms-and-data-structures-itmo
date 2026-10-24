with open('input.txt') as file:
    data = list(map(int, file.read().split()))

n = data[0]
values = data[1:n + 1]
total = sum(values)
answer = 0

if total % 3 == 0:
    target = total // 3

    if max(values) <= target:
        states = [-1] * (1 << n)
        states[0] = 0
        bits = [1 << i for i in range(n)]

        for mask in range(1 << n):
            current = states[mask]
            if current == -1:
                continue

            for i in range(n):
                next_mask = mask | bits[i]
                new_sum = current + values[i]

                if next_mask != mask and states[next_mask] == -1 and new_sum <= target:
                    states[next_mask] = 0 if new_sum == target else new_sum

        if states[-1] == 0:
            answer = 1

with open('output.txt', 'w') as file:
    file.write(str(answer))
