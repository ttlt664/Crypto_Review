# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# # @Time    : 2023/12/2 23:19
from sympy import totient
t = [1997493529, 846961, 47681, 46351, 2909, 1367, 431, 109, 61, 61, 19, 19, 11, 11, 11, 7, 7, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2]
# n =1
# for i in range(9):
    # n *=t[i]*3+1
# print(n)
from Crypto.Util.number import *
from gmpy2 import *
n1=93994292740350224890159196163597206752080667049472
from sage.all import *
for i in range(9999):
    n1 = next_prime(n1-i)
    print(totient(n1), n1)

    # if totient(n1) > 93994292740350224890159196163597206752080667049472:

# t = 93994292740350224890159196163597206752080667049489
# for i in range(99999):
#     print(totient(t-i))

