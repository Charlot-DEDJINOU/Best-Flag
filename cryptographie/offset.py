from file import read, write
from utils import getPaddings

def crypt(input_file, output_file, key, salt, info):
    messages = read(input_file).split(chr(10))
    content = list()
    paddings = getPaddings(key, salt, info)
    padding_index = 0
    
    for message in messages:
        words = message.split()
        crypted_words = []
        
        for word in words:
            word_key = int(paddings[padding_index], 16)
            crypted_word = crypting(word, word_key)
            crypted_words.append(crypted_word)
            padding_index += 1
            if padding_index >= len(paddings):
                padding_index = 0
        
        sentence = ' '.join(crypted_words)
        sentence_key = int(paddings[padding_index], 16)
        final_crypted = crypting(sentence, sentence_key)
        content.append(final_crypted)
        
        padding_index += 1
        if padding_index >= len(paddings):
            padding_index = 0
    
    write(output_file, chr(10).join(content))


def decrypt(input_file, output_file, key, salt, info):
    messages = read(input_file).split(chr(10))
    content = list()
    paddings = getPaddings(key, salt, info)
    padding_index = 0
    
    for message in messages:
        words_count = message.count(' ') + 1
        
        temp_index = padding_index
        for _ in range(words_count):
            temp_index += 1
            if temp_index >= len(paddings):
                temp_index = 0
        
        sentence_key = int(paddings[temp_index], 16)
        decrypted_sentence = decrypting(message, sentence_key)
        
        words = decrypted_sentence.split()
        decrypted_words = []
        
        for word in words:
            word_key = int(paddings[padding_index], 16)
            decrypted_word = decrypting(word, word_key)
            decrypted_words.append(decrypted_word)
            padding_index += 1
            if padding_index >= len(paddings):
                padding_index = 0
        
        content.append(' '.join(decrypted_words))
        
        # Avancer pour la clé de phrase
        padding_index += 1
        if padding_index >= len(paddings):
            padding_index = 0

    write(output_file, chr(10).join(content))


def crypting(s, key):
    if len(s) > key and key > 0:
        res = [""] * len(s)
        
        for i in range(len(s)):
            index = i
            for _ in range(key):
                index += 1
                if index > len(s) - 1:
                    index = 0
            nextPlace = index
            res[nextPlace] = s[i]
        
        return ''.join(res)
    else:
        return s


def decrypting(s, key):
    if len(s) > key and key > 0:
        res = [''] * len(s)
        
        for i in range(len(s)):
            index = i
            for _ in range(key):
                index -= 1
                if index < 0:
                    index = len(s) - 1
            nextPlace = index
            res[nextPlace] = s[i]
        
        return ''.join(res)
    else:
        return s