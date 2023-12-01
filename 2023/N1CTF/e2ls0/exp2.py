#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2023/11/17 15:23
import ast

# https://math.mit.edu/~drew/ClassicalModPolys.html
mp3_def_str = """[1,0] 1855425871872000000000
[1,1] -770845966336000000
[2,0] 452984832000000
[2,1] 8900222976000
[2,2] 2587918086
[3,0] 36864000
[3,1] -1069956
[3,2] 2232
[3,3] -1
[4,0] 1"""
mp3_def = [
    [ast.literal_eval(x) for x in line.split(" ")] for line in mp3_def_str.split("\n")
]
mp_term = (
    lambda e, coef: lambda x, y: coef * x ** e[0] * y ** e[1]
    + coef * x ** e[1] * y ** e[0]
    if e[0] != e[1]
    else coef * x ** e[0] * y ** e[1]
)
mp = lambda mp_def: lambda x, y: sum([mp_term(*term)(x, y) for term in mp_def])
mp3 = mp(mp3_def)


from pwn import process, remote
import subprocess


def connect():
    # io = process(["sage", "task.sage"])
    # return io

    io = remote("121.41.9.20", int(6668))
    io.recvuntil(b") solve ")
    pow_token = io.recvlineS().strip()
    input(f"continue run pow with {pow_token}?")
    ret = subprocess.check_output(
        "python3 <(curl -sSL https://goo.gle/kctf-pow) solve " + pow_token,
        shell=True,
        timeout=20,
    )
    print(ret)
    io.sendline(ret)
    return io


io = connect()
io.recvuntil(b"of size ")
p = ZZ(io.recvuntil(b"^2", drop=True).decode())
io.sendlineafter(b"$ ", b"-1")  # (-1)^r-1=p^2-2 (mod p^2) if r is odd
leak = ZZ(io.recvline().decode())
print(leak)

"""
j1=A+0i  # two unk
j2=C+Di  # two unk
phi(j1,j2)=0  # two eq
B=0  # one eq
(C+Di)*(leak+Fi)=1  # one unk, two eq
"""

x = var("x")
Fp = GF(p)
Fp2 = GF(p ^ 2, "i", modulus=x**2 + 1)
i = Fp2.gen()
aa, cc, dd, ff = Fp2["aa,cc,dd,ff"].gens()
PR_Fp = Fp["aa,cc,dd,ff"]
f = mp3(aa + 0 * i, cc + dd * i)
f_real = PR_Fp(f.map_coefficients(lambda c: c.polynomial()[0]))
f_imag = PR_Fp(f.map_coefficients(lambda c: c.polynomial()[1]))
g = (cc + dd * i) * (leak + ff * i) - 1
g_real = PR_Fp(g.map_coefficients(lambda c: c.polynomial()[0]))
g_imag = PR_Fp(g.map_coefficients(lambda c: c.polynomial()[1]))
aa, cc, dd, ff = PR_Fp.gens()
f1 = f_real.sylvester_matrix(f_imag, dd).det()  # function of a, c
f2 = f_real.sylvester_matrix(g_real, dd).det()  # function of a, c, f
f3 = g_real.sylvester_matrix(g_imag, dd).det()  # function of c, f
f4 = f2.sylvester_matrix(f3, ff).det()  # function of a, c
g = f1.sylvester_matrix(f4, cc).det().univariate_polynomial()  # function of a
for r, _ in g.roots():
    print(r, ZZ(r).bit_length())
    if r > 0 and ZZ(r).bit_length() < 200:
        target_j = ZZ(r)
print("j", target_j)


def recover(r):
    # r = sqrt(n) - floor(sqrt(n))
    # set k = floor(sqrt(n)) is integer
    # (r+k)^2 = r^2 + 2rk + k^2 = n
    # n - 2rk - k^2 - r^2 = 0
    # set m = n - k^2, which is approximately equal to k
    error = -4.22494828768973e-29  # the error by experimenting
    k_ap = 2 ** (20 * 8 // 2)  # approximate k

    B = matrix(
        QQ, [[1, 1, 0, 0], [-2 * QQ(r), 0, 1, 0], [-QQ(r) ** 2, 0, 0, 1]]  # m  # k  # 1
    )
    bounds = [QQ(abs(error)), k_ap, k_ap, 1]
    Q = diagonal_matrix([2**512 // b for b in bounds])
    B *= Q
    T, mul = B._clear_denom()
    T = T.LLL()
    B = T.change_ring(QQ) / mul
    B /= Q
    for row in B:
        if row[-1] < 0:
            row = -row
        if row[-1] == 1:
            n_sub_k2 = row[1]
            k = row[-2]
            return k**2 + n_sub_k2


R = RealField(256)
r = R(target_j) / 10 ** len(str(target_j))  # take the fractional part of sqrt(n)
print(r)
n = recover(r)
print(n)
guess = int(n).to_bytes(20, "big").decode()
print(guess)
io.sendline(guess.encode())
io.interactive()
# n1ctf{0h_you_c4n_get_j_fr0m_th3_h4lf@#$%}
