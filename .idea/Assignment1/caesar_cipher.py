#Caesar Cipher: Custom Encryption-Decryption
# Caesar Cipher Implementation

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            # Shift letters
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            # Keep special characters as-is
            result += char
    return result

def decrypt(cipher, shift):
    return encrypt(cipher, -shift)

# Example usage
message = input("Enter your message: ")
key = int(input("Enter shift key (e.g., 3): "))

encrypted = encrypt(message, key)
decrypted = decrypt(encrypted, key)

print("Encrypted message:", encrypted)
print("Decrypted message:", decrypted)
