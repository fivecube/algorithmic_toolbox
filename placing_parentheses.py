# Uses python3
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

m = dict()
M = dict()
op = dict()

def MinAndMax(i,j):
    mini = float("+inf")
    maxi = float("-inf")
    for k in range(i,j):
        # print(i,k,"and ",k+1,j)
        # print("op is ",op[k])
        a = evalt(M[i,k],M[k+1,j],op[k])
        b = evalt(M[i,k],m[k+1,j],op[k])
        c = evalt(m[i,k],M[k+1,j],op[k])
        d = evalt(m[i,k],m[k+1,j],op[k])
        # print("here ",a,b,c,d)
        mini = min(mini,a,b,c,d)
        maxi = max(maxi,a,b,c,d)
    return (mini,maxi)


def get_maximum_value(dataset):
    n = len(dataset)
    global m
    global M
    count = 1
    count_2 = 1
    for i in range(1,n+1):
        if i%2:
            m[count,count] = int(dataset[i-1])
            M[count,count] = int(dataset[i-1])
            count+=1
        else:
            op[count_2] = dataset[i-1]
            count_2+=1
    d = n-(n//2)
    for s in range(1,d):
        for i in range(1,d-s+1):
            j = i+s
            m[i,j],M[i,j] = MinAndMax(i,j)
    # print(M,m)
    return M[1,d]


if __name__ == "__main__":
    print(get_maximum_value(input()))
