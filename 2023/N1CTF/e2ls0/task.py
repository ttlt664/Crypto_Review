from string import ascii_letters
from sympy import sqrt
import random
import signal
import os
import time

FLAG = os.environ.get('FLAG', 'n1ctf{0h_you_c4n_get_j_fr0m_th3_h4lf@#$%}')
from sage.all import *


def banner():
    print("""
░░░░░░░ ░░░░░░  ░░ ░░░░░░░  ░░░░░░  
▒▒           ▒▒ ▒▒ ▒▒      ▒▒    ▒▒ 
▒▒▒▒▒    ▒▒▒▒▒  ▒▒ ▒▒▒▒▒▒▒ ▒▒    ▒▒ 
▓▓      ▓▓      ▓▓      ▓▓ ▓▓    ▓▓ 
███████ ███████ ██ ███████  ██████  
    """)


def curve_init():
    p = random_prime(2 ^ 256)
    Pt = PolynomialRing(GF(p), name='x')
    x = Pt.gen()
    F = GF(p ^ 2, modulus=x ** 2 + 1, name='i')
    # 这个有限域在这个剩余类上 同时剩余类在这个拓展域上
    R = PolynomialRing(GF(p), name='t')
    t = R.gen()
    guess = ''.join(random.choices(ascii_letters, k=20))
    RR = RealField(256)
    num = RR(int(guess.encode().hex(), 16))
    j = F(str(sqrt(num)).split('.')[1])
    E = EllipticCurve(j=j)  # 拿了小数点后面的值作为j不变量，即使恢复了j应该我也只能得到小数点后面的值 然后如果有前面的就爆破吧
    P = E(0).division_points(3)
    P.remove(E(0))
    phi = E.isogeny(random.choice(P))
    E2 = phi.codomain()  # 3同源上的点集
    j2 = E2.j_invariant()
    assert list(R(j2))[1] != 0
    return E2, p, guess  # guess是生成不变量的


def leak(E, p):
    F = Zmod(p ^ 2)
    R = PolynomialRing(GF(p), name='t')
    t = R.gen()
    r = random.getrandbits(20)
    x = F(input("your magic number?\n$ ")) ^ r - 1
    j_ = E.j_invariant() ^ x  # 次方
    print(list(R(j_))[0])  # 给出这里的j_的常数项


def main():
    signal.alarm(120)
    banner()
    para = None
    print("Curve Initialization...")
    while not para:
        try:
            para = curve_init()
        except:
            continue
    E, p, guess = para
    print(f"einfo: {E.base_ring()}")  # p
    leak(E, p)
    if input("guess > ").strip('\n') == guess:
        print(f"Congratz, your flag: {FLAG}")
    else:
        print("Game over!")


if __name__ == "__main__":
    try:
        print(time.time())
        main()
        print(time.time())
    except:
        print("error!")
