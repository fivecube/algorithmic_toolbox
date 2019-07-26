# Uses python3
import sys
import math
# import random
def n_sum(n):
    return (n*(n+1))//2

def rev_sum(n):
    return (math.sqrt(1+8*n)-1)//2

# def optimal_summands(n):
#     summands = []
#     candies_left = n
#     i = 1
#     while(candies_left>0):
#         # print(i)
#         if i not in summands and candies_left-i not in summands and i!=candies_left-i:
#             summands.append(i)
#             candies_left-=i
#         i+=1
#     return summands

# def optimal_summands_adv(n):
#     i = 1
#     summands = []
#     candies_left = n
#     while(n_sum(i)<=n and n-n_sum(i) not in summands):
#         # print("i is ",i,"and sum is ",n_sum(i))
#         if i!=n-n_sum(i):
#             # print("here")
#             summands.append(i)
#             candies_left-=i
#         i+=1
#     if candies_left:
#         summands.append(candies_left)
#     return summands

def optimal_summands_very_adv(n):
    summands = []
    i = int(rev_sum(n))
    over = 1
    while(over):
        if n-n_sum(i)>i:
            over = 0
            break
        i-=1
    for j in range(1,i+1):
        summands.append(j)
    summands.append(n-n_sum(i))

    return summands


if __name__ == '__main__':
    input = sys.stdin.read()
    summands = optimal_summands_very_adv(int(input))
    print(len(summands))
    for x in summands:
        print(x, end=' ')
    # count = 0
    # while True:
    #     count+=1
    #     n = random.randint(10*8,10**9)
        # summands_1 = optimal_summands_adv(n)
        # summands_2 = optimal_summands_very_adv(n)
        # if summands_1!=summands_2:
        #     print("Wrong Answer for n =",n)
        # if count%10 == 0:
        #     print(count,"testcases passed")
        # print(count,"testcases passed")
        # print(len(summands))
        # for x in summands:
        #     print(x, end=' ')
        # print("\n","###########################################")
