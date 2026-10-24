pairs = {')': '(', ']': '['}

with open('input.txt') as source, open('output.txt', 'w') as output:
    n = int(source.readline())

    for _ in range(n):
        stack = []
        correct = True

        for bracket in source.readline().strip():
            if bracket in '([':
                stack.append(bracket)
            elif not stack or stack.pop() != pairs[bracket]:
                correct = False
                break

        output.write('YES\n' if correct and not stack else 'NO\n')
