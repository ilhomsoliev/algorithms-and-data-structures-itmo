with open('input.txt') as file:
    a, b = map(int, file.read().split())

with open('output.txt', 'w') as file:
    file.write(str(a + b))
