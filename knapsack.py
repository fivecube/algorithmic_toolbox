# Uses python3
import sys
# import random

Value_dict = {}  # each pair will be optimal value of (knapsack_weight,items) = value

def optimal_weight_adv(W,w):
    for i in range(W+1):
        Value_dict[i,0] = 0
    for j in range(len(w)+1):
        Value_dict[0,j] = 0
    # print(Value_dict)
    for item_no in range(1,len(w)+1):
        for knapsack_weight in range(1,W+1):
            val = 0
            # print(knapsack_weight)
            Value_dict[knapsack_weight,item_no] = Value_dict[knapsack_weight,item_no-1]
            if w[item_no-1] <= knapsack_weight:
                val = Value_dict[knapsack_weight - w[item_no-1],item_no-1] + w[item_no-1]
                if Value_dict[knapsack_weight,item_no] < val:
                    Value_dict[knapsack_weight,item_no] = val
    return Value_dict[W,len(w)]
    # print(Value_dict)

Value_dict_memo = {}

def optimal_rec(W,index):
    if (W,index) in Value_dict_memo:
        return Value_dict_memo[W,index]
    Value_dict_memo[W,index] = 0
    # if index == len(w):
    #     return 0
    if index >= len(w):
        return 0
    Value_dict_memo[W,index] = optimal_rec(W,index+1)
    if w[index] <= W:
        val = optimal_rec(W-w[index],index+1) + w[index]
        if val > Value_dict_memo[W,index]:
            Value_dict_memo[W,index] = val
    return Value_dict_memo[W,index]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight_adv(W, w))

    u = W
    i = n
    back_track = []
    while(u != 0 and i > 0):
        if Value_dict[u,i] == Value_dict[u,i-1]:
            i-=1
        else:
            back_track.append(w[i-1])
            u-=w[i-1]
            i-=1
    print(back_track)

    # print(optimal_rec(W,0))
    # print(Value_dict_memo)
    # count = 0
    # while(True):
    #     Value_dict_memo = {}
    #     Value_dict = {}
    #     W = random.randint(1,10**4)
    #     n = random.randint(1,300)
    #     w = []
    #     for i in range(n):
    #         w.append(random.randint(0,10**5))
    #     if optimal_rec(W,0) != optimal_weight_adv(W,w):
    #         print("Wrong Answer at",W,w," memo table is",Value_dict_memo," and iter table is ",Value_dict)
    #         break
    #     if count%1000:
    #         print(count," testcases passed")
    #     count+=1
