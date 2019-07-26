# Uses python3
import sys
# import random
#
# def get_fibonacci_last_digit_naive(n):
#     if n <= 1:
#         return n
#
#     previous = 0
#     current  = 1
#
#     for _ in range(n - 1):
#         previous, current = current, previous + current
#
#     return current % 10

fib_last_digit_list = []
fib_last_digit_list.append(0)
fib_last_digit_list.append(1)

last_accessed_fib = 1

def get_fibonacci_last_digit_adv(n):
    global last_accessed_fib
    if n<=last_accessed_fib:
        return fib_last_digit_list[n]
    else:
        for i in range(last_accessed_fib+1,n+1):
            fib_last_digit_list.append((fib_last_digit_list[i-1]+fib_last_digit_list[i-2])%10)
        last_accessed_fib = n
        return fib_last_digit_list[n]



if __name__ == '__main__':
    input = sys.stdin.read()
    # input = input()
    n = int(input)
    print(get_fibonacci_last_digit_adv(n))
