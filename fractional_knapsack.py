# Uses python3
import sys
# import random
def get_optimal_value(capacity, weights, values):
    value = 0.
    w_by_v = []
    for i,j in zip(values,weights):
        if i == 0:
            w_by_v.append(float("inf"))
        else:
            w_by_v.append(j/i)
    w_by_v_eta = []
    values_eta = []
    weights_eta = []
    for i,j,k in sorted(zip(w_by_v,values,weights)):
        w_by_v_eta.append(i)
        values_eta.append(j)
        weights_eta.append(k)
    for i in range(len(weights_eta)):
        if capacity==0:
            break
        if w_by_v_eta[i] == 0:
            pass
        else:
            pick = min(weights_eta[i],capacity)
            weights_eta[i]-=pick

            value+=pick*(1/w_by_v_eta[i])
            capacity-=pick
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    # n_capacity = input().split(' ')
    # n = int(n_capacity[0])
    # capacity = int(n_capacity[1])
    # values = []
    # weights = []
    # for i in range(n):
    #     v_w = input().split(' ')
    #     values.append(int(v_w[0]))
    #     weights.append(int(v_w[1]))

    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.4f}".format(opt_value))
    # while(True):
    #     n = random.randint(1,10**3)
    #     capacity = random.randint(0,2*(10**6))
    #     values = []
    #     weights = []
    #     for i in range(n):
    #         values.append(random.randint(0,2*(10**6)))
    #         weights.append(random.randint(0,2*(10**6)))
    #     print("here")
    #     opt_value = get_optimal_value(capacity, weights, values)
    #     print("{:.4f}".format(opt_value))
