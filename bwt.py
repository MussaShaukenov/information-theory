#  BORROWS WILLIAM TRANSFORM ALGORITHM ON PYTHON

#  encoding

with open('hah.txt', 'r') as f:
    s = f.read()
    
    
def bwt_encoding(s):
    arr = [s]
    i = 0

    for i in range(len(s)-1):  
        s = arr[i]
        char = s[-1]
        temp = s[:-1]
        s2 = char + temp
        arr.append(s2)
        
    arr = sorted(arr)

    s2 = ''
    for i in arr:
        s2 += i[-1]

    return s2

# print(bwt_encoding(s))
