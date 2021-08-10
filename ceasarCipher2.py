alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt and 'decode' to decrpyt \n")
text = input ("Enter the text: \n")
loweredText = text.lower()
shift = int(input("Enter the shift number: \n"))

def encrypt(plainText, shiftNumber):
    cipherText = ""
    for letter in plainText:
        position = alphabet.index(letter)
        newPosition = position + shiftNumber
        cipherText += alphabet[newPosition]
    print(f"The encoded text is : {cipherText} \n")



def decrypt(decryptText, shiftnumber):
    decodedText = ""
    for letter in decryptText:
        position = alphabet.index(letter)
        new_position = position - shiftnumber
        decodedText += alphabet[new_position]
    print(f"The decoded text is {decodedText}")


if direction == "encode":

    encrypt(plainText=text,shiftNumber=shift)
else:
    decrypt(decryptText=text,shiftnumber=shift)