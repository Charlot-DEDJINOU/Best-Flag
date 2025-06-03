from file import read, write
from utils import getPaddings

def crypt(input_file, output_file, key, salt, info):
    messages = read(input_file).split(chr(10))
    content = list()
    paddings = getPaddings(key, salt, info)
    index = 0

    for message in messages:
        encrypted_chars = []
        
        for c in message:
            offset = int(paddings[index], 16)
            encrypted_chars.append(str(ord(c) + offset))
            index += 1
            if index == len(paddings):
                index = 0
        
        content.append(' '.join(encrypted_chars))

    write(output_file, chr(10).join(content))
    
def decrypt(input_file, output_file, key, salt, info):
    messages = read(input_file).split(chr(10))
    content = list()
    paddings = getPaddings(key, salt, info)
    index = 0
    
    for message in messages:
        decrypted_chars = []
        
        for encrypted_value in message.split():
            offset = int(paddings[index], 16)
            decrypted_chars.append(chr(int(encrypted_value) - offset))
            index += 1
            if index == len(paddings):
                index = 0
        
        content.append(''.join(decrypted_chars))

    write(output_file, chr(10).join(content))
