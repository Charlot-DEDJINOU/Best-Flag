from file import read, write
from math import floor

def crypt(input_file, output_file, key) :
    messages = read(input_file).split(chr(10))
    content = list()
    key = getKey(key)
    for message in messages :
        for c in message.split() :
            content.append(chr(32) * int(c) + chr(key))
        
        content.append(chr(10))
    
    content.pop()

    write(output_file, ''.join(content))

def decrypt(input_file, output_file, key) :
    messages = read(input_file).split(chr(10))
    content = list()
    key = getKey(key)
    for message in messages :
        deshiffer = ' '.join([str(len(c)) for c in message.split(chr(key))[:-1]])
        content.append(deshiffer)

    write(output_file, chr(10).join(content))

def getKey(s) :
    num = 0
    dem = 0
    for (index, item) in enumerate(s) :
        if item.isdigit() :
            num += int(item) + index
            dem += int(item)

    return floor(num/dem)**2