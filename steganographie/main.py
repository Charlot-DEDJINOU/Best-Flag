import argparse
import image_steganography

def main():
    parser = argparse.ArgumentParser(description='Hide or extract data in/from images and perform text processing.')
    parser.add_argument('-a', '--action', type=str, choices=['hide_image', 'extract_hidden_image', 'hide_text', 'extract_text', 'image_to_pixel', 'image_to_bits', 'image_from_bits', 'image_from_pixels', 'save_binary_to_text', 'save_text_to_binary'], help='Action to perform')
    parser.add_argument('-t', '--text', type=str, help='Input file text path')
    parser.add_argument('-sh', '--image_to_hide', type=str, help='Input file path (image to hide)')
    parser.add_argument('-th', '--host_image', type=str, help='Input file path (host image)')
    parser.add_argument('-o', '--output', type=str, help='Output file path')
    
    args = parser.parse_args()

    if args.action == 'hide_image':
        image_steganography.hide_image(args.image_to_hide, args.host_image, args.output)
    elif args.action == 'extract_hidden_image':
        image_steganography.extract_hidden_image(args.host_image, args.output)
    elif args.action == 'hide_text':
        image_steganography.hide_text(args.text, args.host_image, args.output)
    elif args.action == 'extract_text':
        image_steganography.extract_text(args.host_image, args.output)
    else:
        print('Error: Invalid function or action.')

if __name__ == '__main__':
    main()
