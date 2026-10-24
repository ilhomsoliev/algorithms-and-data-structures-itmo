items = {}
last = None

with open('input.txt') as source, open('output.txt', 'w') as output:
    n = int(source.readline())

    for _ in range(n):
        command = source.readline().split()
        action = command[0]
        key = command[1]

        if action == 'put':
            value = command[2]
            if key in items:
                items[key][0] = value
            else:
                items[key] = [value, last, None]
                if last is not None:
                    items[last][2] = key
                last = key

        elif action == 'delete':
            if key in items:
                value, previous, following = items.pop(key)
                if previous is not None:
                    items[previous][2] = following
                if following is not None:
                    items[following][1] = previous
                else:
                    last = previous

        elif action == 'get':
            output.write(items[key][0] + '\n' if key in items else '<none>\n')

        elif action == 'prev':
            if key in items and items[key][1] is not None:
                output.write(items[items[key][1]][0] + '\n')
            else:
                output.write('<none>\n')

        else:
            if key in items and items[key][2] is not None:
                output.write(items[items[key][2]][0] + '\n')
            else:
                output.write('<none>\n')
