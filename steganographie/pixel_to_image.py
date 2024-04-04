from PIL import Image

def create_image_from_pixels(pixels_file, output_image_path, image_size):
    with open(pixels_file, 'r') as file:
        pixel_data = file.read()

    pixels = []
    for line in pixel_data.split(';'):
        r, g, b = map(int, line.strip('()\n ').split(','))
        pixels.append((r, g, b))

    image = Image.new('RGB', image_size)
    image.putdata(pixels)
    image.save(output_image_path)
    print(f"Image créée et enregistrée dans '{output_image_path}' avec succès.")

pixels_file = "pixels.txt"

image_size = (283, 329)

output_image_path = "reconstructed_image.png"

create_image_from_pixels(pixels_file, output_image_path, image_size)