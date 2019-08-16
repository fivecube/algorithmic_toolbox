# Uses python3
import sys
# import random

# def optimal_sequence(n):
#     sequence = []
#     while n >= 1:
#         sequence.append(n)
#         if n % 3 == 0:
#             n = n // 3
#         elif n % 2 == 0:
#             n = n // 2
#         else:
#             n = n - 1
#     return reversed(sequence)
# n=4


no_of_op = dict()
no_of_op[1] = 0
no_of_op[2] = 1
no_of_op[3] = 1

back_track = dict()
back_track[1] = 1
back_track[2] = 1
back_track[3] = 1


def optimal_sequence_adv_2(n):
    if n<=3:
        return no_of_op[n]
    else:
        for i in range(4,n+1):
            temp1 = float("inf")
            temp2 = float("inf")
            if i not in no_of_op:
                if i%2==0:
                    temp1 = no_of_op[i//2]
                if i%3==0:
                    temp2 = no_of_op[i//3]
                temp3 = no_of_op[i-1]
                if temp1<temp2 and temp1<temp3:
                    back_track[i] = i//2
                    no_of_op[i] = temp1 + 1
                elif temp2<=temp1 and temp2<=temp3:
                    back_track[i] = i//3
                    no_of_op[i] = temp2 + 1
                else:
                    back_track[i] = i-1
                    no_of_op[i] = temp3 + 1
    return no_of_op[n]

# sequence_adv = [0]*10**6
# sequence_adv[2] = 1
# sequence_adv[3] = 1
#
# def optimal_sequence_adv(n):
#     sequence = []
#     if n==1:
#         return sequence_adv[n],[1]
#     if n==2:
#         return sequence_adv[n],[1,2]
#     if n==3:
#         return sequence_adv[n],[1,3]
#     else:
#         if not sequence_adv[n//2]:
#             sequence_adv[n//2],sequence_1 = optimal_sequence_adv(n//2)
#         if not sequence_adv[n//3]:
#             sequence_adv[n//3],sequence_2 = optimal_sequence_adv(n//3)
#         if (sequence_adv[n//2]+n%2 + 1) < (sequence_adv[n//3]+n%3 + 1):
#             print("ok1",sequence_1)
#             sequence_1.append(n//2)
#             if n%2:
#                 sequence_1.append(n//2 + 1)
#             sequence_adv[n] = sequence_adv[n//2]+n%2 + 1
#             return sequence_adv[n],sequence_1
#         else:
#             print("ok2",sequence_2)
#             sequence_2.append(n//2)
#             if n%3:
#                 sequence_2.append(n//3 + 1)
#             if n%3 == 2:
#                 sequence_2.append(n//3 + 2)
#             sequence_adv[n] = sequence_adv[n//3]+n%3 + 1
#             return sequence_adv[n],sequence_2
#         # sequence_adv[n] = min(sequence_adv[n//2]+n%2 + 1,sequence_adv[n//3]+n%3 + 1)
#
#         return sequence_adv[n],sequence


# sequence_adv_2 = [0]*10**6
# sequence_adv_2[2] = 1
# sequence_adv_2[3] = 1
# last_accesed = 3
# def optimal_sequence_adv_2(n):
#     global last_accesed
#     for i in range(last_accesed,n+1):
#         sequence_adv_2[i] = min(sequence_adv_2[i-1] + 1,sequence_adv_2[i//2]+i%2 + 1,sequence_adv_2[i//3]+i%3 + 1)
#     last_accesed = n
#     return sequence_adv_2[n]

# input = sys.stdin.read()
n = int(input())
# sequence = list(optimal_sequence(n))
print(optimal_sequence_adv_2(n))
# print("\n")
# print(no_of_op)
# print("\n")
# print(back_track)
dic_value = n
# print(dic_value,end = " ")
list_numbers = []
while(dic_value!=1):
    list_numbers.append(dic_value)
    # print(dic_value,end = " ")
    dic_value = back_track[dic_value]
list_numbers.append(1)
for i in list_numbers[::-1]:
    print(i,end = " ")

# no_of_op,sequence = optimal_sequence_adv(n)
# print(len(sequence) - 1)
# for x in sequence:
#     print(x, end=' ')
# i = 0
# while(True):
#     i+=1
#     n = random.randint(1,100000)
# print(optimal_sequence_adv(n))
#     if optimal_sequence_adv(n) != optimal_sequence_adv_2(n):
#         print("Wrong Answer at ",n)
#         break
#     m_1 = optimal_sequence_adv_2(n)
#     m_2 = optimal_sequence_adv(n)
#     if not i%1000:
#         print(i,"testcases passed")
