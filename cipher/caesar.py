with open('cryptography_caesar_input.txt', 'r') as file:
    encrypted = file.read().replace('\n', '').replace(' ', '')

alphabet = '+-*0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for char in range(len(alphabet)):
    
    decrypted = ''

    for eChar in encrypted:
        num = alphabet.index(eChar)
        num = num - char
        if num < 0:
            num += len(alphabet)
        decrypted += alphabet[num]
    print(f'key #{char}: {decrypted}')
