from cryptographie.file import read, write
from cryptographie.utils import getKey, getPaddings

def crypt(input_file, output_file, key, salt, info):
    messages = read(input_file).split(chr(10))
    content = list()
    custom_key = getKey(key)
    paddings = getPaddings(key, salt, info)
    index = 0

    for message in messages:
        for c in message.split():
            content.append(chr(32) * (int(c) + int(paddings[index], 16)) + chr(custom_key))
            index += 1
            if index == len(paddings):
                index = 0

        content.append(chr(10))
    
    content.pop()
    write(output_file, ''.join(content))

def decrypt(input_file, output_file, key, salt, info):
    messages = read(input_file).split(chr(10))
    content = list()
    custom_key = getKey(key)
    paddings = getPaddings(key, salt, info)
    index = 0
    
    for message in messages:
        segments = message.split(chr(custom_key))[:-1]
        decrypted_values = []
        
        for segment in segments:
            original_value = len(segment) - int(paddings[index], 16)
            decrypted_values.append(str(original_value))
            index += 1
            if index == len(paddings):
                index = 0
        
        content.append(' '.join(decrypted_values))

    write(output_file, chr(10).join(content))