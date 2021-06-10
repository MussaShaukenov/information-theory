from collections import Counter
from browser import *


def part1():
    with open('hah.txt', 'r') as f:
        arr = list(f.read())
        d = []
        for key, value in sorted(Counter(arr).items()):
            p = str(value / len(arr))
            d.append((key, float(p)))
    return d

# def part1():
#     string = document['p1_1'].value
#     arr = list(string)
#     d = []
#     for key, value in sorted(Counter(arr).items()):
#         p = str(value / len(arr))
#         d.append((key, float(p)))
#
#     return d


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

def part2(e):
    encoded = ''
    for i in string:
        for (char, _) in freq:
            if char == i:
                encoded += huffmanCode[char]

    document['p2_2'] <= encoded
    document['p4_1'] <= encoded


document['btn2'].bind('click', part2)
