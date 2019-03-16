is_game_over =  False
p_x_pos = 3
e_x_pos = 3
end_x_pos = 10

while not is_game_over:
    print(p_x_pos)
    print(e_x_pos)
    if p_x_pos == e_x_pos:
        print('You lose')
        is_game_over = True
    elif p_x_pos >= end_x_pos:
            print('You win')
            is_game_over = True
            
    else:
        p_x_pos +=4
        e_x_pos +=1
        
while is_game_over:
    print(p_x_pos)
    print(e_x_pos)
    if p_x_pos == e_x_pos:
        print('You lose')
        is_game_over = False
    elif p_x_pos >= end_x_pos:
            print('You win')
            is_game_over = False
            
    else:
        p_x_pos +=4
        e_x_pos +=1
        
print(p_x_pos)
print(e_x_pos)
