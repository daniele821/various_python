import sys

args = sys.argv[1:]
try:
    n = args[0]
    k = args[1]
except Exception:
    n = 10
    k = 10


def disposition(n, k):
    res = 1
    for i in range(n-k+1, n+1):
        res *= i
    return res


def factorial(n):
    return disposition(n, n-1)


def binomial_coefficient(n, k):
    return disposition(n, k) // factorial(k)