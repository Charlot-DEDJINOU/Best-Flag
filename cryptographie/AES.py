from cryptography.fernet import Fernet
from FileManeger import read, write

def crypt(input_file, output_file, key) :
    cipher_suite = Fernet(key)
    messages = read(input_file).split(chr(10))
    content = list()

    for (message) in messages :
        content.append(aes_encrypt(message, cipher_suite).decode())

    write(output_file, chr(10).join(content))

def decrypt(input_file, output_file, key) :
    cipher_suite = Fernet(key)
    messages = read(input_file).split(chr(10))
    content = list()

    for (message) in messages :
        content.append(aes_decrypt(message.encode(), cipher_suite))

    write(output_file, chr(10).join(content))

def aes_encrypt(message, fernet):
    encrypted_message = fernet.encrypt(message.encode())
    return encrypted_message

def aes_decrypt(message, fernet):
    decrypted_message = fernet.decrypt(message).decode()
    return decrypted_message