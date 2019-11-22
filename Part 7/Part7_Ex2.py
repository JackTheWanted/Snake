#Jack C
def encrypt():
    encrypted_text = ''
    entered_text = input('Please input the text you want to encrypt:')
    for c in entered_text:
        x = ord(c)
        x = x + 1
        c2 = chr(x)
        encrypted_text = encrypted_text + c2
    print('Encrypted Text:', encrypted_text)
    return encrypted_text



def decrypt(encrypted_text):
    entered_text = ''
    for c in encrypted_text:
        x = ord(c)
        x = x - 1
        c2 = chr(x)
        entered_text = entered_text + c2
    print('Decrypted Text:', entered_text)
    return entered_text


encrypted_text = encrypt()

decrypt(encrypted_text)
