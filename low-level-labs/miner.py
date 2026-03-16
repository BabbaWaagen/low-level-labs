import hashlib

block = "example block data"

nonce = 0

difficulty = 4

prefix = "0"*difficulty

while True:

    text = block + str(nonce)

    hash = hashlib.sha256(text.encode()).hexdigest()

    if hash.startswith(prefix):
        print("Found!")
        print("Nonce:",nonce)
        print("Hash:",hash)
        break

    nonce += 1
