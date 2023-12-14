#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2023/12/6 14:31
import itertools
from fractions import Fraction

import gmpy2
from z3 import Ints, solve
from Crypto.Util.number import *
O = [1391526622949983, 2848691279889518, 89200900157319, 31337]
C = [5960650533801939766973431801711817334521794480800845853788489396583576739362531091881299990317357532712965991685855356736023156123272639095501827949743772, 6521307334196962312588683933194431457121496634106944587943458360009084052009954473233805656430247044180398241991916007097053259167347016989949709567530079, 1974144590530162761749719653512492399674271448426179161347522113979158665904709425021321314572814344781742306475435350045259668002944094011342611452228289, 2613994669316609213059728351496129310385706729636898358367479603483933513667486946164472738443484347294444234222189837370548518512002145671578950835894451, 8127380985210701021743355783483366664759506587061015828343032669060653534242331741280215982865084745259496501567264419306697788067646135512747952351628613, 5610271406291656026350079703507496574797593266125358942992954619413518379131260031910808827754539354830563482514244310277292686031300804846114623378588204, 10543, 4]

ctext = 80607532565510116966388633842290576008441185412513199071132245517888982730482694498575603226192340250444218146275844981580541820190393565327655055810841864715587561905777565790204415381897361016717820490400344469662479972681922265843907711283466105388820804099348169127917445858990935539611525002789966360469324052731259957798534960845391898385316664884009395500706952606508518095360995300436595374193777531503846662413864377535617876584843281151030183895735511854
# print(len(C))
# 一共5个未知数
# e, d = Ints('e d')
# solve(C[6] * e - C[7] * d == O[3], e > 0, d > 0)
# [d = 73, e = 3]
def convert_to_integers(rational_numbers):
    # 找到所有分母的最小公倍数
    denominator_lcm = 1
    for number in rational_numbers:
        denominator_lcm = denominator_lcm * number.denominator() // math.gcd(denominator_lcm, number.denominator())
    integer_numbers = [int(number.numerator() * (denominator_lcm // number.denominator())) for number in rational_numbers]
    return integer_numbers

from sage.all import *

R = PolynomialRing(QQ, names=['a', 'b', 'c'])
a, b, c = R.gens()
f = a ** 3 + b ** 3 + c ** 3 - 73 * a * b * c
rational_point = [1,-1,0]
E = EllipticCurve_from_cubic(f,P=rational_point)
# 找一个曲线上的有理点
f = EllipticCurve_from_cubic(f,P= rational_point,morphism=False)
f_inv = E.inverse()
P = (f.gens()[0])
print(P)
L = [[C[0], -C[1], 0],[0, C[2], -C[3]], [-C[5], 0, C[4]]]
L = Matrix(ZZ, 3, 3,L)
# print(L)
for i in range(10):
    x,y,z = f_inv(i*P)
    ty=convert_to_integers([x,y,z])
    # print(ty)
    for vp in itertools.permutations(ty):
        print(vp)
        A = vector(ZZ,vp)
        # print(A)
        res = L.solve_right(A)
        p,q,r = res
        if p%1==0 and q%1==0 and r%1==0:
            ntext = int(p)*int(q)*int(r)*3*73
            phi = (int(p) - 1) * (int(q) - 1) * (int(r) - 1) * 2 * 72
            d=inverse_mod(65537,phi)
            m = gmpy2.powmod(ctext,d,ntext)
            if m >0:
                print(long_to_bytes(m))
        # print(res)
