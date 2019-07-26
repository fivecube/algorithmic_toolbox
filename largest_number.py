#Uses python3

import sys

def IsGreaterOrEqual(n,m):
    if int(n+m)>=int(m+n):
        return True
    else:
        return False


def largest_number(a):
    res = ""
    while(len(a)):
        max_digit = "0"
        for x in a:
            if IsGreaterOrEqual(x,max_digit):
                max_digit = x
        a.remove(max_digit)
        res = res+max_digit
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
