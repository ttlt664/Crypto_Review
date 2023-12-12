#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2023/12/12 17:44
import sys
class Knapsack:
    def __init__(self):
        self.type = None
    def pr(self):
        print("input 1 to get Modular knapsacks\n")
        print("input 2 to get Random knapsacks\n")
        print("input 3 to get Unbalanced knapsacks\n")


    def change_type(self,s):
        if s == 1:
            self.type = "Modular knapsacks"
        elif s == 2:
            self.type = "Random knapsacks"
        else:
            self.type = "Unbalanced knapsacks"

    def run(self):
        Knapsack.pr(self)
if __name__=="__main__":
    k = Knapsack()
    k.run()