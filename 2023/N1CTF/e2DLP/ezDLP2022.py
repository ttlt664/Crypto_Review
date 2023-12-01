from Crypto.Util.number import *
from math import prod

flag = b"flag{this_is_a_test_flag@@@@@@@}"


def keygen(pbits, kbits, k):
    p = getPrime(pbits)
    x = [getPrime(kbits + 1) for i in range(k)]  # 25*20
    y = prod(x)  # 500
    while 1:
        r = getPrime(pbits - kbits * k)  # 12
        q = 2 * y * r + 1  # 512
        if isPrime(q):
            return p * q, (p, q, r, x)


def encrypt(key, message):
    return pow(0x10001, message, key)


key = keygen(512, 24, 20)
flag = bytes_to_long(flag)
messages = [getPrime(flag.bit_length()) for i in range(47)] + [flag]  # 48*flag
enc = [encrypt(key[0], message) for message in messages]  # 挨个加密

print("message=" + str(messages[:-1]))
print("enc=" + str(enc))
