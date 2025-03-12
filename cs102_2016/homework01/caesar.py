#print(ord("a")) #97
#print(ord("z")) #122
#print(ord("A")) #65
#print(ord("Z")) #90

def encrypt_caesar(plaintext):
    ciphertext = ""
    for i in range(len(plaintext)):
        if(97 <= ord(plaintext[i]) <= 122):
            ciphertext += chr(97 + (ord(plaintext[i]) - 97 + 3) % 26)
        elif(65 <= ord(plaintext[i]) <= 90):
            ciphertext += chr(65 + (ord(plaintext[i]) - 65 + 3) % 26)
        else:
            ciphertext += plaintext[i]
    """
    Encrypts plaintext using a Caesar cipher.
(
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    # PUT YOUR CODE HERE
    return ciphertext


def decrypt_caesar(ciphertext):
    plaintext = ""
    for i in range(len(ciphertext)):
        if (97 <= ord(ciphertext[i]) <= 122):
            plaintext += chr(97 + (ord(ciphertext[i]) - 97 - 3 + 26) % 26)
        elif (65 <= ord(ciphertext[i]) <= 90):
            plaintext += chr(65 + (ord(ciphertext[i]) - 65 - 3 + 26) % 26)
        else:
            plaintext += ciphertext[i]
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    # PUT YOUR CODE HERE
    return plaintext

print(decrypt_caesar("Sbwkrq3.6"))
