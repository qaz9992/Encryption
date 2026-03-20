import random

def encrypt(message, seed_list: list=None, rand_min=1, rand_max=255):
    random.seed(None)
    and_key = False
    if seed_list is None:
        and_key = True
        seed_list = [random.randint(rand_min, rand_max) for _ in range(len(message))]
    if len(seed_list) != len(message):
        raise ValueError("Seed list must be the same length as the message.")
    enc = ''
    index = 0
    for i in message:
        random.seed(seed_list[index])
        enc += chr(ord(i) ^ random.randint(rand_min, rand_max))
        index += 1
    if and_key:
        return enc, seed_list
    return enc

def decrypt(message, seed_list: list, rand_min=1, rand_max=255):
    if len(seed_list) != len(message):
        raise ValueError("Seed list must be the same length as the message.")
    enc = ''
    index = 0
    for i in message:
        random.seed(seed_list[index])
        enc += chr(ord(i) ^ random.randint(rand_min, rand_max))
        index += 1
    return enc

if __name__ == "__main__":
    message = "Hello, World!"
    encrypted_message, seed_list = encrypt(message)
    print(f"Encrypted: {encrypted_message}")
    decrypted_message = decrypt(encrypted_message, seed_list)
    print(f"Decrypted: {decrypted_message}")