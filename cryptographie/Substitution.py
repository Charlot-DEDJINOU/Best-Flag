from FileManeger import read, write

def crypt(input_file, output_file, key) :
    messages = read(input_file).split(chr(10))
    content = list()
    for message in messages :
        for c in message.split() :
            content.append(chr(32) * int(c) + chr(key))
        
        content.append(chr(10))
    
    content.pop()

    write(output_file, ''.join(content))


def decrypt(input_file, output_file, key) :
    messages = read(input_file).split(chr(10))
    content = list()
    for message in messages :
        deshiffer = ' '.join([str(len(c)) for c in message.split(chr(key))[:-1]])
        content.append(deshiffer)

    write(output_file, chr(10).join(content))