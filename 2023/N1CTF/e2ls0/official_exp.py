from sage.all import *
p = 31056954144466551354887631023962695320706316712255640373035795693815085684947
a = 29044030291754400812460259687647677793710240498564440662990181268131640570302
Fp = GF(p)
Pt=PolynomialRing(Zmod(p),name='x')
x=Pt.gen()
F = GF(p ** 2, modulus=x ** 2 + 1,name='o')
o=F.gen()
PR= PolynomialRing(Fp,names=["j", "j1"," j2", "b1", "x1", "y1"])
j, j1, j2, b1, x1, y1=PR.gens()
phi = x1 ** 4 + y1 ** 4 - x1 ** 3 * y1 ** 3 + 2232 * (x1 ** 3 * y1 ** 2 + y1 ** 3 * x1 ** 2) - 1069956 * (
            x1 ** 3 * y1 + y1 ** 3 * x1) + 36864000 * (x1 ** 3 + y1 ** 3) \
      + 2587918086 * x1 ** 2 * y1 ** 2 + 8900222976000 * (x1 ** 2 * y1 + y1 ** 2 * x1) + 452984832000000 * (
                  x1 ** 2 + y1 ** 2) - 770845966336000000 * x1 * y1 \
      + 1855425871872000000000 * (x1 + y1)

coeff = list(phi.subs(x1=j, y1=j1 + j2 * o))
f1 = PR(0)
f2 = PR(0)
print(type(coeff[0][1][1]))
for item in coeff:
    if item[0][1]:
        f2 += item[0][1] * item[1] #实部
    else:
        f1 += item[0] * item[1]  #虚部

f3 = -j1 ** 2 + Fp(a) ** (-1) * j1

f1 = f1.change_ring(ZZ)
f2 = f2.change_ring(ZZ)
h = list(PR(f1.resultant(f2)))

f = 0
for item in h:
    k = 1
    while True:
        if item[1] % (j2 ** 2) ** k:
            break
        else:
            k += 1
    f += item[0] * (item[1] // ((j2 ** 2) ** (k - 1))) * f3 ** (k - 1)

Rp= PolynomialRing(Fp,name='x')
x=Rp.gen()
f = Rp(f.univariate_polynomial())
may = f.roots()

for item in may:
    try:
        j1_ = item[0]
        j2_ = Fp(f3.subs(j1=j1_)).nth_root(2)
        num = F(j1_) + F(j2_) * o

        phi = phi.change_ring(F)
        j_ = ZZ(phi.subs(y=num).univariate_polynomial().roots()[0][0])

        d = len(str(j_))
        zeta = len(str(2 ** 80))
        L = Matrix(ZZ, [[10 ** d, 0, 0, 10 ** (2 * d)],
                        [0, 10 ** d, 0, -10 ** d * 2 * j_],
                        [0, 0, 10 ** (d + zeta), -j_ ** 2]])

        basis = L.LLL()[0]

        t = abs(basis[1] // 10 ** d)
        k = abs(basis[0] // 10 ** d) + t ** 2
        print(bytes.fromhex(hex(k)[2:]).decode())
    except:
        continue