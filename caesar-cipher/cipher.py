import string

def caesar_cipher(plaintext, key, action):
    # convert plaintext to uppercase
    plaintext = plaintext.upper()
    
    # remove spaces
    plaintext = plaintext.replace(" ", "")
    
    # convert fullstop to "X"
    plaintext = plaintext.replace(".", "X")
    
    # create a list to store the ciphertext
    ciphertext = []
    
    # loop through each character in the plaintext
    for char in plaintext:
        # check if the character is a letter
        if char in string.ascii_uppercase:
            if action == "encrypt":
                shifted = (ord(char) + key - ord('A')) % 26 + ord('A')
            elif action == "decrypt":
                shifted = (ord(char) - key - ord('A')) % 26 + ord('A')
            cipher_char = chr(shifted)
            # add the encrypted letter to the ciphertext list
            ciphertext.append(cipher_char)
        else:
            # if the character is not a letter, add it to the ciphertext list without encrypting
            ciphertext.append(char)
    
    # join the list of characters back into a string
    if action == "encrypt":
        ciphertext = ''.join(ciphertext)
        return ciphertext
    elif action == "decrypt":
        plaintext = ''.join(ciphertext)
        return plaintext

# begin while loop
while True:
    # ask user what they want to do
    action = input("Do you want to encrypt, decrypt or quit? (e/d/q) ")
    # if user chooses to encrypt;
    if action.lower() == "encrypt" or action.lower() == "e":
        action = "encrypt"
        plaintext = input("Enter encrypted string: ")
        # this checks for special characters, prints an error if found
        invalid_input = False
        for i in plaintext:
            if i not in string.ascii_letters and i not in string.whitespace:
                invalid_input = True
                break
        if invalid_input:
            print("Invalid input. We hate $#^!&*%! words!.")
            continue
        # set the char offset
        key = 3
        ciphertext = caesar_cipher(plaintext, key, action)
        # output to user the complete offset string
        print("Encrypted text: ", ciphertext)

    # if user chose to decrypt;    
    elif action.lower() == "decrypt" or action.lower() == "d":
        action = "decrypt"
        plaintext = input("Enter decrypted string: ")
        invalid_input = False
        for i in plaintext:
            if i not in string.ascii_letters and i not in string.whitespace:
                invalid_input = True
                break
        if invalid_input:
            print("Invalid input. We hate $#^!&*%! words!.")
            continue
        key = 3
        ciphertext = caesar_cipher(plaintext, key, action)
        print("Decrypted text: ", ciphertext)
    # if user chose to quit;    
    elif action.lower() == "q" or action.lower() == "quit":
        print("Exiting program")
        break
    else:
        print("Invalid action. Please enter 'encrypt', 'decrypt' or 'q'. You may also enter e/d/q")