#Uses python3

import sys
T = dict()
back_track = dict()


def lcs3(a, b, c):
    for i in range(len(a)+1):
        for j in range(len(b)+1):
            for k in range(len(c)+1):
                if i==0 or j==0 or k==0:
                    T[(i,j,k)] = 0
                    back_track[(i,j,k)] = None
                else:
                    if a[i-1] == b[j-1] and a[i-1] == c[k-1]:
                        T[(i,j,k)] = 1+T[(i-1,j-1,k-1)]
                        back_track[(i,j,k)] = (i-1,j-1,k-1)
                    else:
                        temp1 = T[(i-1,j,k)]
                        temp2 = T[(i-1,j-1,k)]
                        temp3 = T[(i-1,j,k-1)]
                        temp4 = T[(i,j-1,k)]
                        temp5 = T[(i,j-1,k-1)]
                        temp6 = T[(i,j,k-1)]
                        if temp1>=temp2 and temp1>=temp3 and temp1>=temp4 and temp1>=temp5 and temp1>=temp6:
                            T[(i,j,k)] = temp1
                            back_track[(i,j,k)] = (i-1,j,k)
                        if temp2>=temp1 and temp2>=temp3 and temp2>=temp4 and temp2>=temp5 and temp2>=temp6:
                            T[(i,j,k)] = temp2
                            back_track[(i,j,k)] = (i-1,j-1,k)
                        if temp3>=temp1 and temp3>=temp2 and temp3>=temp4 and temp3>=temp5 and temp3>=temp6:
                            T[(i,j,k)] = temp3
                            back_track[(i,j,k)] = (i-1,j,k-1)
                        if temp4>=temp1 and temp4>=temp2 and temp4>=temp3 and temp4>=temp5 and temp4>=temp6:
                            T[(i,j,k)] = temp4
                            back_track[(i,j,k)] = (i,j-1,k)
                        if temp5>=temp2 and temp5>=temp3 and temp5>=temp4 and temp5>=temp1 and temp5>=temp6:
                            T[(i,j,k)] = temp5
                            back_track[(i,j,k)] = (i,j-1,k-1)
                        if temp6>=temp2 and temp6>=temp3 and temp6>=temp4 and temp6>=temp5 and temp6>=temp1:
                            T[(i,j,k)] = temp6
                            back_track[(i,j,k)] = (i,j,k-1)
                        # print(T)
    return T[(len(a),len(b),len(c))]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
    # traveller = (len(a),len(b),len(c))
    # templist = []
    # while(traveller!=None):
    #     row,col,col2 = traveller
    #     if a[row-1] == b[col-1] and a[row-1] == c[col2-1] and back_track[traveller] == (row-1,col-1,col2-1):
    #         templist.append(a[row-1])
    #     traveller = back_track[traveller]
    # templist.reverse()
    # print(templist)
