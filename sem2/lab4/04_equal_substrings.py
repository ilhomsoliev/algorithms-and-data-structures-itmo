from random import randrange

with open('input.txt', 'rb') as file:
    string = file.readline().rstrip(b'\r\n')
    queries_count = int(file.readline())
    queries = [tuple(map(int, file.readline().split())) for _ in range(queries_count)]

base = randrange(256, 1000000000)
mod1 = 1000000007
mod2 = 1000000009
power1 = [1]
power2 = [1]
hash1 = [0]
hash2 = [0]

for letter in string:
    power1.append(power1[-1] * base % mod1)
    power2.append(power2[-1] * base % mod2)
    hash1.append((hash1[-1] * base + letter) % mod1)
    hash2.append((hash2[-1] * base + letter) % mod2)

answers = []

for a, b, length in queries:
    first1 = (hash1[a + length] - hash1[a] * power1[length]) % mod1
    second1 = (hash1[b + length] - hash1[b] * power1[length]) % mod1

    if first1 != second1:
        answers.append('No')
        continue

    first2 = (hash2[a + length] - hash2[a] * power2[length]) % mod2
    second2 = (hash2[b + length] - hash2[b] * power2[length]) % mod2
    answers.append('Yes' if first2 == second2 else 'No')

with open('output.txt', 'w') as file:
    file.write('\n'.join(answers))
