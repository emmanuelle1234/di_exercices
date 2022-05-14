# WEEK 7 DAY 5 MINI-PROJECT
import random

board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]
         ]
username = ""
players = [{'player': 1, 'username': '', 'mark': '', 'turn': False},
           {'player': 2, 'username': '', 'mark': '', 'turn': False}]


def display_board(board):
    print('*' * 17)
    for i in range(2):
        print(f'*{" " * 3}{board[i][0]} | {board[i][1]} |  {board[i][2]}  *')
        print(f'*  {"-" * 3}|{"-" * 3}|{"-" * 3}  *')
    print(f'*{" " * 3}{board[2][0]} | {board[2][1]} |  {board[2][2]}  *')
    print('*' * 17)


def start_the_game():
    print('Let\'s start the famous Tic Tac Toe game. Two players are needed.')
    players[0]['username'] = input('Dear first player, please input your username: ')
    players[1]['username'] = input('Dear second player, please input your username: ')
    print('Let\'s see who is starting.')
    starting_player_number = random.randint(1, 2)
    starting_player_name = ""
    for i in range(0, 2):
        if players[i]['player'] == starting_player_number:
            players[i]['turn'] = True
            players[i]['mark'] = 'X'
            starting_player_name = players[i]['username']
        else:
            players[i]['mark'] = 'O'
    player = starting_player_name
    return player


def player_input(player):
    cell_string = input(f'Hi {player}, it\'s your turn. Please enter row and column (row, column): ')
    try:
        cell = list(cell_string.replace(" ", "").split(","))
        cell = [int(cell[0]), int(cell[1])]
    except:
        print('Please follow the recommended format')
        cell = [0, 0]
        player_play(player)
    return cell


def change_player(player):
    for i in range(0, 2):
        if players[i]['turn']:
            players[i]['turn'] = False
        else:
            players[i]['turn'] = True
    for i in range(0, 2):
        if players[i]['turn']:
            player = players[i]['username']
    return player


def player_play(player):
    cell = player_input(player)
    if check_not_filled(cell):
        for i in range(0, 2):
            if players[i]['username'] == player:
                board[cell[0]-1][cell[1]-1] = players[i]['mark']
                display_board(board)
    else:
        print("This cell is not empty")
        player_play(player)
    return board


def check_not_win():
    not_win = True
    for i in range(2):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            not_win = False
            break
        elif board[0][i] == board[1][i] == board[2][i] != " ":
            not_win = False
            break
        else:
            not_win = True
    if board[0][0] == board[1][1] == board[2][2] != " ":
        not_win = False
    if board[2][0] == board[1][1] == board[0][2] != " ":
        not_win = False
    return not_win


def check_not_filled(cell):
    not_filled = False
    if board[cell[0]-1][cell[1]-1] == " ":
        not_filled = True
    return not_filled


def check_board_not_filled():
    board_not_filled = False
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board_not_filled = True
                break
        if board_not_filled:
            break
    return board_not_filled


def play_the_game():
    print('TIC TAC TOE')
    display_board(board)
    not_win = True
    board_not_filled = True
    player = start_the_game()
    while board_not_filled or not_win:
        player_play(player)
        not_win = check_not_win()
        if not not_win:
            winner = player
            print(f"Congratulations to {winner}!")
            break
        board_not_filled = check_board_not_filled()
        print(board_not_filled)
        if not board_not_filled:
            print(f"No winner! Perhaps could you play again?")
            break
        player = change_player(player)


play_the_game()
