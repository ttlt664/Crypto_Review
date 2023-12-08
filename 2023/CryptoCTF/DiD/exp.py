#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2023/12/6 10:43

from pwn import *
from sage.all import *
r = remote("127.0.0.1", 1337)
PR = PolynomialRing(Zmod(127),name='x')
x = PR.gen()
def solve(c):
    # 怎么在素数域上开二次根
    f = x**2 - 1 - c
    res = f.roots()
    if len(res) == 0:
        f = x**2 - c
        res = f.roots()
    print(res)
    return res

def extract_did():
    did = str(r.recvline()).replace("'", "").replace("\\", "").replace("b[", "").replace("]n", "").replace("b+ DID = [","")
    did  = did.split(",")
    di = []
    for d in did:
        di.append(int(d))
    return di
def send_A(A_lis):
    s = (str(A_lis)[1:-1]).encode()
    r.sendline(s)


r.recvuntil(b"Are you ready? ::.  ")
A = [32, 116, 7, 76, 17, 8, 37, 85, 15, 63, 71, 117, 6, 35, 74, 2, 75, 114, 110, 116]
send_A(A)
r.recvline()
r.recvline()
ret = extract_did()
print(ret)
send_A(A)
r.recvline()
ret = extract_did()
print(ret)
for k in ret:
    print(solve(k))
    print("this list has finished----------------")

send_A(A)
r.recvline()
ret = extract_did()
print(ret)
send_A(A)
r.recvline()
ret = extract_did()
print("------------------")
print(ret)