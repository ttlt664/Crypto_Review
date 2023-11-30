#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2023/10/21 11:54
from Crypto.Util.number import *
from random import randint
import libnum
from Crypto.Util.number import *
from sage.all import *
p=getPrime(512)
import  gmpy2
def Legendre(n,p): # 这里用勒让德符号来表示判断二次（非）剩余的过程
    return pow(n,(p - 1) // 2,p)
p=10526848180930195785337788235924463766051753152735125220253464630026770909868392509854901429992537760504253926452393857377530900908769927464829973373111343
def guess_p(p):
    e = 65537
    P = p
    n1 = getPrime(512)*getPrime(512)
    with open('enc2.txt', 'w+') as f:
        while libnum.jacobi(2,n1) == 1:
            n1 = getPrime(512)*getPrime(512)
        while P:
            pad = randint(0, 2**2023)**2
            message = pad << 1 + P % 2
            # print()
            # print("-------------------")
            cipher = pow(message, e, n1)
            print(P%2,jacobi_symbol(cipher,n1))
            f.write(str(cipher)+'n')
            P //= 2
    print("n1 = "+ str(n1) )
guess_p(p)