with open('input.txt') as file:
    n = int(file.read())

a, b = 0, 1
for i in range(n):
    a, b = b, a + b

with open('output.txt', 'w') as file:
    file.write(str(a))
