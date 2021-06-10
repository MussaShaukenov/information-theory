from collections import Counter
from random import randint
from browser import *

with open('hah.txt') as f:
    string = f.read()
    document['p1_1'] <= string
    document['p2_1'] <= string


def part1():
    with open('hah.txt', 'r') as f:
        arr = list(f.read())
        d = []
        for key, value in sorted(Counter(arr).items()):
            p = str(value / len(arr))
            d.append((key, float(p)))
    return d


def show1():
    document['p1_2'] <= str(part1())


document['btn1'].bind('click', show1)


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
                
    return encoded  # encoded binary sequence


def show2():
    document['p2_2'] <= part2()
    document['p3_1'] <= part2()
    document['p4_1'] <= encoded


document['btn2'].bind('click', show2)


def unique_dict(freq):
    unique = {}
    for (char, _) in freq:
        unique[char] = str(huffmanCode[char])
    return unique


# part3


def part3(s):

    encoded_dict = {}
    key = 0
    for i in string:
        for (char, _) in freq:
            if char == i:
                encoded_dict[key] = huffmanCode[char]
                key += 1

    decoded = ''
    unique = unique_dict(freq)

    for i in encoded_dict.values():
        for key, value in unique.items():
            if i == value:
                decoded += key

    document['p3_2'] <= decoded


document['btn3'].bind('click', part3)


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

    document['p4_2'] <= ready_for_checking  # binary sequence with r1, r2, r3


document['btn4'].bind('click', part4)


# part5 

def part5():
    ready_for_checking = part4()

    bc_to_arr = []
    while ready_for_checking:
        bc_to_arr.append(ready_for_checking[:7])
        ready_for_checking = ready_for_checking[7:]

    errors_arr = []  # with errors
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


document['btn5'].bind('click', part5)

# part6

def part6():
    error_binary_code = part5()

    errored_arr = []
    while error_binary_code:
        errored_arr.append(error_binary_code[:7])
        error_binary_code = error_binary_code[7:]

    syndromes = {
        "001": "6",  # r3
        "010": "5",  # r2
        "011": "3",  # i4
        "100": "4",  # r1
        "101": "0",  # i1
        "110": "2",  # i3
        "111": "1"}  # i2

    error_indexes = []
    fixed_arr = []
    temp = ''

    for i in errored_arr:
        syndrome = ''

        s1 = str(int(i[4]) ^ int(i[0]) ^ int(i[1]) ^ int(i[2]))
        s2 = str(int(i[5]) ^ int(i[1]) ^ int(i[2]) ^ int(i[3]))
        s3 = str(int(i[6]) ^ int(i[0]) ^ int(i[1]) ^ int(i[3]))

        syndrome += s1 + s2 + s3

        error_index = ''

        for key, value in syndromes.items():
            if syndrome == key:
                error_index = value

        error_indexes.append(error_index)

        if i[int(error_index)] == '1':
            temp = i[:int(error_index)] + '0' + i[int(error_index) + 1:]
            fixed_arr.append(temp)
        else:
            temp = i[:int(error_index)] + '1' + i[int(error_index) + 1:]
            fixed_arr.append(temp)

    final_arr = []
    tempp = ''
    for i in fixed_arr:
        tempp = i[:4]
        final_arr.append(tempp)

    final_str = ''
    for i in final_arr:
        final_str += i

    document['p6_2'] <= final_str


document['btn6'].bind('click', part6)
