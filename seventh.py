from browser import *

def part7(e):
    with open('hah.txt', 'r') as f:
        s = f.read()
        arr = [s]
        i = 0

        for i in range(len(s) - 1):
            s = arr[i]
            char = s[-1]
            temp = s[:-1]
            s2 = char + temp
            arr.append(s2)

        arr = sorted(arr)

        s2 = ''
        for i in arr:
            s2 += i[-1]

    document['p7_2'] <= s2


document['btn7'].bind('click', part7)
