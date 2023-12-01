#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2023/12/1 11:07

from sage.all import *


class Knapsack_Attacks:
    def __init__(self,a,M):
        '''
        :param a: the weight
        :param M: ciphertext
        '''
        self.a = a
        self.M = M

    def calc_density(self):
        n = len(self.a)
        t = math.log(max(self.a),2)
        density = float(n / t)
        print("===================================================")
        print(f"density of the knapsack is {density}")
        return density


    def __sv_check(self,B):
        for bij in B:
            bij = list(bij)
            for i in range(len(bij)):
                if bij[i]!=0:
                    bij[i] = 1
            # print(bij)
            s = sum(x * y for x, y in zip(self.a, bij))
            if s == self.M:
                return bij,True
        # no right answer in B
        return "No answer ",False



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

    def SV_Lattice(self, a, M):
        '''

        :param a: the weight of encryption
        :param M: the ciphertext
        :return: relative short vector can be found
        '''
        n = len(a)
        B = Matrix(ZZ, n + 1, n + 1)
        for i in range(n):
            B[i, i] = 1
            B[i, n] = -a[i]
        B[n, n] = M
        # self.__matrix_overview(B)
        B = B.LLL()
        # self.__matrix_overview(B)
        return B

    def sv_attack(self):
        global a_solve
        B = self.SV_Lattice(self.a,self.M)
        if self.__sv_check(B)[1]==False:
            K = Knapsack_Attacks(self.a,sum(a)-self.M)
            K.sv_attack()
        else:
            a_solve = self.__sv_check(B)[0]
        return a_solve

    # def run(self):
    #     Knapsack_Attacks.sv_attack(self)
    #     Knapsack_Attacks.calc_density(self)

if __name__ == "__main__":
    a = [65651991706497, 247831871690373, 120247087605020, 236854536567393, 38795708921144, 256334857906663, 120089773523233, 165349388120302, 123968326805899, 79638234559694, 259559389823590, 256776519514651, 107733244474073, 216508566448440, 39327578905012, 118682486932022, 263357223061004, 132872609024098, 44605761726563, 24908360451602, 237906955893793, 204469770496199, 7055254513808, 221802659519968, 169686619990988, 23128789035141, 208847144870760, 272339624469135, 269511404473473, 112830627321371, 73203551744776, 42843503010671, 118193938825623, 49625220390324, 230439888723036, 241486656550572, 107149406378865, 233503862264755, 269502011971514, 181805192674559, 152612003195556, 184127512098087, 165959151027513, 188723045133473, 241615906682300, 216101484550038, 81190147709444, 124498742419309]
    M = 4051501228761632
    K = Knapsack_Attacks(a,M)
    # K.run()
