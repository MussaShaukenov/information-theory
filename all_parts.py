from collections import Counter
from textwrap import wrap
from random import randint

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



#print(part1())

# part2

unique = {}
for (char, _) in freq:
    unique[char] = str(huffmanCode[char])

#print('\n' + 'Unique characters list: ')
#print(unique)

encoded = ''
encoded_dict = {}
key = 0
for i in string:
    for (char, _) in freq:
        if char == i:
            encoded += huffmanCode[char]
            encoded_dict[key] = huffmanCode[char]
            key += 1

#print('\n' + 'Encoded text:')
#print(encoded + '\n')

# part3

def part3(str):

    decoded = ''

    #for i in encoded.split(' '):
    #    for key, value in unique.items():
    #        if i == value:
    #            decoded += key

    for i in encoded_dict.values():
        for key, value in unique.items():
            if i == value:
                decoded += key

    print('\n' + 'Decoded text:')
    print(decoded)


#part4

split_strings = wrap(encoded, 4)
#print(split_strings)
result_arr = []
for i in split_strings:
    
    r1 = str(int(i[0]) ^ int(i[1]) ^ int(i[2]))
    r2 = str(int(i[1]) ^ int(i[2]) ^ int(i[3]))
    r3 = str(int(i[0]) ^ int(i[1]) ^ int(i[3]))
    i += r1 + r2 + r3
    result_arr.append(i)

#print('\n')
#print(result_arr)

ready_for_checking = ''
for i in result_arr:
    ready_for_checking += i

#print('\n')
#print(ready_for_checking)


#  part5 

bc_to_arr = wrap(ready_for_checking, 7)

#print(bc_to_arr)  # original binary code to array
print('\n')

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

#print(errors_arr)  # array with random errors
print('\n')

error_binary_code = ''
for i in errors_arr:
    error_binary_code += i


#print(error_binary_code)  # binary code with random errors
print('\n')



# part6

errored_arr = wrap(error_binary_code, 7) # wrap string from part5

#print(errored_arr)
print('\n')

syndromes = {
  #"000": "no error",
  "001": "6", #r3
  "010": "5", #r2
  "011": "3", #i4
  "100": "4", #r1
  "101": "0", #i1
  "110": "2", #i3
  "111": "1"  #i2
}

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

#print(error_indexes)   
print('\n')
#print(fixed_arr)
print('\n')
#print(bc_to_arr == fixed_arr) #check if fixed array is the same as original array from part5
print('\n')

final_arr = []
tempp = ''
for i in fixed_arr:
    tempp = i[:4]
    final_arr.append(tempp)

#print(final_arr)
print('\n')

final_str = ''
for i in final_arr:
    final_str += i


print(final_str)
print('\n')

#print(encoded == final_str) #check if final array is the same as encoded text from part2
print('\n')

part3(final_str)
