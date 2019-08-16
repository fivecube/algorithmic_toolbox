#Uses python3

import sys

T = dict()
back_track = dict()

def lcs2(a, b):
    for i in range(len(a)+1):
        for j in range(len(b)+1):
            if i==0 or j==0:
                T[(i,j)]=0
                back_track[(i,j)] = None
            else:
                if a[i-1]==b[j-1]:
                    T[(i,j)] = 1+T[(i-1,j-1)]
                    back_track[(i,j)] = (i-1,j-1)
                else:
                    temp1 = T[(i-1,j)]
                    temp2 = T[(i,j-1)]
                    if temp1>temp2:
                        T[(i,j)] = temp1
                        back_track[(i,j)] = (i-1,j)
                    else:
                        T[(i,j)] = temp2
                        back_track[(i,j)] = (i,j-1)
    return T[(len(a),len(b))]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
    # print(back_track)
    traveller = (len(a),len(b))
    templist = []
    while(traveller!=None):
        row,col = traveller
        if a[row-1] == b[col-1] and back_track[traveller] == (row-1,col-1):
            templist.append(a[row-1])
        traveller = back_track[traveller]
    templist.reverse()
    print(templist)
