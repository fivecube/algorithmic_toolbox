# Uses python3
import sys
# import random
# def fibonacci_partial_sum_naive(from_, to):
#     sum = 0
#
#     current = 0
#     next  = 1
#
#     for i in range(to + 1):
#         if i >= from_:
#             sum += current
#
#         current, next = next, current + next
#
#     return sum % 10

list_fib = []
list_fib.append(0)
list_fib.append(1)
last_fib_accessed = 1
def calc_fib(n):
	global last_fib_accessed
	if n<=last_fib_accessed:
		return list_fib[n]
	else:
		for i in range(last_fib_accessed+1,n+1):
			list_fib.append(list_fib[i-1]+list_fib[i-2])
		else:
			last_fib_accessed = n
			return list_fib[n]


def get_fibonacci_huge_adv(n,m):
    if n<=1:
        return n
    else:
        i=2
        over = 1
        fib_mod_list =[]
        fib_mod_list.append(0)
        fib_mod_list.append(1)
        while(over):
            fib_mod_list.append((calc_fib(i))%m)
            # print(calc_fib(i))
            previous = fib_mod_list[i-1]
            present = fib_mod_list[i]
            # print(str(previous)+str(present))
            if str(previous)+str(present) == "01":
                # print(fib_mod_list)
                over = 0
            i+=1
        zeta_index = n%(len(fib_mod_list)-2)
        zeta = fib_mod_list[zeta_index]
        return(zeta)


def fibonacci_partial_sum_adv(n,m):
    # print(get_fibonacci_huge_adv(n+2,10))
    res1 = (get_fibonacci_huge_adv(m+2,10)-1)
    if res1==-1:
        res1 = 9
    # print(res1)
    res2 = (get_fibonacci_huge_adv(n+1,10)-1)
    if res2 == -1:
        res2 = 9
    # print(res2)

    if res1>res2:
        return(res1-res2)
    else:
        return((10+res1-res2)%10)


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_adv(from_, to))
    # i=0
    # while(1):
    #     n = random.randint(0,1000)
    #     m = random.randint(n,10000)
    #     # m = 7
    #     # n = 3
    #     result1 = fibonacci_partial_sum_naive(n,m)
    #     result2 = fibonacci_partial_sum_adv(n,m)
    #
    #     if result1 != result2:
    #         print("Wrong result for n =",n,"  res1 is",result1,"and res2 is",result2)
    #         break
    #     if i%1000 == 0:
    #         print(i," testcases passed")
    #     i+=1
