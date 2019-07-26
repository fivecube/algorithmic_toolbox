# Uses python3
import sys
# import random
#
# def get_fibonacci_huge_naive(n, m):
#     if n <= 1:
#         return n
#
#     previous = 0
#     current  = 1
#
#     for _ in range(n - 1):
#         previous, current = current, previous + current
#
#     return current % m

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

if __name__ == '__main__':
    # input = sys.stdin.read();
    input = input()
    n, m = map(int, input.split())
    print(get_fibonacci_huge_adv(n, m))
    # i=0
    # while(1):
    #     i+=1
    #     n = random.randint(1,10)
    #     m = random.randint(2,5)
    #
    #     res1 = get_fibonacci_huge_naive(n,m)
    #     res2 = get_fibonacci_huge_adv(n,m)
    #
    #     if res1 != res2:
    #         print("Wrong result for n =",n,"and m =",m)
    #         break
    #     if i%1000 == 0:
    #         print(i," testcases passed")
