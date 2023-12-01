#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2023/12/1 11:07

from fractions import Fraction
from sage.all import *


class Knapsack_Attacks:
    def __init__(self):
        return

    def calc_density(self, n, a_lis):
        t = math.log(max(a_lis, 2))
        density = Fraction(n / t)
        return density

    def __sv_check(self,B):
        for bij in B:
            print(len(bij))
        return

    def __matrix_overview(self, BB):
        for ii in range(BB.dimensions()[0]):
            a = ('%02d ' % ii)
            for jj in range(BB.dimensions()[1]):
                if BB[ii, jj] == 0:
                    a += ' '
                else:
                    a += 'X'
                if BB.dimensions()[0] < 60:
                    a += ' '
            print(a)

    def SV(self, n, a, M):
        '''

        :param n: the length of sequence
        :param a: the weight of encryption
        :return: relative short vector can be found
        '''
        B = Matrix(ZZ, n + 1, n + 1)
        for i in range(n):
            B[i, i] = 1
            B[i, n] = -a[i]
        B[n, n] = M
        self.__matrix_overview(B)
        B = B.LLL()
        self.__matrix_overview(B)

        return B

    def run(self):
        Knapsack_Attacks.SV(self, 3, 4, 65537)


if __name__ == "__main__":
    K = Knapsack_Attacks()
    K.run()
