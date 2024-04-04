from PIL import Image

def reconstruct_image_from_pixels(pixels_file, output_image_path, image_size):
    with open(pixels_file, 'r') as file:
        pixel_data = file.read()

    pixels = []
    for i in range(0, len(pixel_data), 24):
        red = int(pixel_data[i:i+8], 2)
        green = int(pixel_data[i+8:i+16], 2)
        blue = int(pixel_data[i+16:i+24], 2)
        pixels.append((red, green, blue))

    image = Image.new('RGB', image_size)
    image.putdata(pixels)
    image.save(output_image_path)
    print("Image reconstituée et enregistrée avec succès.")

image_size = (283, 329)
output_image_path = "reconstructed_image.png"

reconstruct_image_from_pixels("pixels.txt", output_image_path, image_size)