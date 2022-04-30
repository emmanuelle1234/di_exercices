# #Daily challenge
#ord() returns the unicode of a character. For example, ord('a') returns 97
#chr() returns
import random

choice = input("Do you want encryption or decryption of a text ? Please enter either encryption or decryption : ")
if choice == "encryption":
    text=input("Please enter a message to encrypt: ")
    #Encryption with a random shift - We could have asked the user for a given shift
    shift = random.randint(1,25)
    cypher_text=""
    print(f"Your secret shift is {shift}")
    letter=""
    for letter in text:
        letter_number = ord(letter) + shift
        if letter =="," or letter ==" " or letter =="'": #Could add other special characters we want to keep as they are
            cypher_text += letter
        else:
            if ((96 < letter_number < 123) and (96 < ord(letter) < 123)) or ((64 < letter_number < 91) and (64 < ord(letter) < 91)):
                cypher_text += chr(letter_number)
            else:
                cypher_text += chr(letter_number - 26)
    print(cypher_text)

elif choice == "decryption":
    text=""
    cypher_text=input("Please enter a message to decypher: ")
    shift = input("Please enter the secret shift (a number between 1 and 25) : ")
    for letter in cypher_text:
        letter_number = ord(letter) - int(shift)
        if letter == "," or letter == " " or letter == "'":
            text += letter
        else:
            if ((96 < letter_number < 123) and (96 < ord(letter) < 123)) or ((64 < letter_number < 91) and (64 < ord(letter) < 91)):
                text += chr(letter_number)
            else:
                text += chr(letter_number + 26)
    print(text)

else:
    print("I do not understand what you want.")