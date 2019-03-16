game_over = False

while game_over == False:




    Player_1 = input("Are your rock, paper or scissors \n" )
    Player_2 = input("Are your rock, paper or scissors \n")
    print('Player 1 chose ' + Player_1)
    print('Player 2 chose ' + Player_2)

    if Player_1 != Player_2:
        a = Player_1
        b = Player_2
    else:
        print('Remis')
        break

    if a == 'rock'and b == 'paper':
        b = 1
        a = 0
    elif a == 'scissors' and b == 'rock':
        b = 1
        a = 0
    else:
        if a == 'paper' and b == 'scissors':
            b = 1
            a = 0
        else:
            a = 1
            b = 0

    if a == b:
        a = 1
        b = 1
        print('remis')


    #print(a)
    #print(b)

    if a > b:
        print('Player1 has won')
    else:
        print('Player2 has won')

    usr_command = input('Enter your command ')
    if usr_command == 'quit':
        break

















