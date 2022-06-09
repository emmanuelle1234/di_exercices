import itertools


class AnagramChecker:

    def __init__(self):
        with open('text.txt', 'r') as words_file:
            self.words_list = [] # you define it twice, please remove
            self.words_list = [word.replace('\n', '') for word in words_file.readlines()]

    def is_english_word(self, word):
        if word.upper() in self.words_list: # just replace with return word.upper() in self.words_list
            return True
        else:
            return False

    def is_anagram(self, word1, word2):
        # the same replace with one line
        if sorted(word1) == sorted(word2):  # alternative solution to be thought with permutations in itertools?
            return True
        else:
            return False

    def get_anagrams(self, word):
        # the var is redandant
        anagrams = [item.lower() for item in self.words_list if self.is_anagram(item, word.upper()) and item != word.upper()]
        return anagrams


# TESTING

"""
a = AnagramChecker()
print(a.words_list)
print(a.is_valid_word('word'))
print(a.is_anagram('team', 'meet'))
print(a.is_anagram('team', 'meat'))
print(a.get_anagrams('team'))
print(a.get_anagrams('TEAM'))"""
