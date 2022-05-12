# WEEK 7 DAY 5 MINIPROJECT
import random
from random import randint

def display_board() :
    print('TOC TACT TOE')
    print('*'*17)
    for i in range(2):
        print(f'*{" " * 5}|{" " * 3}|{" " * 5}*')
        print(f'*  {"-" * 3}|{"-" * 3}|{"-" * 3}  *')
    print(f'*{" " * 5}|{" " * 3}|{" " * 5}*')
    print('*' * 17)

username=""
players = [{'player': 1, 'username': '', 'turn': False},{'player': 2, 'username': '', 'turn': False}]

def start_the_game():
    print('Let\'s start the famous Tic Tac Toe game. Two players are needed.')
    players[0]['username'] = input('Dear first player, please input your username: ')
    players[1]['username'] = input('Dear second player, please input your username: ')
    print('Let\'s see who will start the game.')
    starting_player_number = random.randint(1, 2)
    starting_player_name=""
    for i in range(0, 2):
        if players[i]['player'] == starting_player_number:
            players[i]['turn'] = True
            print(players)
            starting_player_name = players[i]['username']
            print(i)
            print(f'Dear {starting_player_name}, it\'s up to you')
    return starting_player_name

start_the_game()


"""def player_turn()
    # Show the updated board
    # Select the position in empty squares def player_input(player)
    # Choose the mark
    # Update the board
    # Check if the game is won

def change_player()

def check_win()
    return player_number

def play_the_game()
    display_board()
    start_the_game()
    #loop play until the game is won
    #congrat the winner"""

# To test step by step
display_board()


