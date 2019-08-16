# Uses python3
import sys

min_change = [0]*1000


def get_change(money):
    change = [1,3,4]
    for m in range(1,money+1):
        min_change[m] = float("inf")
        for ch in change:
            if ch <= m:
                temp_min = min_change[m-ch] + 1
                if temp_min < min_change[m]:
                    min_change[m] = temp_min
    return min_change[money]

if __name__ == '__main__':
    # m = int(sys.stdin.read())
    money = int(input())
    print(get_change(money))
