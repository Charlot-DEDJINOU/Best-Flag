from file import read, write

def text_to_binary(text):
    binary_data = ''
    for char in text:
        ascii_value = ord(char)
        binary_value = bin(ascii_value)[2:]
        binary_data += binary_value.zfill(8)
    return binary_data

def binary_to_text(binary_data):
    text = ''
    for i in range(0, len(binary_data), 8):
        binary_chunk = binary_data[i:i+8]
        char = chr(int(binary_chunk, 2))
        text += char
    return text

def save_binary_to_text(input_file, output_file) :
    write(output_file, text_to_binary(read(input_file)))

def save_text_to_binary(input_file, output_file) :
    write(output_file, binary_to_text(read(input_file)))