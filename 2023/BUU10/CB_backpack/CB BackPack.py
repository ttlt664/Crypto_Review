from random import shuffle
from hashlib import *
from random import *
def gen_e():
    e = []
    for i in range(8):
        ee = [0]*3+[1]*3
        shuffle(ee)
        e += ee
    return e
# 生成随机字符串的01一共48位
e = gen_e()
print(len(e))
nbit = len(e)
flag = 'DASCTF{'+sha256(''.join([str(i) for i in e]).encode()).hexdigest()+'}'

a = [randint(1,2^nbit) for i in range(nbit)]
# 一共48个大数
# 1~2**48
re = 0
for i in range(nbit):
    re += e[i]*a[i]
# 这48个大数要么存在于加法线性中要么不存在
print(a)
print(re)