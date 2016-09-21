##################################################
## module: py2_poly_lambda_dances.py
## author: Misty Jenkins
## A#: A01489174
## //What it does//
## 09/22/2016
##################################################

import sys
from sets import Set


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


########## test code ##########
# p1 = make_2nd_deg_poly(4, 5, 6)
# rslt = p1(3)
# print('%s = %s, %s' % (rslt[0], str(rslt[1]), rslt[2]))

# polys = make_2nd_deg_polys([(1, 2, 3), (4, 5, 6)])
# print polys[0](1)
# print polys[1](3)
# print polys[1](2)

# poly_maps = map_polys(polys, xrange(1, 6))
# display_poly_maps(poly_maps)

display_poly_maps(poly_dance(((1, 2, 3), (4, 5, 6)), xrange(1, 10)))