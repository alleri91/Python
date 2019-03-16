import random
import time

game_over = False
print('Aby wygenerowac liczba wpisz "Generuj" aby skonczyc wpisz "Exit" ')
while game_over == False:
    usr_inp = input()
    if usr_inp == 'exit':
        game_over = True
    else:
        r_liczba = random.randrange(1,10)
        usr_liczba = 0
        i = 0
        while r_liczba != usr_liczba:
            usr_liczba = input('Wpisz swoja liczbe: \n')
            for liczba in usr_liczba:
                i+=1
            usr_liczba = int(usr_liczba)
            if usr_liczba > r_liczba:
                time.sleep(2)
                print("Twoja liczba jest za duża\n")
            elif usr_liczba < r_liczba:
                time.sleep(2)
                print('Twoja liczba jest za mała\n')
            else:
                print('Zgadles wlasciwa liczba!')
                time.sleep(2)

                print('Zgadnij nowa liczba albo wpisz "exit", aby zakonczyc')

            print('To bylo twoje {} podejscie '.format(i))
