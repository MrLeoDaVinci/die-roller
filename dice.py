import random

print('Hello and welcome to Leo\'s die roller.')

while True:
    number_input = int(input('How many dice are you using? \n'))
    die_input = input('What type of dice are you using? (example, d6, d10, d20) \n')


    if die_input.startswith('d') and die_input[1:].isdigit():
        sides = int(die_input[1:])
    else:
        print('Invalid input for the type of dice. Please use the correct format (example, d6, d10, d20).\n')
        continue

    print('Type roll to roll the dice. or exit to exit the program\n')
    inpt = input()

    if inpt == 'exit':
        print('Exiting the program.')
        break
    elif inpt == 'roll':

        while True:
            results = [random.randint(1, sides) for _ in range(number_input)]
            print(' '.join([str(result) for result in results]))
            print('Type roll to roll another set of dice or new dice. or exit to exit the program\n')
            inpt = input()

            if inpt == 'new dice':
                break
            elif inpt != 'roll':
                print('Invalid input. Please type roll or new dice. or exit to exit the program\n')
                break
    else:
        print('Invalid input. Please type roll or new dice\n')
		
