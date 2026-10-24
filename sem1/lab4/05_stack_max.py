stack = []
maximums = []

with open('input.txt') as source, open('output.txt', 'w') as output:
    n = int(source.readline())

    for _ in range(n):
        command = source.readline().split()

        if command[0] == 'push':
            value = int(command[1])
            stack.append(value)
            maximums.append(max(value, maximums[-1]) if maximums else value)
        elif command[0] == 'pop':
            stack.pop()
            maximums.pop()
        else:
            output.write(str(maximums[-1]) + '\n')
