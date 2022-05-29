from translator import translate_french_to_english


def translate_french_to_english_list(list):
    translated_list = [translate_french_to_english(word) for word in list]
    result_dict = {list[i]: translated_list[i] for i in range(len(list))}
    return result_dict


french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]
print(translate_french_to_english_list(french_words))
