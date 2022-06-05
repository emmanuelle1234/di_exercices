import anagram_checker
import re


def is_word_valid (word):
    word_list = list(word)
    if word_list[0] ==' ':
        word = word[1:]
    if word_list[len(word_list)-1] ==' ':
        word = word[0:len(word)-1]
    only_one_word = word.split(" ")
    if len(only_one_word) != 1:
        is_valid = False
    else:
        pattern = re.compile(r'[A-Za-z]+')
        if not re.fullmatch(pattern, word):
            is_valid = False
        else:
            is_valid = True
    return is_valid


def show_menu():
    not_yet_answer = True
    while not_yet_answer:
        answer = input("""
        ANAGRAM CHECKER - MENU
        **********************
        1. Input a word to check if there is an anagram
        2. Quit
        **********************
        
        Please enter your choice: """)
        if answer == '1':
            word = input("\n        Please enter a word: ")
            if is_word_valid(word):
                a = anagram_checker.AnagramChecker()
                if a.is_english_word(word):
                    if len(a.get_anagrams(word)) != 0:
                        print(f"""
        YOUR WORD: {word}
        This is a valid English word.
        Anagrams for your word: {", ".join(a.get_anagrams(word))}.
                """)
                        break
                    else:
                        print(f"""
        YOUR WORD: {word}
        This is a valid English word.
        There is no english anagram for your word.
                """)
                        break
                else:
                    print(f"""
        YOUR WORD: {word}
        This is not a valid English word.
                """)
                    break
            else:
                print('        A single word is required.')
        elif answer == '2':
            break
        else:
            print('        This is not a valid choice.')


show_menu()













