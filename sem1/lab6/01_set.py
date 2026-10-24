numbers = set()

with open('input.txt') as source, open('output.txt', 'w') as output:
    n = int(source.readline())

    for _ in range(n):
        operation, value = source.readline().split()
        value = int(value)

        if operation == 'A':
            numbers.add(value)
        elif operation == 'D':
            numbers.discard(value)
        else:
            output.write('Y\n' if value in numbers else 'N\n')
