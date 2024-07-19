from PIL import Image
import random

def encrypt_image(input_image_path, output_image_path, key):
    image = Image.open(input_image_path)
    pixels = list(image.getdata())
    width, height = image.size

    random.seed(key)
    random.shuffle(pixels)

    encrypted_image = Image.new(image.mode, image.size)
    encrypted_image.putdata(pixels)
    encrypted_image.save(output_image_path)
    print(f"Image encrypted and saved to {output_image_path}")

def decrypt_image(encrypted_image_path, output_image_path, key):
    image = Image.open(encrypted_image_path)
    pixels = list(image.getdata())
    width, height = image.size

    random.seed(key)
    indices = list(range(len(pixels)))
    random.shuffle(indices)

    decrypted_pixels = [None] * len(pixels)
    for i, idx in enumerate(indices):
        decrypted_pixels[idx] = pixels[i]

    decrypted_image = Image.new(image.mode, image.size)
    decrypted_image.putdata(decrypted_pixels)
    decrypted_image.save(output_image_path)
    print(f"Image decrypted and saved to {output_image_path}")

def main():
    print("Image Encryption and Decryption Tool")
    choice = input("Would you like to (e)ncrypt or (d)ecrypt an image? ").lower()
    if choice not in ['e', 'd']:
        print("Invalid choice. Please choose 'e' for encryption or 'd' for decryption.")
        return

    # input_image_path = input("Enter the path to the input image: ")
    # input_image_path = "D:\SHIP\prodigy\Projects\Pixel Manipulation for Image Encryption\Images/fugaku.png"

    # when using decoder
    input_image_path = "D:\SHIP\prodigy\Projects\Pixel Manipulation for Image Encryption\Output\Decodes/fugaku.png"


    # output_image_path = input("Enter the path to save the output image: ")
    # output_image_path = "D:\SHIP\prodigy\Projects\Pixel Manipulation for Image Encryption\Output\Decodes/fugaku.png"

     # when using decoder
    output_image_path = "D:\SHIP\prodigy\Projects\Pixel Manipulation for Image Encryption\Output\Encodes/fugaku.png"

    key = int(input("Enter the encryption/decryption key: "))

    if choice == 'e':
        encrypt_image(input_image_path, output_image_path, key)
    elif choice == 'd':
        decrypt_image(input_image_path, output_image_path, key)

if __name__ == "__main__":
    main()
