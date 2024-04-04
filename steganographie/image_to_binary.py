from PIL import Image

def save_pixels_to_file(image_path, output_file):
    # Charger l'image
    image = Image.open(image_path)

    # Récupérer les pixels de l'image
    pixels = list(image.getdata())

    # Convertir les pixels en données binaires
    binary_data = ''
    for pixel in pixels:
        red, green, blue = pixel
        binary_data += format(red, '08b')
        binary_data += format(green, '08b')
        binary_data += format(blue, '08b')

    with open(output_file, 'w') as file:
        file.write(binary_data)

    print(f"Données des pixels enregistrées dans '{output_file}' avec succès.")


image_path = "open.jpg"

output_file = "pixels.txt"

save_pixels_to_file(image_path, output_file)