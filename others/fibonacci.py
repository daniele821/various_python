# count sequences of length n, without any sequence long k of ones!
# basically the formula is:
# fibk(n) = { fibk(n-1) + ... + fibk(n-k)       if n >= k
#           { 2^k                               if 0 <= n < k


FIBONACCI3 = {}
FIBONACCI4 = {}


# binary sequences where there are no sequences of 1 of len 3
def fibonacci3(n):
    if n in FIBONACCI3:
        return FIBONACCI3[n]
    tmp = None
    match n:
        case 0: tmp = 1
        case 1: tmp = 2
        case 2: tmp = 4
        case _: tmp = fibonacci3(n-1)+fibonacci3(n-2)+fibonacci3(n-3)
    FIBONACCI3[n] = tmp
    return tmp


# binary sequences where there are no sequences of 1 of len 4
def fibonacci4(n):
    if n in FIBONACCI4:
        return FIBONACCI4[n]
    tmp = None
    match n:
        case 0: tmp = 1
        case 1: tmp = 2
        case 2: tmp = 4
        case 3: tmp = 8
        case _: tmp = fibonacci4(n-1)+fibonacci4(n-2)+fibonacci4(n-3)+fibonacci4(n-4)
    FIBONACCI4[n] = tmp
    return tmp


# binary sequences where there are no sequences of 1 of len k
def fib(n, k):
    sub = "1" * k
    count = 0
    for i in range(2**n):
        if str(bin(i)).find(sub) == -1:
            # print(str(bin(i)))
            count += 1
    return count


for i in range(100):
    print(i, end="\t")
    print(fibonacci4(i), end="\t")
    print(fib(i, 4), end="\n")
