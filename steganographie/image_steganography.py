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

    hidden_image = Image.new(host_image.mode, host_image.size)
    hidden_image.putdata(hidden_pixels)
    hidden_image.save(output_image_path)

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

    print(f"Taille de l'image cachée : {hidden_image_size} bits")

    hidden_image_data = extracted_data[128 : 128 + hidden_image_size]

    hidden_image_pixels = []
    for i in range(0, len(hidden_image_data), 24):
        red = int(hidden_image_data[i : i + 8], 2)
        green = int(hidden_image_data[i + 8 : i + 16], 2)
        blue = int(hidden_image_data[i + 16 : i + 24], 2)
        hidden_image_pixels.append((red, green, blue))

    hidden_image = Image.new('RGB', (hidden_image_width, hidden_image_height))
    hidden_image.putdata(hidden_image_pixels)
    hidden_image.save(output_image_path)
    print(f"Image cachée extraite et enregistrée dans '{output_image_path}'.")

from PIL import Image

def encode_LSB(image_path, binary_data):
    image = Image.open(image_path)
    pixels = list(image.getdata())

    # Vérifier que la longueur des données binaires est inférieure au nombre total de pixels
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

    encoded_image = Image.new(image.mode, image.size)
    encoded_image.putdata(encoded_pixels)
    encoded_image.save("encoded_image.png")

binary_data = '100110001111011101010100'

encode_LSB("image_hote.png", binary_data)