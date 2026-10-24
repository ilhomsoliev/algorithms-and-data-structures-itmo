votes = {}

with open('input.txt') as source:
    for line in source:
        name, count = line.split()
        votes[name] = votes.get(name, 0) + int(count)

with open('output.txt', 'w') as output:
    for name in sorted(votes):
        output.write(f'{name} {votes[name]}\n')
