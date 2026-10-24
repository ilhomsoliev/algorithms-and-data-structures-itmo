import random


class Node:
    __slots__ = ('key', 'priority', 'left', 'right')

    def __init__(self, key):
        self.key = key
        self.priority = random.getrandbits(64)
        self.left = None
        self.right = None


def rotate_left(node):
    child = node.right
    node.right = child.left
    child.left = node
    return child


def rotate_right(node):
    child = node.left
    node.left = child.right
    child.right = node
    return child


def insert(node, key):
    if node is None:
        return Node(key)
    if key < node.key:
        node.left = insert(node.left, key)
        if node.left.priority > node.priority:
            node = rotate_right(node)
    elif key > node.key:
        node.right = insert(node.right, key)
        if node.right.priority > node.priority:
            node = rotate_left(node)
    return node


def delete(node, key):
    if node is None:
        return None
    if key < node.key:
        node.left = delete(node.left, key)
    elif key > node.key:
        node.right = delete(node.right, key)
    elif node.left is None:
        return node.right
    elif node.right is None:
        return node.left
    elif node.left.priority > node.right.priority:
        node = rotate_right(node)
        node.right = delete(node.right, key)
    else:
        node = rotate_left(node)
        node.left = delete(node.left, key)
    return node


root = None

with open('input.txt') as source, open('output.txt', 'w') as output:
    for line in source:
        action, text = line.split()
        key = int(text)

        if action == 'insert':
            root = insert(root, key)
        elif action == 'delete':
            root = delete(root, key)
        else:
            current = root
            answer = None

            if action == 'exists':
                while current is not None:
                    if key == current.key:
                        answer = True
                        break
                    current = current.left if key < current.key else current.right
                output.write('true\n' if answer else 'false\n')

            elif action == 'next':
                while current is not None:
                    if current.key > key:
                        answer = current.key
                        current = current.left
                    else:
                        current = current.right
                output.write(str(answer) + '\n' if answer is not None else 'none\n')

            else:
                while current is not None:
                    if current.key < key:
                        answer = current.key
                        current = current.right
                    else:
                        current = current.left
                output.write(str(answer) + '\n' if answer is not None else 'none\n')
