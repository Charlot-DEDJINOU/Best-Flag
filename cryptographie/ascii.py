from file import read, write
from math import floor

def crypt(input_file, output_file, key) :
    messages = read(input_file).split(chr(10))
    content = list()
    key = getKey(key)
    for message in messages :
        shiffer = ' '.join([str(ord(c) + key) for c in message])
        content.append(shiffer)

    write(output_file, chr(10).join(content))
    
def decrypt(input_file, output_file, key) :
    messages = read(input_file).split(chr(10))
    content = list()
    key = getKey(key)
    for message in messages:
        deshiffer = ''.join([chr(int(c) - key) for c in message.split()])
        content.append(deshiffer)

    write(output_file, chr(10).join(content))

def getKey(s) :
    num = 0
    dem = 0
    for (index, item) in enumerate(s) :
        num += ord(item) + index
        dem += index * 2

    return floor(num/dem) + 1