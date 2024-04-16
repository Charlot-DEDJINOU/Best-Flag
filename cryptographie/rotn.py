from file import write, read

def crypt(input_file, output_file, key, alphabet) : 
    messages = read(input_file).split(chr(10))
    content = list()

    for (index,message) in enumerate(messages) :
        content.append(crypting(message, alphabet, key + index + 1))

    write(output_file, chr(10).join(content))


def decrypt(input_file, output_file, key, alphabet) :
    messages = read(input_file).split(chr(10))
    content = list()

    for (index,message) in enumerate(messages) :
        content.append(decrypting(message, alphabet, key + index + 1))

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