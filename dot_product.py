#Uses python3

import sys

def max_dot_product(a, b):
    #write your code here
    res = 0
    a = sorted(a)
    b = sorted(b)
    # print(a)
    # print(b)
    for i in range(len(a)):
        # print(i)
        res += a[i] * b[i]
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]

    # n = int(input())
    # a = list(map(int,input().split(' ')))
    # b = list(map(int,input().split(' ')))
    print(max_dot_product(a, b))
