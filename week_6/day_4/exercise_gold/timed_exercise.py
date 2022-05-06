#Write a program to reverse the sentence wordwise.
sentence=input('Please enter a sentence: ')
words=sentence.split(' ')
words_reverse= reversed(words)
sentence_reverse= ' '.join(words_reverse)
print(sentence_reverse)