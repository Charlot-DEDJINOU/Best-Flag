from FileManeger import read, write

def crypt(input_file, output_file, key):
    messages = read(input_file).split(chr(10))
    content = list()

    for message in messages :
        content.append(crypting(' '.join([crypting(c, key) for c in message.split()]), key))
    
    write(output_file, chr(10).join(content))


def decrypt(input_file, output_file, key):
    messages = read(input_file).split(chr(10))
    content = list()

    for message in messages :
        content.append(' '.join([decrypting(c, key) for c in decrypting(message, key).split()]))

    write(output_file, chr(10).join(content))


def crypting(s, key) : 
    if len(s) > key:
        res = [""] * len(s)

        for i in range(len(s)) :
            index = i
            for _ in range(key) :
                index += 1
                if index > len(s) - 1 :
                    index = 0
            nextPlace = index
            res[nextPlace] = s[i]
        
        return ''.join(res)
    else:
        return s
    
def decrypting(s, key) : 
    if len(s) > key :
        res = [''] * len(s)

        for i in range(len(s)) :
            index = i
            for _ in range(key) :
                index -= 1
                if index < 0 :
                    index = len(s) - 1
            nextPlace = index
            res[nextPlace] = s[i]

        return ''.join(res)
    else :
        return s