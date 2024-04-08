from file import read, write
from PIL import Image

def hide_image(image_to_hide_path, host_image_path, output_image_path):
   
    image_to_hide = Image.open(image_to_hide_path)
    host_image = Image.open(host_image_path)

    width_binary = format(image_to_hide.width, '032b')
    height_binary = format(image_to_hide.height, '032b')
    size_binary = format(len(image_to_hide.tobytes()) * 8, '064b')

    metadata_binary = width_binary + height_binary + size_binary

    binary_data = ''.join(format(pixel, '08b') for pixel in image_to_hide.tobytes())

    binary_data_with_metadata = metadata_binary + binary_data

    if len(binary_data_with_metadata) > len(list(host_image.getdata())) * 3:
        raise ValueError("Les données binaires de l'image à cacher avec métadonnées sont trop volumineuses pour être cachées dans l'image hôte.")

    host_pixels = list(host_image.getdata())
    hidden_pixels = []

    index = 0
    for host_pixel in host_pixels:
        red, green, blue = host_pixel
        if index < len(binary_data_with_metadata):
            red = red & ~1 | int(binary_data_with_metadata[index])
            index += 1
        if index < len(binary_data_with_metadata):
            green = green & ~1 | int(binary_data_with_metadata[index])
            index += 1
        if index < len(binary_data_with_metadata):
            blue = blue & ~1 | int(binary_data_with_metadata[index])
            index += 1
        hidden_pixels.append((red, green, blue))

    create_image(host_image.size, host_image.mode, hidden_pixels, output_image_path)

    print(f"L'image cachée avec métadonnées binaires a été créée avec succès et enregistrée dans '{output_image_path}'.")

def extract_hidden_image(host_image_path, output_image_path):

    host_image = Image.open(host_image_path)

    host_pixels = list(host_image.getdata())

    extracted_bits = []
    for pixel in host_pixels:
        red = pixel[0] & 1
        green = pixel[1] & 1
        blue = pixel[2] & 1
        extracted_bits.extend([red, green, blue])

    extracted_data = ''.join(map(str, extracted_bits))

    metadata = extracted_data[:128]
    hidden_image_width = int(metadata[:32],2)
    hidden_image_height = int(metadata[32:64],2)
    hidden_image_size = int(extracted_data[64:128], 2)

    hidden_image_data = extracted_data[128 : 128 + hidden_image_size]

    hidden_image_pixels = []
    for i in range(0, len(hidden_image_data), 24):
        red = int(hidden_image_data[i : i + 8], 2)
        green = int(hidden_image_data[i + 8 : i + 16], 2)
        blue = int(hidden_image_data[i + 16 : i + 24], 2)
        hidden_image_pixels.append((red, green, blue))

    create_image((hidden_image_width, hidden_image_height), 'RGB', hidden_image_pixels, output_image_path)

    print(f"Image cachée extraite et enregistrée dans '{output_image_path}'.")

def hide_text(image_path, binary_data):
    image = Image.open(image_path)
    pixels = list(image.getdata())

    if len(binary_data) > len(pixels):
        raise ValueError("Les données binaires sont trop longues pour être cachées dans l'image.")

    encoded_pixels = []
    index = 0
    for pixel in pixels:
        red, green, blue = pixel
        if index < len(binary_data):
            red = red & ~1 | int(binary_data[index])
            index += 1
        if index < len(binary_data):
            green = green & ~1 | int(binary_data[index])
            index += 1
        if index < len(binary_data):
            blue = blue & ~1 | int(binary_data[index])
            index += 1
        encoded_pixels.append((red, green, blue))

    create_image(image.size, image.mode, encoded_pixels, "encoded_image.png")

def image_to_pixel(image_path, output_file):
    
    image = Image.open(image_path)

    pixels = list(image.getdata())

    pixel_data = [f"({pixel[0]},{pixel[1]},{pixel[2]})" for pixel in pixels]

    write(output_file, ';'.join(pixel_data))

    print(f"Données des pixels enregistrées dans '{output_file}' avec succès.")


def image_to_bits(image_path, output_file):
   
    image = Image.open(image_path)

    binary_data = ''.join(format(pixel, '08b') for pixel in image.tobytes())

    write(output_file, binary_data)

    print(f"Données des pixels enregistrées dans '{output_file}' avec succès.")


def image_from_bits(bits_file, output_image_path, image_size):

    bits_data = read(bits_file)

    pixels = []
    for i in range(0, len(bits_data), 24):
        red = int(bits_data[i:i+8], 2)
        green = int(bits_data[i+8:i+16], 2)
        blue = int(bits_data[i+16:i+24], 2)
        pixels.append((red, green, blue))

    create_image(image_size, 'RGB', pixels, output_image_path)

    print("Image reconstituée et enregistrée avec succès.")

def image_from_pixels(pixels_file, output_image_path, image_size):
   
    pixel_data = read(pixels_file)

    pixels = []
    for line in pixel_data.split(';'):
        r, g, b = map(int, line.strip('()\n ').split(','))
        pixels.append((r, g, b))

    create_image(image_size, 'RGB', pixels, output_image_path)

    print(f"Image créée et enregistrée dans '{output_image_path}' avec succès.")

def create_image(size, mode, data, output_file) :
    image = Image.new(mode, size)
    image.putdata(data)
    image.save(output_file)


extract_hidden_image('./images/hidden_image.png', './images/charlot.png')