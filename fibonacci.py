# Uses python3
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

n = int(input())
print(calc_fib(n))
