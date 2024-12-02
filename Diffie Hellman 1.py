def modular_exponent(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent >> 1
        base = (base * base) % modulus
    return result

def diffie_hellman_exchange():
    P = 23
    G = 9
    print("The value of P (public modulus):", P)
    print("The value of G (public base):", G)

    ana_private = 4
    josep_private = 3
    print("Private key for Ana:", ana_private)
    print("Private key for Josep:", josep_private)

    ana_public = modular_exponent(G, ana_private, P)
    josep_public = modular_exponent(G, josep_private, P)
    print("Public key for Ana:", ana_public)
    print("Public key for Josep:", josep_public)

    ana_shared_secret = modular_exponent(josep_public, ana_private, P)
    josep_shared_secret = modular_exponent(ana_public, josep_private, P)

    print("Shared secret for Ana:", ana_shared_secret)
    print("Shared secret for Josep:", josep_shared_secret)

if __name__ == "__main__":
    diffie_hellman_exchange()
