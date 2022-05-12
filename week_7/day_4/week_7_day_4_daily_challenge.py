# DAILY CHALLENGE

num1 = int(input('Please enter a first number: '))
num2 = int(input('Please enter a second number: '))


def division(num1, num2):
    try:
        division_result = num1 / num2
        print(f'{num1} / {num2} = {division_result}')
        return division_result
    except ZeroDivisionError as e:
        print('Sorry but division by zero is impossible...\n...because zero has no inverse\n...because any number '
              'multiplied by zero equals zero.')
        print(f'Such an error generates the following exception message: {e}')
    except TypeError as e:
        print('Sorry but division is an operation which requires 2 numbers and only 2 numbers.')
        print(f'Such an error generates the following exception message: {e}')
    except ValueError as e:
        print('Sorry but division is an operation which requires numbers and numbers only.')
        print(f'Such an error generates the following exception message: {e}')
    except FloatingPointError as e:
        print('Sorry but something failed due to the representation of floating-point numbers which has nothing to do '
              'with python.')
        print(f'Such an error generates the following exception message: {e}')
    except RuntimeError as e:
        print('Sorry but an error which does not fall in any identified category of errors has unfortunately happened.')
        print(f'Such an error generates the following exception message: {e}')
    finally:
        print('...Finally, we choose not to disturb you with a while loop and asking you again and again for numbers \n'
              'but please feel free to use this exceptional function infinitely.')

division(num1, num2)

print('\n')

division(5, 0)
