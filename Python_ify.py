# if statements

#if condition : code to execute if condition is true

x_pos_1 = input(int)


if int(x_pos_1) < 2:
    print('Blad')


    
is_game_over = False
p_0_x_pos = int(x_pos_1)
e_0_x_pos = 3
e_1_x_pos = 5



if p_0_x_pos == e_0_x_pos:
    is_game_over = True

elif p_0_x_pos == e_1_x_pos:
    is_game_over = True
    
else:
 e_0_x_pos +=1
 e_1_x_pos +=1



if p_0_x_pos == e_0_x_pos or p_0_x_pos == e_1_x_pos:
    is_game_over = True

    
else:
 e_0_x_pos +=1
 e_1_x_pos +=1
    
if is_game_over == True:
    print ('Koniec gry')
else:
    print ('Graj dalej')


