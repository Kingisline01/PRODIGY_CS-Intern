def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            shifted_char = ord(char) + shift_amount
            if char.islower():
                if shifted_char > ord('z'):
                    shifted_char -= 26
                encrypted_text += chr(shifted_char)
            elif char.isupper():
                if shifted_char > ord('Z'):
                    shifted_char -= 26
                encrypted_text += chr(shifted_char)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            shifted_char = ord(char) - shift_amount
            if char.islower():
                if shifted_char < ord('a'):
                    shifted_char += 26
                decrypted_text += chr(shifted_char)
            elif char.isupper():
                if shifted_char < ord('A'):
                    shifted_char += 26
                decrypted_text += chr(shifted_char)
        else:
            decrypted_text += char
    return decrypted_text

def main():
    print("Caesar Cipher Program")
    choice = input("Would you like to (e)ncrypt or (d)ecrypt a message? ")
    if choice.lower() not in ['e', 'd']:
        print("Invalid choice. Please choose 'e' for encryption or 'd' for decryption.")
        return

    message = input("Enter your message: ")
    shift = int(input("Enter the shift value: "))

    if choice.lower() == 'e':
        encrypted_message = caesar_cipher_encrypt(message, shift)
        print(f"Encrypted Message: {encrypted_message}")
    elif choice.lower() == 'd':
        decrypted_message = caesar_cipher_decrypt(message, shift)
        print(f"Decrypted Message: {decrypted_message}")

if __name__ == "__main__":
    main()
