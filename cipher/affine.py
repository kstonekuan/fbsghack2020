with open('cryptography_quick_response_input.txt', 'r') as file:
    encrypted = file.read().replace('\n', '').replace(' ', '')


alphabet = "+-*0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

for a in range(len(alphabet)):
    for b in range(len(alphabet)):
        
        try:
            c = modinv(int(a), len(alphabet))
        except:
            continue

        decrypted = ""

        for eChar in encrypted:
            # print(eChar)
            decrypted += alphabet[c * (alphabet.index(eChar) - int(b)) % len(alphabet)]
            #decrypted += " "
        if decrypted.find("STOP") != -1:
            print(decrypted)