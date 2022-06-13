# Exercise 1 : What’s Your Name ?


def get_full_name(first_name: str, middle_name="", last_name=""):
    name = f'{first_name} {middle_name+" "}{last_name}'
    return name


print(get_full_name('Bruce', 'Lee'))
print(get_full_name('Bruce', 'Junior', 'Lee'))


# Exercise 2 :

ENGLISH_TO_MORSE = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    " ": "SPACE", # to simplify the code later on
}

MORSE_TO_ENGLISH_ = {value: key for key, value in ENGLISH_TO_MORSE.items()}



def translate_to_morse(text):
    morse = " ".join(ENGLISH_TO_MORSE[letter] for letter in text)
    morse = morse.replace(" SPACE ", "   ")
    return morse


def translate_from_morse(morse):
    signs = morse.replace("   ", " SPACE ").split(" ")
    translated_morse = "".join(MORSE_TO_ENGLISH_[item] for item in signs)
    return translated_morse


def translate(starting_language, message):
    if starting_language == 'english':
        return translate_to_morse(message.upper())
    elif starting_language == 'morse':
        return translate_from_morse(message).capitalize()
    else:
        return 'input should be either english or morse'


print(translate('english', 'Hello World'))
print(translate('morse', '.... . .-.. .-.. ---   .-- --- .-. .-.. -..'))




