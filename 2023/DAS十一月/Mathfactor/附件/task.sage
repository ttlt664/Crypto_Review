from random import randint
from Crypto.Util.number import *
from secret import flag
def encrypt(key, message, mask):
    return pow(64901, message^^mask, key)
def get_Prime_leak(bits,t1):
    x,y=0,1
    while True:
        
        u=randint(1,200)
        v=randint(1,200)
        x,y=u*x+t1*v*y,v*x-u*y
        if int(x).bit_length()<=bits//2:
            p=x^2+t1*y^2|1
            if isPrime(int(p)) and int(p).bit_length()>=bits:
                return p
        else:
            x,y=0,1
t1=getPrime(16)
print(f"t1={t1}")
p=get_Prime_leak(512,t1)
q=get_Prime_leak(512,t1)
assert p>q
n=p*q
print(f"n={n}")
flag=bytes_to_long(flag)
messages = [getRandomNBitInteger(flag.bit_length()) for i in range(200)]
enc = [encrypt(p, message, flag) for message in messages]

with open("output.txt",'w')as f2:
    f2.write(f'message = {messages}\n')
    f2.write(f'enc = {enc}')

#t1=39041
#n=31757681951092898377241647622353350811555571588021442714393002561722357855033517882719102833176105251763057313366942759802483366389547670310504898517419619177075155149247837212852121269080431969095421646338619498652624131319645919876504536274428562199882910834700167991957991646691071345200388502034841600000001
