##################################################
## module: py2_poly_lambda_dances.py
## author: Misty Jenkins
## A#: A01489174
## //What it does//
## 09/22/2016
##################################################
import random
from datetime import datetime

def gen_rand_coeff(a, b):
    sign = random.randint(1, 1000)
    if sign < 500:
        return -random.randint(a, b)
    else:
        return random.randint(a, b)


def make_2nd_deg_poly(k2, k1, k0):
    return lambda x: (
        "p(x) = {!s}x^2 + {!s}x + {!s}".format(k2, k1, k0),
        k2 * x ** 2 + k1 * x + k0,
        "at x = " + str(x)
    )


def make_2nd_deg_polys(coeffs):
    return [make_2nd_deg_poly(i[0], i[1], i[2]) for i in coeffs]


# takes a list of anonymous 2nd degree polynomials and a sequence of
# numbers and applies each polynomial to each number in the sequence
def map_polys(polys, numbers):
    return [f(n) for n in numbers for f in polys]


def display_poly_maps(poly_maps):
    for m in poly_maps:
        print('%s = %s, %s' % (m[0], str(m[1]), m[2]))


def poly_dance(coeffs, xvals):
    polys = make_2nd_deg_polys(coeffs)
    poly_maps = map_polys(polys, xvals)
    return poly_maps


def make_nth_deg_rand_poly(n, a, b):
    if(a<=0 or n<0):
        return
    if(a>b):
        return
    coeffs = [gen_rand_coeff(a, b) for i in range(0,n)]
    polyStr = "p(x) = "
    equationStr = ""
    for i in reversed(range(1, n)):
        polyStr += "{!s}x^{!s} + ".format(coeffs[i], i)
        equationStr += "{!s}*x**{!s} + ".format(coeffs[i], i)
    polyStr += str(coeffs[0])
    equationStr += str(coeffs[0])

    return lambda x: (
        polyStr,
        eval(equationStr),
        "at x = " + str(x)
    )


def make_nth_deg_rand_polys(num_polys, n, a, b):
    return [make_nth_deg_rand_poly(n,a,b) for i in range(0,num_polys)]


def rand_poly_dance(num_polys, n, a, b, xvals):
    polys = make_nth_deg_rand_polys(num_polys, n, a, b)
    poly_maps = map_polys(polys, xvals)
    return poly_maps


def sorted_rand_poly_dance(num_polys, n, a, b, xval):
    polys = make_nth_deg_rand_polys(num_polys, n, a, b)
    computedPolys = [poly(xval) for poly in polys]
    return sorted(computedPolys, key=lambda tup: tup[1], reverse=True)


########## test code ##########
start = datetime.now()
top_10 = sorted_rand_poly_dance(10000, 5, 1, 10, 2)[:10]
end = datetime.now()
print ('start = ', start)
print ('end = ', end)
print ('duration = ', end - start)
display_poly_maps(top_10)