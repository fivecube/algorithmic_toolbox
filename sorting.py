# Uses python3
import sys
import random

def partition3(a, l, r):
    x = a[l]
    j = l
    e = l
    for i in range(l+1,r+1):
        if a[i]<x:
            j+=1
            e+=1
            if i==e:
                a[i],a[j] = a[j],a[i]
            else:
                a[j],a[e] = a[e],a[j]
                a[i],a[j] = a[j],a[i]
        elif a[i] == x:
            e = e+1
            a[i],a[e] = a[e],a[i]
    a[l],a[j] = a[j],a[l]
    return j,e



def partition2(a, l, r):
    x = a[l]
    j = l;
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    # m = partition2(a, l, r)
    # randomized_quick_sort(a, l, m - 1);
    # randomized_quick_sort(a, m + 1, r);

    m1,m2 = partition3(a, l, r)
    # print(m1,m2)
    randomized_quick_sort(a, l, m1 - 1);
    randomized_quick_sort(a, m2 + 1, r);



if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')

    # count = 0
    # while True:
    #     count+=1
    #     n = random.randint(1,10**3)
    #     a = []
    #     for i in range(n):
    #         a.append(random.randint(1,10**3))
    #     # print("##########################")
    #     # print(a)
    #     a_eta = sorted(a)
    #     randomized_quick_sort(a,0,n-1)
    #     if a_eta != a:
    #         print("Wrong Answer at a = ",a)
    #         print("and the right a_eta = ",a_eta)
    #         break
    #     if not count%1000:
    #         print(count," testcases has passed")
