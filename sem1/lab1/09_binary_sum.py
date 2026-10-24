with open('input.txt') as file:
    a, b = file.read().split()

n = len(a)
result = ['0'] * (n + 1)
carry = 0

for i in range(n - 1, -1, -1):
    total = int(a[i]) + int(b[i]) + carry
    result[i + 1] = str(total % 2)
    carry = total // 2

result[0] = str(carry)

with open('output.txt', 'w') as file:
    file.write(''.join(result))
