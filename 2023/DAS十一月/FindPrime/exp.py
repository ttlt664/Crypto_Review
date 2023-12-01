#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2023/11/30 16:23
p_list = []
with open("output.txt","r") as f:
    s = f.read().split("\n")[:-1]
    for t in s:
        y = int(t)
        p_list.append(y)
