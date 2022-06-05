# EXERCISE 1

import random


def get_words_from_file():
    with open('words.txt', mode='r') as my_file:
        words_list = [word.replace('\n', '') for word in my_file.readlines()]
    return words_list


def get_random_sentence(length):
    words_for_sentence = []
    for i in range(0, length):
        word = random.choice(get_words_from_file()).lower()
        words_for_sentence.append(word)
    return words_for_sentence


def create_sentence(words_for_sentence):
    sentence = " ".join(words_for_sentence)+"."
    return sentence

    # not clear what is asked to create a sentence
    # would a pipy module allow something which looks like more a sentence?


def main():
    print("""
This program creates a random sentence generator.
You have to decide how long the sentence is.
The sentence should include at least 2 words and not exceed 20 words.\n """)
    not_yet_answered = True
    while not_yet_answered:
        length = int(input("Dear user, how long do you want the sentence to be (between 2 and 20): "))
        if 1 < length < 21:
            print(create_sentence(get_random_sentence(length)).capitalize())
            not_yet_answered = False
        else:
            print('This is not a valid choice.')
            break


main()


print('\n')
# EXERCISE 2

import json  # should be at the beginning

sampleJson = {
    "company": {
        "employee": {
            "name": "emma",
            "payable": {
                "salary": 7000,
                "bonus": 800
            }
        }
    }
}

salary = sampleJson["company"]["employee"]["payable"]["salary"]
sampleJson["company"]["employee"]["birth_date"] = "1991/12/30"
print(f'{sampleJson["company"]["employee"]["name"].capitalize()}, whose salary is {salary}, is born on {sampleJson["company"]["employee"]["birth_date"]}.')

with open('dictionary.json', mode='w') as file:
    json.dump(sampleJson, file)
