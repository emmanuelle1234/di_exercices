french_list = ["A bientôt", "Au revoir", "Bienvenue", "Bonjour", "Client", "Entreprise", "Usine"]
english_list = ["Company", "Customer", "Factory", "Goodbye", "Hello", "See you soon", "Welcome"]
fe_translation = [[0,5], [1, 3], [2, 6], [3, 4], [4, 1], [5, 0], [6, 2]]
ef_translation = sorted([[b, a] for [a, b] in fe_translation])

def translate_french_to_english(word):
    for i in range(len(french_list)):
        if word == french_list[i]:
            translated_word = english_list[fe_translation[i][1]]
            # print(translated_word)
            return translated_word

def translate_english_to_french(word):
    for i in range(len(english_list)):
        if word == english_list[i]:
            translated_word = french_list[ef_translation[i][1]]
            # print(translated_word)
            return translated_word


# TESTING
"""translate_french_to_english("Bienvenue")
translate_french_to_english("Client")
translate_english_to_french("Goodbye")
translate_english_to_french("See you soon")"""
