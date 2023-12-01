#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2023/11/2 18:00

with open("output.txt", "r") as f:
    c = f.read()
c = c.split("\n")
m = c[0][11:-1].split(",")
ec = c[1][7:-1].split(",")
message = []
enc = []
for t in m:
    t = int(t)
    message.append(t)
for e in ec:
    e = int(e)
    enc.append(e)
print(message)
print(enc)
print(len(enc))