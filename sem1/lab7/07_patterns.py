with open('input.txt') as file:
    pattern = file.readline().rstrip('\r\n')
    text = file.readline().rstrip('\r\n')

masks = {}

for i, letter in enumerate(text, 1):
    masks[letter] = masks.get(letter, 0) | (1 << i)

all_positions = (1 << (len(text) + 1)) - 1
matches = 1

for symbol in pattern:
    if symbol == '*':
        first = matches & -matches
        matches = all_positions ^ (first - 1)
    elif symbol == '?':
        matches = (matches << 1) & all_positions
    else:
        matches = (matches << 1) & masks.get(symbol, 0)

    if matches == 0:
        break

with open('output.txt', 'w') as file:
    file.write('YES' if matches & (1 << len(text)) else 'NO')
