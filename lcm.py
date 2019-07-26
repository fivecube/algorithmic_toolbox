# Uses python3
import sys

# def lcm_naive(a, b):
#     for l in range(1, a*b + 1):
#         if l % a == 0 and l % b == 0:
#             return l
#
#     return a*b


def lcm_adv(a,b):
    if a==0 or b==0:
        return 0
    else:
        for l in range(max(a,b),a*b+1,max(a,b)):
            if l % a == 0 and l % b == 0:
                return l

if __name__ == '__main__':
    input = sys.stdin.read()
    # input = input()
    a, b = map(int, input.split())
    print(lcm_adv(a, b))
