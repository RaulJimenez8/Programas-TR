import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

p = 3
q = 7
n = p * q
fi = (p - 1) * (q - 1)

e = 2
while gcd(e, fi) != 1:
    e += 1

k = 2
d = (1 + (k * fi)) // e

message = 12
print("Original Message:", message)

c = pow(message, e, n)
print("Encrypted Message:", c)

m = pow(c, d, n)
print("Decrypted Message:", m)
