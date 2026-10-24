with open('input.txt') as file:
    n = int(file.read())

a, b = 0, 1
for i in range(n % 60):
    a, b = b, (a + b) % 10

with open('output.txt', 'w') as file:
    file.write(str(a))
