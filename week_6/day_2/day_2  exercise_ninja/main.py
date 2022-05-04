# Exercises Ninja

#Exercise3
3 <= 3 < 9#True
3 == 3 == 3#True
bool(0)# False
bool(5 == "5") #False
bool(4 == 4) == bool("4" == "4")#True
bool(bool(None))#False

x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10
print("x is", x) #x is True
print("y is", y) #x is False
print("a:", a) # a: 5
print("b:", b) # b:10

#Exercise4
my_text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, \
           sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. \
           Ut enim ad minim veniam, quis nostrud exercitation ullamco \
           laboris nisi ut aliquip ex ea commodo consequat. \
           Duis aute irure dolor in reprehenderit in voluptate velit \
           esse cillum dolore eu fugiat nulla pariatur. \
           Excepteur sint occaecat cupidatat non proident, \
           sunt in culpa qui officia deserunt mollit anim id est laborum.'
print(len(my_text.replace(" ", "").replace(".", "").replace(",", "")))

#Exercise5
"""Instructions
1. Keep asking the user to input the longest sentence they can without the character “A”.
2. Each time a user successfully sets a new longest sentence, print a congratulations message."""
length = 0
word = input("Please input the longest word you can without the character A: ")
while len(word)>length and "A" not in word:
    print("Congratulations")
    length = len(word)
    print(length)
    word = input("Please input the longest word you can without the character A: ")


