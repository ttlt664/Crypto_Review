#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2023/12/12 17:44
import sys
import math
import argparse
class Knapsack:
    def __init__(self):
        self.type = None
        self.a = None
        self.n = None
    def pr(self):
        print("Usage:")
        print("python Knapsack_many.py --v1= --v2=")
        print("input v1=1 to get Modular knapsacks\n")
        print("input v1=2 to get Random knapsacks\n")
        print("input v1=3 to get Unbalanced knapsacks\n")

    def calc_density(self):
        self.n = len(self.a)
        t = math.log(max(self.a), 2)
        density = float(self.n / t)
        print("===================================================")
        print(f"density of the knapsack is {density}")
        return density

    def change_type(self):
        s = sys.argv[1]
        if s == 1:
            self.type = "Modular knapsacks"
        elif s == 2:
            self.type = "Random knapsacks"
        else:
            self.type = "Unbalanced knapsacks"

    def run(self):
        Knapsack.pr(self)
        Knapsack.get_RandomKnapsacks(self)
    def get_ModularKnapsacks(self):

        return
    def get_random_parameters(self):

        return
    def get_RandomKnapsacks(self):
        n = self.n
        D = Knapsack.calc_density(self)
        B = math.floor(2**(n/D))
        print(B)
        return

    def get_UnbalancedKnapsacks(self):

        return


if __name__ == "__main__":
    k = Knapsack()
    k.run()
