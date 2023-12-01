#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2023/11/27 11:38

from sage.all import *
from sage.matrix.matrix2 import Matrix as Matrix2


def resultant(f1, f2, var):
    return Matrix2.determinant(f1.sylvester_matrix(f2, var))


p = 31056954144466551354887631023962695320706316712255640373035795693815085684947
leak = 29044030291754400812460259687647677793710240498564440662990181268131640570302
PR = PolynomialRing(GF(p), names=['X', 'Y', 'j1', 'j2', 'j3', 'j4', 'j6'])
X, Y, j1, j2, j3, j4, j6 = PR.gens()
phi = 1855425871872000000000 * (X + Y) - 770845966336000000 * X * Y + 452984832000000 * (X ** 2+Y**2) + 8900222976000 *( X ** 2 * Y+ Y**2*X) + 2587918086 * X ** 2 * Y ** 2*2 + 36864000 * (X ** 3+Y**3) - 1069956 * (X ** 3 * Y +X*Y**3)+ 2232 * (X ** 3 * Y ** 2+X**2*Y**3) - X ** 3 * Y ** 3*2 + X ** 4+Y**4
Pt = PolynomialRing(GF(p), name='t')
t = Pt.gen()
F = GF(p ** 2, modulus=t ** 2 + 1, name='i')
i = F.gen()
poly = phi.subs(X=j1, Y=j3 + j4 * i)

f1 = poly.map_coefficients(lambda c: c.polynomial()[0])  # 实数部分的参数
f2 = poly.map_coefficients(lambda c: c.polynomial()[1])  # 虚数部分的参数

# -1次方 互为倒数
# f3 = (j3 + j4 * i) * (leak + j6 * i) - 1
# print(f3)

f3 = j3 * (j3 ** 2 + j4 ** 2) - leak
f4 = j4 * (j3 ** 2 + j4 ** 2) + j6 ** 2

h1=resultant(f1,f2,j1) #3,4
h2 = resultant(f4, h1,j3) #
h3 = resultant(,h2,j4)

# h3=resultant(h1,h2,j3)
# roots = h3.univariate_polynomial().roots()
# print(roots)