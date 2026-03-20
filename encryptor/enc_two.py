def encrypt(text, key):
    enc = ''
    for i in text:
        enc += chr(ord(i) ^ key)
    return enc

def decrypt(text, key):
    enc = ''
    for i in text:
        enc += chr(ord(i) ^ key)
    return enc

if __name__ == "__main__":
    message = "Hello, World!"
    key = 123
    encrypted_message = encrypt(message, key)
    print(f"Encrypted: {encrypted_message}")
    decrypted_message = decrypt(encrypted_message, key)
    print(f"Decrypted: {decrypted_message}")