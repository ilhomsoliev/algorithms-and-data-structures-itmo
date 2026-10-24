with open('input.txt') as file:
    expression = file.read().strip()

numbers = list(map(int, expression[::2]))
operations = expression[1::2]
n = len(numbers)
minimum = [[0] * n for _ in range(n)]
maximum = [[0] * n for _ in range(n)]

for i, value in enumerate(numbers):
    minimum[i][i] = value
    maximum[i][i] = value


def calculate(a, b, operation):
    if operation == '+':
        return a + b
    if operation == '-':
        return a - b
    return a * b


for length in range(2, n + 1):
    for left in range(n - length + 1):
        right = left + length - 1
        low = float('inf')
        high = float('-inf')

        for middle in range(left, right):
            for a in (minimum[left][middle], maximum[left][middle]):
                for b in (minimum[middle + 1][right], maximum[middle + 1][right]):
                    value = calculate(a, b, operations[middle])
                    low = min(low, value)
                    high = max(high, value)

        minimum[left][right] = low
        maximum[left][right] = high

with open('output.txt', 'w') as file:
    file.write(str(maximum[0][n - 1]))
