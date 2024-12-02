def modular_exponent(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent >> 1
        base = (base * base) % modulus
    return result

def xor_encrypt_decrypt(message, key):
    return ''.join(chr(ord(c) ^ key) for c in message)

def diffie_hellman_exchange():
    P = 23
    G = 9
    ana_private = 4
    josep_private = 3

    ana_public = modular_exponent(G, ana_private, P)
    josep_public = modular_exponent(G, josep_private, P)

    ana_shared_secret = modular_exponent(josep_public, ana_private, P)
    josep_shared_secret = modular_exponent(ana_public, josep_private, P)

    if ana_shared_secret == josep_shared_secret:
        shared_key = ana_shared_secret
        print("Shared secret key:", shared_key)

        message = "Hello, Josep!"
        encrypted_message = xor_encrypt_decrypt(message, shared_key)
        print("Encrypted message:", encrypted_message)

        decrypted_message = xor_encrypt_decrypt(encrypted_message, shared_key)
        print("Decrypted message:", decrypted_message)

if __name__ == "__main__":
    diffie_hellman_exchange()
