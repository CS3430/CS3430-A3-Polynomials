##################################################
## module: py2_poly_lambda_dances.py
## author: Misty Jenkins
## A#: A01489174
## //What it does//
## 09/22/2016
##################################################

import sys

def make_adder(n): return lambda x: x + n


def test_adders():
    add3 = make_adder(3)
    add4 = make_adder(4)
    print 'Testing adders...'
    for x in xrange(1, 6):
        sys.stdout.write('add3(' + str(x) + ')=' + str(add3(x)) + "\n")
        sys.stdout.write('add4(' + str(x) + ')=' + str(add4(x)) + "\n")


def make_2nd_deg_poly(k2, k1, k0):
    return lambda x: k2 * x ** 2 + k1 * x + k0