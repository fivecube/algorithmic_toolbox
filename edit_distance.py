# Uses python3
# import string
import random
import time

D = dict()
# T = dict()
back_track = dict()
# def edit_distance(s, t, l, m):
#     if not (l,m) in T:
#         if l==0:
#             T[l,m] = m
#         elif m==0:
#             T[l,m] = l
#         else:
#             if s[l-1] == t[m-1]:
#                 diff = 0
#             else:
#                 diff = 1
#             T[(l,m)] = min(edit_distance(s,t,l,m-1)+1,edit_distance(s,t,l-1,m)+1,edit_distance(s,t,l-1,m-1)+diff)
#
#     return T[(l,m)]

def edit_distance_iter(s,t):
    for i in range(len(s)+1):
        for j in range(len(t)+1):
            if i==0:
                D[(i,j)] = j
                back_track[(i,j)] = (0,j-1)
            elif j==0:
                D[(i,j)] = i
                back_track[(i,j)] = (i-1,0)
            else:
                temp1 = D[(i-1,j)]+1
                temp2 = D[(i,j-1)]+1
                diff = 0 if s[i-1]==t[j-1] else 1
                temp3 = D[(i-1,j-1)] + diff
                if (temp1 <= temp2 and temp1 <= temp3):
                    D[(i,j)] = temp1
                    back_track[(i,j)] = (i-1,j)
                elif temp2 <= temp1 and temp2 <= temp3:
                    D[(i,j)] = temp2
                    back_track[(i,j)] = (i,j-1)
                else:
                    D[(i,j)] = temp3
                    back_track[(i,j)] = (i-1,j-1)

    return D[(len(s),len(t))]

if __name__ == "__main__":
    s = input()
    t = input()
    l = len(s)
    m = len(t)
    # print(edit_distance(s,t,l,m))
    # print("\niter wala")
    print(edit_distance_iter(s,t))
    # print(back_track)
    templist1 = []
    templist2 = []
    row_col = (l,m)
    while(D[row_col]!=0):
        row,col = row_col
        if s[row-1] == t[col-1]:
            templist1.append(s[row-1])
            templist2.append(t[col-1])
        elif s[row-1] != t[col-1]:
            if back_track[row_col] == (row-1,col):
                templist1.append("-")
                templist2.append(t[col-1])
            elif back_track[row_col] == (row,col-1):
                templist1.append(s[row-1])
                templist2.append("-")
            else:
                templist1.append("*")
                templist2.append("*")
        row_col = back_track[row_col]
    templist1.reverse()
    templist2.reverse()
    print(templist1)
    print(templist2)




    # stress testing
    # count = 0
    # while(True):
    #     count+=1
    #     D = dict()
    #     T = dict()
    #     # print(count)
    #     so = str(random.randint(10,1000))
    #     to = str(random.randint(10,1000))
    #     lo = len(so)
    #     mo = len(to)
    #     rec = edit_distance(so,to,lo,mo)
    #     # time.sleep(1)
    #     iter = edit_distance_iter(so,to)
    #     if rec!= iter:
    #         print("Wrong Answer at",so,to)
    #         print("and rec is",rec," iter is",iter)
    #         break
    #     if not count%10:
    #         print(count," testcases passed")
