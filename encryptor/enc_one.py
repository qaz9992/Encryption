def encrypt(message, key):
    encrypted = ""
    for char in message:
        if char.isalpha():
            shifted = (ord(char) - ord('a') + key) % 26
            encrypted += chr(shifted + ord('a'))
        else:
            encrypted += char
    return encrypted

def decrypt(encrypted_message, key):
    decrypted = ""
    for char in encrypted_message:
        if char.isalpha():
            shifted = (ord(char) - ord('a') - key) % 26
            decrypted += chr(shifted + ord('a'))
        else:
            decrypted += char
    return decrypted
