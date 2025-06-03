from math import floor
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

def getKey(s) :
    num = 0
    dem = 0
    
    for (index, item) in enumerate(s) :
        if item.isdigit() :
            num += int(item) + index
            dem += int(item)
        else :
            num += ord(item) + index
            dem += index * 2

    return floor(num/dem)**2

def getPaddings(s, salt, info, length_bytes=5000) :
    hkdf = HKDF(
        algorithm=hashes.SHA256(),
        length=length_bytes,
        salt=salt.encode(),
        info=info.encode(),
        backend=default_backend()
    )
    derived_key = hkdf.derive(s.encode())
    paddings = derived_key.hex()

    return list(paddings)