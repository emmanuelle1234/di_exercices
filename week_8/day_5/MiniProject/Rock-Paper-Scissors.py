def get_user_menu_choice():
    print("""
            1.Play a new game
            2.Show scores
            3.Exit
            """)
    try:
        answer = int(input("What would you like to do? Pleaser enter 1, 2 or 3: "))
        if answer == 1:
            print("\n Play a new game")
            return answer
        elif answer == 2:
            print("\n Show scores")
            return answer
        elif answer == 3:
            print("\n Exit")
            return answer
        else:
            raise Exception('invalid_choice')
    except ValueError:
        print("You should choose between 1, 2 or 3.")
    except:
        print('This is not a valid choice.')



def print_results (results):
    results = {win: 2,loss: 4,draw: 3}


def main():
    answer = 0
    while answer != 3:
        get_user_menu_choice()
        if answer == 1:
            game = Game()
            return answer
        elif answer == 2:
            print("\n Show scores")
            return answer
        elif answer == 3:
            print("\n Exit")
            break


get_user_menu_choice()