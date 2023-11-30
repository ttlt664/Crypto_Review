from Crypto.Util.number import *
from random import randint
flag=b"flag{this_is_a_test_flag}"
order=1141741939958844590498346884870015122544171009688372185479632675211885925945760

class CB_curve:
    def __init__(self):
        self.p = 1141741939958844590498346884870015122543626602665954681008204697160652371664923
        self.a = 727131475903635498678013730344448225340496007388151739960305539398192321065043
        self.b = 840714623434321649308065401328602364673881568379142278640950034404861312007307

    def add(self, P, Q):
        if P == -1:
            return Q
        (x1, y1) = P
        (x2, y2) = Q
        x3 =  (x1+x2)*(1+self.a*y1*y2)*inverse((1+self.b*x1*x2)*(1-self.a*y1*y2),self.p)% self.p
        y3 =  (y1+y2)*(1+self.b*x1*x2)*inverse((1-self.b*x1*x2)*(1+self.a*y1*y2),self.p)% self.p
        return (x3, y3)

    def mul(self, x, P):
        Q = -1
        while x > 0:
            if x & 1:
                Q = self.add(Q, P)
            P = self.add(P, P)
            x = x >> 1
        return Q
    
    def negG(self,G):
        return self.mul(order-1,G)

ecc = CB_curve()
G = (586066762126624229327260483658353973556531595840920560414263113786807168248797, 66727759687879628160487324122999265926655929132333860726404158613654375336028)
P = (ecc.mul(bytes_to_long(flag),G)[0],randint(1,ecc.p))
Q = (460843895959181097343292934009653542386784127282375019764638432240505304648101, 739422832583403823403837831802136107593509589942947902014204968923412689379907)
p=1141741939958844590498346884870015122543626602665954681008204697160652371664923
e = randint(1,p)
pl = [ecc.add(P,ecc.mul(10-i,ecc.negG(Q)))[0] + e for i in range(10)]
ph = [ecc.add(P,ecc.mul(10-i,Q))[0] + e for i in range(10)]

print(pl)
print(ph)
