import binascii
import hashlib
from flag import flag
from Crypto.Cipher import AES
from Crypto.Util import *
import os

key1 = os.urandom(32)
key2 = b'tn*-ix6L*tCa*}i*'
key_len = len(key2)
assert flag.startswith(b'flag{')
assert (flag[13] == 45 and flag[18] == 45 and flag[23] == 45 and flag[28] == 45)
flag1 = b"2023: "+flag[:13]+flag[14:18]+flag[19:23]
flag2 = 'a3eae82b4c491e0e'

h = binascii.unhexlify(hashlib.sha256(key2).hexdigest())[:11]
gift1 = b'***********************************************************************************************'
gift2 = b'I tell you this, for when my days have come to an end , you, shall be King.'+h


def encrypt1(message, key):
    cipher = AES.new(key, AES.MODE_CTR, counter=Counter.new(128))
    ciphertext = cipher.encrypt(message)
    return ciphertext.hex()


def encrypt2(message, key, iv):
    padding = bytes((key_len - len(message) % key_len) * '&', encoding='utf-8')
    message += padding
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(message)
    return ciphertext.hex()


print("enc_gift1 = "+encrypt1(gift1, key1))
print("enc_flag = "+encrypt1(flag1, key1))
print("enc_gift2 = "+encrypt2(gift2, key2, flag2))

# enc_gift1 = bad7dbcff968d7cdbf51da011fe94e176fc8e7528e4dd85d2d5fc20ba69cefb7bfd03152a2874705bd2d857ea75b3216a830215db74772d9b9e9c218271d562694d3642d2917972fdb8c7363d8125730a50824cd8dc7e34cd4fa54be427cca
# enc_flag = c1c78891e30cd4c0aa5ed65c17e8550429c4e640881f9f1d6a56df
# enc_gift2 = ********c********b**************4***5********3****6a*****a**2********c*8******7***********3***5***2********e*5*************a******5**c***74***********fee046b4d2918096cfa3b76d6622914395c7e28eef
