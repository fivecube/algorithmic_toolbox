# Uses python3
import sys

def get_majority_element(a,n):
    if n == 1:
        return 1
    a = sorted(a)
    for i in range(n//2):
        majority = n//2+i
        if a[i] == a[majority]:
            return 1
    if n%2!=0:
        if a[n//2] == a[n-1]:
            return 1

    return -1

# def get_majority_element_naive(a,n):
#     for i in range(0,n):
#         currentElement = a[i]
#         count = 0
#         for j in range(i,n):
#             count+=1
#         if count > n//2:
#             return a[i]
#     return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a,n) != -1:
        print(1)
    else:
        print(0)
