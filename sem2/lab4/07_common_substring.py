from random import randrange

base = randrange(256, 1000000000)
mod1 = 1000000007
mod2 = 1000000009


def make_hashes(string):
    first = [0]
    second = [0]

    for letter in string:
        first.append((first[-1] * base + letter) % mod1)
        second.append((second[-1] * base + letter) % mod2)

    return first, second


def common_substring(s, t):
    s1, s2 = make_hashes(s)
    t1, t2 = make_hashes(t)
    powers1 = [1]
    powers2 = [1]

    for _ in range(min(len(s), len(t))):
        powers1.append(powers1[-1] * base % mod1)
        powers2.append(powers2[-1] * base % mod2)

    def find(length):
        seen = {}
        power1 = powers1[length]
        power2 = powers2[length]

        for i in range(len(s) - length + 1):
            h1 = (s1[i + length] - s1[i] * power1) % mod1
            h2 = (s2[i + length] - s2[i] * power2) % mod2
            key = h1 * mod2 + h2
            if key not in seen:
                seen[key] = i

        for j in range(len(t) - length + 1):
            h1 = (t1[j + length] - t1[j] * power1) % mod1
            h2 = (t2[j + length] - t2[j] * power2) % mod2
            key = h1 * mod2 + h2
            i = seen.get(key)
            if i is not None and s[i:i + length] == t[j:j + length]:
                return i, j

        return None

    left = 0
    right = min(len(s), len(t)) + 1
    answer = (0, 0, 0)

    while right - left > 1:
        length = (left + right) // 2
        position = find(length)

        if position is None:
            right = length
        else:
            left = length
            answer = position[0], position[1], length

    return answer


answers = []

with open('input.txt', 'rb') as file:
    for line in file:
        words = line.split()
        if not words:
            continue

        i, j, length = common_substring(words[0], words[1])
        answers.append(f'{i} {j} {length}')

with open('output.txt', 'w') as file:
    file.write('\n'.join(answers))
