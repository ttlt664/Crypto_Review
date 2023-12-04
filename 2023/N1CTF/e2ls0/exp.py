#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2023/11/27 11:38

from sage.all import *
from sage.matrix.matrix2 import Matrix as Matrix2

def resultant(f1, f2, var):
    return Matrix2.determinant(f1.sylvester_matrix(f2, var))

p = 31056954144466551354887631023962695320706316712255640373035795693815085684947
leak = 29044030291754400812460259687647677793710240498564440662990181268131640570302
# PR = PolynomialRing(GF(p), names=['X', 'Y', 'j1', 'j2', 'j3', 'j4', 'j6'])
# X, Y, j1, j2, j3, j4, j6 = PR.gens()
# phi = 1855425871872000000000 * (X + Y) - 770845966336000000 * X * Y + 452984832000000 * (X ** 2+Y**2) + 8900222976000 *( X ** 2 * Y+ Y**2*X) + 2587918086 * X ** 2 * Y ** 2*2 + 36864000 * (X ** 3+Y**3) - 1069956 * (X ** 3 * Y +X*Y**3)+ 2232 * (X ** 3 * Y ** 2+X**2*Y**3) - X ** 3 * Y ** 3*2 + X ** 4+Y**4
# t = var('t')
# F = GF(p ** 2, modulus=t ** 2 + 1, name='i')
# i = F.gen()
# poly = phi.subs(X=j1, Y=j3 + j4 * i)
#
# f1 = (poly.map_coefficients(lambda c: c.polynomial()[0]))
# f2 = (poly.map_coefficients(lambda c: c.polynomial()[1]))
#
# pl = PR((j3 + j4 * i) * (leak + j6 * i) - 1)
# f3 = pl.map_coefficients(lambda c: c.polynomial()[0])  # 实数部分的参数
# f4 = pl.map_coefficients(lambda c: c.polynomial()[1])  # 虚数部分的参数
#
# h1 = resultant(f1,f2,j1)
# # print(h1)
# h2 = resultant(f3,f4,j6)
# # print(h2)
# h3 = resultant(h1,h2,j3)
# # print(h3)
# roots3 = h3.univariate_polynomial().roots()
# # print(roots3)
# h4 = resultant(h1,h2,j4)
# roots4 = h4.univariate_polynomial().roots()
# # print(roots4)
# #
# # j3_list = [(16706373907252631717349263775854279382622910030873210439383810388500800002128*i, 1), (14350580237213919637538367248108415938083406681382429933651985305314285682819*i, 1), (0, 8)]
# # j4_list = [(20355407949250159998926206432124782400376292812951871375034432732824997645919, 2), (0, 4), (29264949559255044208848952758968038559951535718518059230907121871763494487985, 4)]
# #
# # res_list = []
# # for j3t in j3_list:
# #     for j4t in j4_list:
# #         f1 = poly.map_coefficients(lambda c: c.polynomial()[0])  # 实数部分的参数
# #         p = f1.subs(j3 = j3t[0],j4 = j4t[0])
# #         p = p.univariate_polynomial().roots()
# #         res_list += p
# #         print(p)
# # print(res_list)
# # res_list = [(7047854988620514207127367513945528319234396290697294400267995423583195014756, 1),(0, 1), (31056954144466551354887631023962695320706316712255640373035795693815073396947, 3)]
# #
# # for j_ in res_list:
# #     j_ = j_[0]
# #     d = j_.bit_length()
# #     B = Matrix(ZZ,3,4)
# #     zeta = len(str(2 ** 80))
# #
# #     B[0,0] = 10**d
# #     B[0,2] = 10**(2*d)
# #     B[1,1] = 10**d
# #     B[1,2] = -2*j_*(10**d)
# #     B[2,2] = 10**(d+zeta)
# #     B[2,-1] = -j_**2
# #     print(B.LLL())
# #     break

import ast

# https://math.mit.edu/~drew/ClassicalModPolys.html
mp3_def_str = """[1,0] 1855425871872000000000
[1,1] -770845966336000000
[2,0] 452984832000000
[2,1] 8900222976000
[2,2] 2587918086
[3,0] 36864000
[3,1] -1069956
[3,2] 2232
[3,3] -1
[4,0] 1"""
mp3_def = [
    [ast.literal_eval(x) for x in line.split(" ")] for line in mp3_def_str.split("\n")
]
mp_term = (
    lambda e, coef: lambda x, y: coef * x ** e[0] * y ** e[1]
    + coef * x ** e[1] * y ** e[0]
    if e[0] != e[1]
    else coef * x ** e[0] * y ** e[1]
)
mp = lambda mp_def: lambda x, y: sum([mp_term(*term)(x, y) for term in mp_def])
mp3 = mp(mp3_def)
x = var("x")
Fp = GF(p)
Fp2 = GF(p ** 2, "i", modulus=x**2 + 1)
i = Fp2.gen()
aa, cc, dd, ff = Fp2["aa,cc,dd,ff"].gens()
PR_Fp = Fp["aa,cc,dd,ff"]
f = mp3(aa + 0 * i, cc + dd * i)
f_real = PR_Fp(f.map_coefficients(lambda c: c.polynomial()[0]))
f_imag = PR_Fp(f.map_coefficients(lambda c: c.polynomial()[1]))
g = (cc + dd * i) * (leak + ff * i) - 1
g_real = PR_Fp(g.map_coefficients(lambda c: c.polynomial()[0]))
g_imag = PR_Fp(g.map_coefficients(lambda c: c.polynomial()[1]))
aa, cc, dd, ff = PR_Fp.gens()
f1 = f_real.sylvester_matrix(f_imag, dd).det()  # function of a, c
f2 = f_real.sylvester_matrix(g_real, dd).det()  # function of a, c, f
f3 = g_real.sylvester_matrix(g_imag, dd).det()  # function of c, f
f4 = f2.sylvester_matrix(f3, ff).det()  # function of a, c
g = f1.sylvester_matrix(f4, cc).det().univariate_polynomial()  # function of a
for r, _ in g.roots():
    print(r, ZZ(r).bit_length())
    if r > 0 and ZZ(r).bit_length() < 200:
        target_j = ZZ(r)
print("j", target_j)
