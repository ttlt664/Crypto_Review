#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2023/12/11 18:17

from Crypto.Util.number import *
P = (71451574057642615329217496196104648829170714086074852, 69505051165402823276701818777271117086632959198597714)
Q1 = (40867727924496334272422180051448163594354522440089644, 56052452825146620306694006054673427761687498088402245)

def on_barak(P, E):
	c, d, p = E
	x, y = P
	return (x**3 + y**3 + c - d*x*y) % p == 0

def add_barak(P, Q, E):
	if P == (0, 0):
		return Q
	if Q == (0, 0):
		return P
	assert on_barak(P, E) and on_barak(Q, E)
	x1, y1 = P
	x2, y2 = Q
	if P == Q:
		x3 = y1 * (c - x1**3) * inverse(x1**3 - y1**3, p) % p
		y3 = x1 * (y1**3 - c) * inverse(x1**3 - y1**3, p) % p
	else:

		x3 = (y1**2*x2 - y2**2*x1) * inverse(x2*y2 - x1*y1, p) % p
		y3 = (x1**2*y2 - x2**2*y1) * inverse(x2*y2 - x1*y1, p) % p
	return (x3, y3)

def mul_barak(m, P, E):
	if P == (0, 0):
		return P
	R = (0, 0)
	while m != 0:
		if m & 1:
			R = add_barak(R, P, E)
		m = m >> 1
		if m != 0:
			P = add_barak(P, P, E)
	return R
p = 73997272456239171124655017039956026551127725934222347
d = 68212800478915688445169020404812347140341674954375635
c = 1
from sage.all import *

R = PolynomialRing(Zmod(p), names=['a', 'b', 'c'])
a, b, c = R.gens()
f = a ** 3 + b ** 3 + c**3 - d * a * b * c
rational_point = (-1, 0, 1)

E = EllipticCurve_from_cubic(f, P=rational_point,morphism=False)
Finv = EllipticCurve_from_cubic(f,P=rational_point)
F_inv = Finv.inverse()
a1= E.a_invariants()
print(a1)
F = EllipticCurve(a1)
Q1 = F_inv(Q1)
P = F_inv(P)
# m = discrete_log(Q1,P)
# print(m)