from encryptor import Encryptor
from decryptor import Decryptor

cifra = [
    [
        'L', 'N', 'A', 'M', 'U'
    ],
    [
        'O', 'D', 'B', 'C', 'E'
    ],
    [
        'F', 'G', 'H', 'I', 'K'
    ],
    [
        'P', 'Q', 'R', 'S', 'T'
    ],
    [
        'V', 'W', 'X', 'Y', 'Z'
    ]
]
palavra = 'climax'

a = Encryptor(cifra).encrypt(input())
print(a)
print(Decryptor(cifra).decrypt(a))
