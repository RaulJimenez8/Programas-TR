letters = 'abcdefghijklmnopqrstuvwxyz'
num_letters = len(letters)

def decrypt_with_key(ciphertext, key): 
    plaintext = ''
    for letter in ciphertext: 
        letter = letter.lower() 
        if letter in letters:
            index = letters.find(letter)
            new_index = (index - key) % num_letters
            plaintext += letters[new_index]
        else:
            plaintext += letter
    return plaintext

print()
print('*** CAESAR CIPHER PROGRAM ***') 
print()

ciphertext = input('Enter the encrypted text: ')
print("\nAll possible Caesar cipher decryptions:\n")

for key in range(1, num_letters + 1):
    plaintext = decrypt_with_key(ciphertext, key)
    print(f'Key {key}: {plaintext}')
