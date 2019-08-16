# Uses python3
import sys
import random

def binary_search(keys, query ,low,high):
    # assert all(keys[i] < keys[i + 1] for i in range(len(keys) - 1))
    # assert 1 <= len(keys) <= 10 ** 4
    # print("low is ",low,"and high is ",high)
    if low > high:
        return -1
    mid = (low+high)//2
    if query == keys[mid]:
        return mid
    elif query>keys[mid]:
        low = mid+1
        return binary_search(keys,query,low,high)
    elif query< keys[mid]:
        high = mid-1
        return binary_search(keys,query,low,high)
    else:
        return -1

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    # count = 0
    # while 1:
    #     count+=1
    #     n = random.randint(1,10**2)
    #     k = random.randint(1,10**2)
    #     a = []
    #     prvs = 1
    #     for i in range(n):
    #         current = random.randint(prvs,10**3)
    #         prvs = current
    #         a.append(current)
    #     x = []
    #     for i in range(k):
    #         x.append(random.randint(1,10**3))
    #
    #     for q in x:
    #         ans_bin = binary_search(a,q,0,n-1)
    #         ans_lin = linear_search(a,q)
    #         if ans_bin != ans_lin:
    #             print("Wrong ans")
    #             break
    #     if not count%100:
    #         print(count,"testcases passed")
    for x in data[n + 2:]:
    # replace with the call to binary_search when implemented
        # print(linear_search(a, x), end = ' ')
        print(binary_search(a, x,0,len(a)-1), end = ' ')
