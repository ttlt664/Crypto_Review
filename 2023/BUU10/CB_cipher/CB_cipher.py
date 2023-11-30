from random import randint
from pylfsr import LFSR
from Crypto.Util.number import *
from secret import state1,state2,state3,flag

assert b'DASCTF' in flag

fpoly1 = [14,13,6,2]
fpoly2 = [20,15,12,9,7,4,3]
fpoly3 = [13,12,11,9,7,6,3]

def iv():
    a,b,c = L1.next(),L2.next(),L3.next()
    return (a & b) ^ (b & c) ^ c

class CB_cipher():
    def __init__(self):
        key = [''.join([str(randint(0,1)) for i in range(16)]) for j in range(2)]

        self.key = [[int(j) for j in i] for i in key]
        
        self.sbox = [0x6, 0x4, 0xc, 0x5,
                     0x0, 0x7, 0x2, 0xe,
                     0x1, 0xf, 0x3, 0xd,
                     0x8, 0xa, 0x9, 0xb]
    
    def s_trans(self,pt):
        pt = ''.join([str(i) for i in pt])
        pt = [self.sbox[int(i,16)] for i in hex(int(pt,2))[2:].rjust(4,'0')]
        ct = ''.join([bin(i)[2:].rjust(4,'0') for i in pt])
        ct = [int(i) for i in ct]
        return ct
        
    def encrypt(self,pltxt):
        key_add = lambda x,key : [x[i]^key[i] for i in range(len(x))]
        bit_move = lambda x : [x[(i//4)+(i%4)*4] for i in range(len(x))]
        
        ct = [int(i) for i in pltxt]
        
        for i in range(5):
            ct = key_add(ct,self.key[i%2])
            ct = self.s_trans(ct)
            if (i+1)%2:
                ct = bit_move(ct)
        
        ct = key_add(ct,self.key[1])
        return ''.join([str(i) for i in ct]) 
    
    def bt_to_bin(self,msg):
        msg = msg if (len(msg)+1)%2 else msg+b'\x00'
        return bin(bytes_to_long(msg))[2:].rjust(8*len(msg),'0')
        
    def txt_encrypt(self,msg):
        time = (len(msg)+1)//2
        pltxt = [self.bt_to_bin(msg)[i*16:i*16+16] for i in range(time)]
        #print(pltxt)
        output = []
        
        for i in range(time):
            now_re = self.encrypt(pltxt[i])
            if output != []:
                now_re = bin(int(now_re,2) ^ int(output[-1],2))[2:].rjust(16,'0')
            output.append(now_re)
        
        return long_to_bytes(int(''.join(output),2))
    
L1 = LFSR(fpoly = fpoly1, initstate = state1)
L2 = LFSR(fpoly = fpoly2, initstate = state2)
L3 = LFSR(fpoly = fpoly3, initstate = state3)

iv_txt = ''
for i in range(len(flag)*8):
    iv_txt += str(iv())
    
a = CB_cipher()

print(iv_txt[:320])
print(a.txt_encrypt(b'Welcome to our CBCTF! I hope you can have a nice day here. Come with me.'))
print(long_to_bytes(bytes_to_long(a.txt_encrypt(flag))^int(iv_txt,2)))

#10101010100110100000111111011110111101010010011000011011001010010010111000100101011111010001110110110111000010100001010111110110000011110100110011011110001100100011101101110001000100111100001111100111010100010000001101001001000011110001100110101100101000101001110011101100001100100000011101011110100110110110000110010101
#b'\x10\x07t9\x88\x95\x8b&\xb2\x8fp\xe7\xce\\k{\xbb\xe5\xa7\xb8\x92\xbe\xd1\n\x84.\xe1\xe0\xab\x08\x97\x92\x1a\xbd\xdf\x80R\xbe\xe2\x84\xe17\x14\x8a\x07\x03\x87)\xb2\xa6W:\xda\x04Y\xa5\xca\x16o1\x93\x9d\x90.\xcdS\xd6\xcbK\xf4\xd8G'
#b"\xec\x16<[D;F6\xb6\xcc\x7f\x80jL1\xb1@\x84iF[\xfcW\xbbbp\xdc\x0fI,%\x15\x1a\xbe\x86hT\r\xf0\x8a\xa91\x9aF\xe3\x84n\xeb\xe9\xa3,T\xec\x8f\xdbb\xc1\xd7\xe7&'u\xe9A\xe9\x03\xe1\x89\x04\x8f\xa77\x8a\xd7\x97x\xccl\x1e\xc6\xea%\xb1/P\x98\x8e\x9bS\xca\xf5kR\x98H\xc6d\x15"