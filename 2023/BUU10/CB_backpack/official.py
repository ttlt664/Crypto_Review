#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2023/12/13 14:16

from tqdm import tqdm
from copy import deepcopy
from random import randint
import time


def add(a, s):
    re = 0
    for i, j in zip(a, s):
        re += i * j
    return re


def Schroeppel_Shamir_balance(a, re, N4, M):
    SL1 = []
    SL1_ = {}
    SR1 = [0 for i in range(2 ^ N4)]
    SR1_ = {}
    SL2 = []
    SL2_ = {}
    SR2 = [0 for i in range(2 ^ N4)]
    SR2_ = {}

    for i in range(2 ^ N4):
        s = [int(j) for j in bin(i)[2:].rjust(N4, '0')]
        s1 = s + [0] * N4 * 3
        s2 = [0] * N4 + s + [0] * N4 * 2
        s3 = [0] * N4 * 2 + s + [0] * N4 * 3
        s4 = [0] * N4 * 3 + s
        if sum(s) != N4 // 2:
            continue
        SL1.append(add(s1, a) % M)
        SR1[i] = add(s2, a) % M
        SL2.append(add(s3, a) % M)
        SR2[i] = add(s4, a) % M
        # print(add(s4,a),a,s4)
        try:
            SL1_[add(s1, a) % M].append(s)
        except:
            SL1_[add(s1, a) % M] = [s]
        try:
            SL2_[add(s3, a) % M].append(s)
        except:
            SL2_[add(s3, a) % M] = [s]
        try:
            SR1_[add(s2, a) % M].append(s)
        except:
            SR1_[add(s2, a) % M] = [s]
        try:
            SR2_[add(s4, a) % M].append(s)
        except:
            SR2_[add(s4, a) % M] = [s]
    S1 = []
    S1_ = {}
    Sol = []
    for eM in range(M):
        for i in range(1, len(SL1)):
            eL1 = SL1[i] % M
            et = (eM - eL1) % M
            if et in SR1_.keys():
                for sr in SR1_[et]:
                    j = int(''.join([str(k) for k in sr]), 2)
                    S1.append((eL1 + SR1[j]) % M)
                    for sl1 in SL1_[SL1[i]]:
                        try:
                            S1_[(eL1 + SR1[j]) % M].append(sl1 + sr)
                        except:
                            S1_[(eL1 + SR1[j]) % M] = [sl1 + sr]
        for i in range(1, len(SL2)):
            eL2 = SL2[i] % M
            et = (re - eM - eL2) % M
            if et in SR2_.keys():
                for sr in SR2_[et]:
                    l = int(''.join([str(k) for k in sr]), 2)
                    t_ = (re - eL2 - SR2[l]) % M
                    if t_ in S1_.keys():
                        for sl2 in SL2_[SL2[i]]:
                            for s1 in S1_[t_]:
                                Sol.append(s1 + sl2 + sr)
    return Sol


a = [65651991706497, 247831871690373, 120247087605020, 236854536567393, 38795708921144, 256334857906663,
     120089773523233, 165349388120302, 123968326805899, 79638234559694, 259559389823590, 256776519514651,
     107733244474073, 216508566448440, 39327578905012, 118682486932022, 263357223061004, 132872609024098,
     44605761726563, 24908360451602, 237906955893793, 204469770496199, 7055254513808, 221802659519968, 169686619990988,
     23128789035141, 208847144870760, 272339624469135, 269511404473473, 112830627321371, 73203551744776, 42843503010671,
     118193938825623, 49625220390324, 230439888723036, 241486656550572, 107149406378865, 233503862264755,
     269502011971514, 181805192674559, 152612003195556, 184127512098087, 165959151027513, 188723045133473,
     241615906682300, 216101484550038, 81190147709444, 124498742419309]
re = 4051501228761632
n = len(a)
start_time = time.time()

M = 101
# M = 2

for i in tqdm(range(M // 2 + 1)):
    s1 = Schroeppel_Shamir_balance(a[:n // 2], i, n // 8, M)
    s2 = Schroeppel_Shamir_balance(a[n // 2:], re - i, n // 8, M)
    print(len(s1), len(s2))

    for result1 in s1:
        for result2 in s2:
            if add(a, result1 + result2) == re:
                print('answer:', result1 + result2)

end_time = time.time()
print(end_time - start_time)