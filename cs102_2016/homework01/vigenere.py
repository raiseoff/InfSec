def encrypt_vigenere(plaintext, keyword):
    keyword = keyword * (len(plaintext)//len(keyword)+1)
    ciphertext = ""
    for i in range(len(plaintext)):
        if (97 <= ord(plaintext[i]) <= 122):
            ciphertext += chr(97 + (ord(plaintext[i]) - 97 + (ord(keyword[i]) - 97)) % 26)
        elif (65 <= ord(plaintext[i]) <= 90):
            ciphertext += chr(65 + (ord(plaintext[i]) - 65 + (ord(keyword[i]) - 65)) % 26)
        else:
            ciphertext += plaintext[i]
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    # PUT YOUR CODE HERE
    return ciphertext


def decrypt_vigenere(ciphertext, keyword):
    keyword = keyword * (len(ciphertext)//len(keyword)+1)
    plaintext = ""
    for i in range(len(ciphertext)):
        if (97 <= ord(ciphertext[i]) <= 122):
            plaintext += chr(97 + (ord(ciphertext[i]) - 97 - (ord(keyword[i]) - 97) + 26) % 26)
        elif (65 <= ord(ciphertext[i]) <= 90):
            plaintext += chr(65 + (ord(ciphertext[i]) - 65 - (ord(keyword[i]) - 65) + 26) % 26)
        else:
            plaintext += ciphertext[i]
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    # PUT YOUR CODE HERE
    return plaintext


print(encrypt_vigenere("python", "a"))