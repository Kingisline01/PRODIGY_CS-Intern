from PIL import Image
import numpy as np

def encrypt_image(image_path, key):
    # Open the image
    image = Image.open(image_path)
    image_array = np.array(image)
    
    # Convert the key to a binary format
    key_bin = ''.join(format(ord(char), '08b') for char in key)
    
    # Encrypt the image
    encrypted_array = image_array.copy()
    key_len = len(key_bin)
    
    for i in range(encrypted_array.shape[0]):
        for j in range(encrypted_array.shape[1]):
            for k in range(encrypted_array.shape[2]):
                pixel_bin = format(encrypted_array[i, j, k], '08b')
                encrypted_bin = ''.join(str(int(pixel_bin[l]) ^ int(key_bin[(i + j + l) % key_len])) for l in range(8))
                encrypted_array[i, j, k] = int(encrypted_bin, 2)
    
    encrypted_image = Image.fromarray(encrypted_array)
    return encrypted_image

def decrypt_image(image, key):
    # Convert the image to a numpy array
    image_array = np.array(image)
    
    # Convert the key to a binary format
    key_bin = ''.join(format(ord(char), '08b') for char in key)
    
    # Decrypt the image
    decrypted_array = image_array.copy()
    key_len = len(key_bin)
    
    for i in range(decrypted_array.shape[0]):
        for j in range(decrypted_array.shape[1]):
            for k in range(decrypted_array.shape[2]):
                pixel_bin = format(decrypted_array[i, j, k], '08b')
                decrypted_bin = ''.join(str(int(pixel_bin[l]) ^ int(key_bin[(i + j + l) % key_len])) for l in range(8))
                decrypted_array[i, j, k] = int(decrypted_bin, 2)
    
    decrypted_image = Image.fromarray(decrypted_array)
    return decrypted_image

# Example usage
if __name__ == "__main__":
    key = "key"
    image_path = "Images/Gwen.jpg"  # Replace with your image path

    # Encrypt the image
    encrypted_image = encrypt_image(image_path, key)
    encrypted_image.save("Output/Encodes/encrypted_image.png")

    # Decrypt the image
    decrypted_image = decrypt_image(encrypted_image, key)
    decrypted_image.save("Output/Decodes/decrypted_image.png")
