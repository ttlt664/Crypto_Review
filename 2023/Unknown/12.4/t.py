#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2023/12/3 12:16
from Crypto.Util.number import *
flag=b"SCUCTF{123456789123456123456789789}"
m=bytes_to_long(flag.ljust(100,b"\x00"))
for _ in range(3):
    p = getPrime(512)
    q = getPrime(512)
    e = 7
    print(f"c{_+1},n{_+1} = ",pow(m,e,p*q),",",p*q)
print(pow(m,e))
