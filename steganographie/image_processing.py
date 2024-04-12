from file import read, write
from PIL import Image

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

def extracted_last_bits(host_pixels) :
    extracted_bits = []
    for pixel in host_pixels:
        red = pixel[0] & 1
        green = pixel[1] & 1
        blue = pixel[2] & 1
        extracted_bits.extend([red, green, blue])

    return extracted_bits

image_from_pixels('pixels.txt', 'retraite.png', (500,500))