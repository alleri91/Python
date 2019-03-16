x_pos = 3
e_pos = 4
print(x_pos)

def movement(pozycja):
    global x_pos
    global e_pos
    x_pos += pozycja
    if x_pos == e_pos:
        return True
    else:
        return False


    
movement(5)





print(x_pos)    

#if wojtek == True:
  ##  print('kolizja')
#else:
 #   print('chuj ci w dupe') 
