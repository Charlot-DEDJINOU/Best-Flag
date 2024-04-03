from FileManeger import read, write

def crypt(input_file, output_file, key) :
    messages = read(input_file).split(chr(10))
    content = list()
    for message in messages :
        shiffer = ' '.join([str(ord(c) + key) for c in message])
        content.append(shiffer)

    write(output_file, chr(10).join(content))
    
def decrypt(input_file, output_file, key) :
    messages = read(input_file).split(chr(10))
    content = list()
    for message in messages:
        deshiffer = ''.join([chr(int(c) - key) for c in message.split()])
        content.append(deshiffer)

    write(output_file, chr(10).join(content))