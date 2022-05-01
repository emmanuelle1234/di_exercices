# Exercise 1
from random import randint

random_integers_list = [randint(-100, 100) for i in range(0,10)]
print(random_integers_list)

#not clear for me which generated number should be a positive integer and the max of numbers to generated
random_integers_random_list = [randint(50, 100) for i in range(0, randint(0, 100))]
print(random_integers_random_list)

# Exercise 2 and exercise 3

users_dict = {
    'username1': 'password1',
    'username2': 'password2',
    'username3': 'password3'
}
logged_in = {}
while 1 :
    user_input = input('Please enter \"exit\" or \"login\": ')
    if user_input =='exit':
        break
    if user_input == 'login':
        username_input = input('Please enter your username: ')
        if username_input in users_dict.keys():
            password_input = input('Please enter your password: ')
            if password_input == users_dict[username_input]:
                print('You are now logged in')
                logged_in.update({username_input: 1})
                print(logged_in) #just to check
                break
            else:
                print('You cannot login')
                break #not clear what we should do if the password is wrong
        else:
            user_create=input('Would you like to sign up (please enter \"yes\" or \"no\") : ')
            if user_create=='yes':
                username_new = input('Please choose your new username: ')
                while username_new in users_dict.keys():
                    username_new = input('Please choose your new username: ')
                password_new=input('Please choose a password: ')
                users_dict.update({username_new : password_new})
                print(users_dict)#for the pleasure to see an augmented dictionary
                #no break in order to enter the login loop with this new pair of username/password
            else:
                print('OK. Do not hesitate to sign up next time')
                break
