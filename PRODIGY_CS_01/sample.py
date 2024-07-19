def caesar_cipher_encrypt(text_file, shift):
    """Encrypts text from a file and writes the result to a new file."""
    with open(text_file, 'r') as f:
        message = f.read()
    encrypted_text = caesar_cipher_encrypt(message, shift)

    # Create a new filename for the encrypted text
    encrypted_filename = f"{text_file[:-4]}_encrypted.txt"  # Remove ".txt" extension
    with open(encrypted_filename, 'w') as f:
        f.write(encrypted_text)

def caesar_cipher_decrypt(text_file, shift):
    """Decrypts text from a file and writes the result to a new file."""
    with open(text_file, 'r') as f:
        message = f.read()
    decrypted_text = caesar_cipher_decrypt(message, shift)

    # Create a new filename for the decrypted text
    decrypted_filename = f"{text_file[:-4]}_decrypted.txt"  # Remove ".txt" extension
    with open(decrypted_filename, 'w') as f:
        f.write(decrypted_text)

def main():
    print("Caesar Cipher Program")
    choice = input("Would you like to (e)ncrypt or (d)ecrypt a message (using a text file)? ")
    if choice.lower() not in ['e', 'd']:
        print("Invalid choice. Please choose 'e' for encryption or 'd' for decryption.")
        return

    text_file = input("Enter the text file name (including extension): ")
    shift = int(input("Enter the shift value: "))

    if choice.lower() == 'e':
        caesar_cipher_encrypt(text_file, shift)
        print(f"Encrypted message written to: {text_file[:-4]}_encrypted.txt")
    elif choice.lower() == 'd':
        caesar_cipher_decrypt(text_file, shift)
        print(f"Decrypted message written to: {text_file[:-4]}_decrypted.txt")

if __name__ == "__main__":
    main()
