with open('input.txt') as source, open('output.txt', 'w') as output:
    n, m = map(int, source.readline().split())
    left = [0] * (n + 1)
    right = [0] * (n + 1)

    for _ in range(m):
        command = source.readline().split()
        action = command[0]
        i = int(command[1])

        if action == 'left':
            j = int(command[2])
            neighbor = left[j]
            left[i] = neighbor
            right[i] = j
            left[j] = i
            if neighbor:
                right[neighbor] = i
        elif action == 'right':
            j = int(command[2])
            neighbor = right[j]
            right[i] = neighbor
            left[i] = j
            right[j] = i
            if neighbor:
                left[neighbor] = i
        elif action == 'leave':
            if left[i]:
                right[left[i]] = right[i]
            if right[i]:
                left[right[i]] = left[i]
            left[i] = 0
            right[i] = 0
        else:
            output.write(f'{left[i]} {right[i]}\n')
