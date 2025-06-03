from file import write, read
from utils import getPaddings

def crypt(input_file, output_file, key, salt, info, alphabet) : 
    messages = read(input_file).split(chr(10))
    content = list()
    paddings = getPaddings(key, salt, info)

    for (index,message) in enumerate(messages) :
        content.append(crypting(message, alphabet, int(paddings[index % len(paddings)], 16)))

    write(output_file, chr(10).join(content))


def decrypt(input_file, output_file, key, salt, info, alphabet) :
    messages = read(input_file).split(chr(10))
    content = list()
    paddings = getPaddings(key, salt, info)
    
    for (index,message) in enumerate(messages) :
        content.append(decrypting(message, alphabet, int(paddings[index % len(paddings)], 16)))

    write(output_file, chr(10).join(content))

def crypting(text, alphabet, key):
    encrypted_text = ''
    for char in text:
        if char.isalpha():
            encrypted_text += alphabet[(alphabet.index(char) + key) % len(alphabet)]
        else:
            encrypted_text += char
    return encrypted_text

def decrypting(text, alphabet, key):
    decrypted_text = ''
    for char in text:
        if char.isalpha():
            decrypted_text += alphabet[(alphabet.index(char) - key) % len(alphabet)]
        else:
            decrypted_text += char
    return decrypted_text