import combinatorics as cmb
from fractions import Fraction


def lambda_density_binomial(n, p):
    return lambda k: cmb.binomial_coefficient(n, k) * (p**k) * ((1-p)**(n-k))


def lambda_density_ipergeometric(n, b, r):
    return lambda k: Fraction(cmb.binomial_coefficient(b, k) * cmb.binomial_coefficient(r, n - k)) / Fraction(cmb.binomial_coefficient(r + b, n))


def density_binomial(n, p, k):
    return lambda_density_binomial(n, p)(k)


def density_ipergeometric(n, b, r, k):
    return lambda_density_ipergeometric(n, b, r)(k)


print(density_binomial(100, Fraction('0.85'), 85).__float__())
print(density_ipergeometric(3, 4, 3, 1))
