import random


class Game:

    def __init__(self):
        self.list = ['rock', 'paper', 'scissors']

    def get_user_item(self):
        valid_input = False
        while not valid_input:
            user_item = input('Please enter one of the following items "rock", "paper" or "scissors": ')
            try:
                if user_item in self.list:
                    valid_input = True
                    return user_item
                else:
                    raise Exception('invalid_choice')
            except:
                print('This is not a valid choice')

    def get_computer_item(self):
        computer_item = random.choice(self.list)
        return computer_item

    def game_result(self, user_item, computer_item):
        winning_list = [['rock', 'scissors'], ['scissors', 'paper'], ['paper', 'rock']]
        if user_item == computer_item:
            result = 'draw'
        elif [user_item, computer_item] in winning_list:
            result = 'win'
        else:
            result = 'loss'
        return result

    def play_self(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self. game_result(user_item, computer_item)
        print(f'You selected {user_item}.')
        print(f'The computer\'s random choice was {computer_item}.')
        if result == 'draw':
            print(f'You drew!')
        elif result == 'win':
            print(f'You won!')
        else:
            print(f'You lose.')
        return result


def get_user_menu_choice():
    print("""
            1.Play a new game
            2.Show scores
            3.Exit
            """)
    try:
        answer = int(input("What would you like to do? Pleaser enter 1, 2 or 3: "))
        if answer == 1:
            print("Play a new game")
            return answer
        elif answer == 2:
            print("Show scores")
            return answer
        elif answer == 3:
            print("Exit")
            return answer
        else:
            raise Exception('invalid_choice')
    except ValueError:
        print("You should choose between 1, 2 or 3.")
    except:
        print('This is not a valid choice.')


def print_results(results):
    print(f'Dear user, thank you for playing.')
    print(f'Let us share with you your results : {results}')
    return results


def main():
    answer = 0
    results = {'win': 0, 'loss': 0, 'draw': 0}
    while answer != 3:
        answer = get_user_menu_choice()
        if answer == 1:
            play = Game()
            result = play.play_self()
            if result == 'draw':
                results['draw'] += 1
            elif result == 'win':
                results['win'] += 1
            else:
                results['loss'] += 1
        elif answer == 2:
            print("\n Show scores")
            print_results(results)
        elif answer == 3:
            print("\n Exit")
            print_results(results)
            print('Bye and see you next time.')
            break


main()
