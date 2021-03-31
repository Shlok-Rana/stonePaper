import random
print('=========== Game ===========')
print('You have 5 lives to guess the number\n')
list = ['rock', 'paper', 'scissor']

i = 1
comp_win = 0
gamer_win = 0
while(i<6):
    choice = input('Enter = ')
    computer = random.choice(list)
    if (choice == 'rock'):
        if (computer == 'paper'):
            print('Computer value is =', computer)
            print('You loose')
            comp_win = comp_win + 1
            print('\n')

        elif (computer == choice):
            print('Computer value is =', computer)
            print('Draw')
            print('\n')

        else:
            print('Computer value is =', computer)
            print('You win')
            gamer_win = gamer_win + 1
            print('\n')

    if (choice == 'paper'):
        if (computer == 'scissor'):
            print('Computer value is =', computer)
            print('You loose')
            comp_win = comp_win + 1
            print('\n')

        elif (computer == choice):
            print('Computer value is =', computer)
            print('Draw')
            print('\n')

        else:
            print('Computer value is =', computer)
            print('You win')
            gamer_win = gamer_win + 1
            print('\n')

    if (choice == 'scissor'):
        if (computer == 'rock'):
            print('Computer value is =', computer)
            print('You loose')
            comp_win = comp_win + 1
            print('\n')

        elif (computer == choice):
            print('Computer value is =', computer)
            print('Draw')
            print('\n')

        else:
            print('Computer value is =', computer)
            print('You win')
            gamer_win = gamer_win + 1
            print('\n')

    i = i+1

if (gamer_win > comp_win):
        print('Congratulations, you win the entire game')

if (gamer_win < comp_win):
        print('Better luck next time, you loose')

if (gamer_win == comp_win):
        print('The whole game is draw')

