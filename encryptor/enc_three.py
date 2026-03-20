import random
random.seed(None)

def encrypt(message, key=None, rand_min=1, rand_max=255):
    random.seed(None)
    and_key = False
    if key is None:
        key = random.randint(rand_min, rand_max)
        and_key = True
    random.seed(key)
    enc = ''
    for i in message:
        enc += chr(ord(i) ^ random.randint(rand_min, rand_max))
    if and_key:
        return enc, key
    return enc

def decrypt(message, key, rand_min=1, rand_max=255):
    random.seed(key)
    enc = ''
    for i in message:
        enc += chr(ord(i) ^ random.randint(rand_min, rand_max))
    return enc