from PIL import Image

def save_image_to_pixel(image_path, output_file):
    image = Image.open(image_path)

    pixels = list(image.getdata())

    pixel_data = [f"({pixel[0]},{pixel[1]},{pixel[2]})" for pixel in pixels]

    with open(output_file, 'w') as file:
        file.write(';'.join(pixel_data))

    print(f"Données des pixels enregistrées dans '{output_file}' avec succès.")

image_path = "open.jpg"

output_file = "pixels.txt"

save_image_to_pixel(image_path, output_file)