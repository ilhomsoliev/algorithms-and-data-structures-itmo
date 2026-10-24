with open('input.txt', 'rb') as file:
    pattern = file.readline().rstrip(b'\r\n')
    text = file.readline().rstrip(b'\r\n')

base = 263
mod = 1000000007
length = len(pattern)
positions = []

if length <= len(text):
    pattern_hash = 0
    window_hash = 0

    for i in range(length):
        pattern_hash = (pattern_hash * base + pattern[i]) % mod
        window_hash = (window_hash * base + text[i]) % mod

    highest_power = pow(base, length - 1, mod)

    for i in range(len(text) - length + 1):
        if window_hash == pattern_hash and text.startswith(pattern, i):
            positions.append(str(i + 1))

        if i + length < len(text):
            window_hash = (window_hash - text[i] * highest_power) % mod
            window_hash = (window_hash * base + text[i + length]) % mod

with open('output.txt', 'w') as file:
    file.write(str(len(positions)) + '\n' + ' '.join(positions))
