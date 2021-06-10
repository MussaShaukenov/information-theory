from collections import Counter
from random import randint
from browser import *


def part1():
    with open('hah.txt', 'r') as f:
        arr = list(f.read())
        d = []
        for key, value in sorted(Counter(arr).items()):
            p = str(value / len(arr))
            d.append((key, float(p)))
    return d


with open('hah.txt') as f:
    string = f.read()


class NodeTree(object):
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

    def nodes(self):
        return (self.left, self.right)

    def str(self):
        return '%s_%s' % (self.left, self.right)


def huffman_code_tree(node, left=True, binString=''):
    if type(node) is str:
        return {node: binString}
    (l, r) = node.children()
    d = dict()
    d.update(huffman_code_tree(l, True, binString + '0'))
    d.update(huffman_code_tree(r, False, binString + '1'))
    return d


freq = part1()
freq = sorted(freq, key=lambda x: x[1], reverse=True)

nodes = freq
while len(nodes) > 1:
    (key1, c1) = nodes[-1]
    (key2, c2) = nodes[-2]
    nodes = nodes[:-2]
    node = NodeTree(key1, key2)
    nodes.append(
        (node, c1 + c2))

    nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

huffmanCode = huffman_code_tree(nodes[0][0])


# part2

def part2():
    encoded = ''
    for i in string:
        for (char, _) in freq:
            if char == i:
                encoded += huffmanCode[char]

    return encoded


# part4
def part4():
    encoded = part2()
    if len(encoded) % 4 != 0:
        number_of_spaces = 4 - (len(encoded) % 4)
        encoded += '0' * number_of_spaces

    split_strings = []

    while encoded:
        split_strings.append(encoded[:4])
        encoded = encoded[4:]

    result_arr = []

    for i in split_strings:
        r1 = str(int(i[0]) ^ int(i[1]) ^ int(i[2]))
        r2 = str(int(i[1]) ^ int(i[2]) ^ int(i[3]))
        r3 = str(int(i[0]) ^ int(i[1]) ^ int(i[3]))
        i += r1 + r2 + r3
        result_arr.append(i)

    ready_for_checking = ''
    for i in result_arr:
        ready_for_checking += i

    return ready_for_checking


# part5
def part5(e):

    ready_for_checking = part4()

    bc_to_arr = []
    while ready_for_checking:
        bc_to_arr.append(ready_for_checking[:7])
        ready_for_checking = ready_for_checking[7:]

    errors_arr = []
    temp_str = ''

    for i in bc_to_arr:
      index_of_error = randint(0, 6)
      if i[index_of_error] == '1':
        temp_str = i[:index_of_error] + '0' + i[index_of_error + 1:]
        errors_arr.append(temp_str)
      else:
        temp_str = i[:index_of_error] + '1' + i[index_of_error + 1:]
        errors_arr.append(temp_str)

    error_binary_code = ''
    for i in errors_arr:
        error_binary_code += i

    document['p5_2'] <= error_binary_code
    document['p6_1'] <= error_binary_code


document['btn5'].bind('click', part5)