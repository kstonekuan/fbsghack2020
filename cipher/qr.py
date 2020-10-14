with open('cryptography_quick_response_sample_input.txt', 'r') as file:
    encrypted = file.read().replace('\n', ' ').split(' ')

alphabet = '+-*0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def binaryToDecimal(n): 
    return int(n,2) 

for i in range(len(encrypted)):
    # print(char)
    print(alphabet[binaryToDecimal(encrypted[i]) + binaryToDecimal(encrypted[i+1])])
