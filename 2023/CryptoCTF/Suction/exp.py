#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2023/12/5 15:35
import requests
from Crypto.Util.number import *
PKEY = 76717969558587152375798562887929961077291822499987128569546270763178084194729
enc = 189862862542101122892824733782145266259795828082217623925853585549680290362
e_ = int(bin(PKEY)[-8:],2)
print(e_)
print(e_.bit_length())
n_ = int(bin(PKEY)[2:-8],2)
from sage.all import *
import time
import random
def factorize_large_number(number):
    url = f"http://factordb.com/api?query={number}"

    try:
        time.sleep(random.randint(0,3))
        response = requests.get(url)
        data = response.json()
        # print(data)
        # print(data['status'])

        if data['status'] == 'FF':
            factors = data['factors']
            return factors
        else:
            return f"Factorization not found for {number}"
    except Exception as e:
        return f"Error: {str(e)}"


for i in range(2**8):
    nr = (n_<< 8) + i
    # print(n_ << 8 + i)
    # print(nr)
    if isPrime(nr) == False:
        if len(factorize_large_number(nr)) == 2:
            print(factorize_large_number(nr))

p = 247206233189438647228272524110963931669
q = 310339948021443182792741136446099304149
# import gmpy2
# phi = (p-1)*(q-1)
# for e_ in range(65537):
#     try:
#         d=gmpy2.invert(e_,phi)
#         print(d)
#         n1 = p *q
#         m = gmpy2.powmod(enc,d,n1)
#         print(long_to_bytes(m))
#     except:
#         pass