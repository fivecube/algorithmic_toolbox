# python3
import sys
# import random

def compute_min_refills(distance, tank, stops):
    stops = [0]+stops+[distance]
    min_refills = 0
    prvs_refill=0
    current_refill=0
    fuel = tank
    # print("fuel is ",tank)
    while(stops[current_refill]<distance):
        while(stops[current_refill] < distance and fuel>=stops[current_refill+1]-stops[prvs_refill]):
            current_refill+=1
        if current_refill == prvs_refill:
            return -1
        if stops[current_refill] != distance:
            # print("refill at",stops[current_refill])
            min_refills+=1
            fuel = tank
        prvs_refill = current_refill
    return min_refills

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())

    # d = int(input())
    # m = int(input())
    # n = int(input())
    # stops =list(map(int,input().split(' ')))

    # while(True):
    #     d = random.randint(1,10**5)
    #     m = random.randint(1,400)
    #     n = random.randint(1,300)
    #     stops = []
    #     for i in range(n):
    #         stops.append(random.randint(0,m))
    #     print(compute_min_refills(d, m, stops))
    print(compute_min_refills(d, m, stops))
