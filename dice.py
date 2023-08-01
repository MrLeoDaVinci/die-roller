import random

print('Hello and welcome to Leo\'s die roller. Please say \n\nd2 roll \nd6 roll \nd10 roll \nd12 roll \nd20 roll \n\nto roll a die \n')

while True:
    die_input = input()

    if die_input == 'd2 roll':
        d2 = random.randint(1, 2)
        print(d2)
	
    elif die_input == 'd6 roll':
        d6 = random.randint(1, 6)
        print(d6)

    elif die_input == 'd10 roll':
        d10 = random.randint(1, 10)
        print(d10)

    elif die_input == 'd12 roll':
        d12 = random.randint(1, 12)
        print(d12)

    elif die_input == 'd20 roll':
        d20 = random.randint(1, 20)
        print(d20)

    elif die_input == 'exit':
        print('Exiting the program.')
        break
    else:
        print('Not a valid input. Please type a roll, or exit')
