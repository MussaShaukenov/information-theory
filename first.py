from collections import Counter
from browser import *

with open('hah.txt') as f:
    string = f.read()
    document['p1_1'] <= string
    document['p2_1'] <= string
    document['p7_1'] <= string


def part1(e):
    with open('hah.txt', 'r') as f:
        arr = list(f.read())
        d = []
        for key, value in sorted(Counter(arr).items()):
            p = str(value / len(arr))
            d.append((key, float(p)))

    document['p1_2'] <= str(d)


document['btn1'].bind('click', part1)

