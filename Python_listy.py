# To sa turple po polsku krotki
size = (100, 200)
width = size[0]
height = size[1]
print(size)
print (width)

len(size)
max(size)
min(size)

does_containt = 150 in size
    
print (does_containt)
print(len(size))


new_size = size + (300,)
#del new_size
len(new_size)
print(len(new_size))

# Od teraz zaczynaja sie listy

movement = [5, -2, -3, 4, -1] # listy sa w kwadratowych
first_movement = movement[0] # liczenie krokow odbywa sie od 0
movement[0] = 7
movement.append (19)
movement.remove (-3)


print (movement)


# Od teraz zaczynaja sie dictonaries

# definujemy obiekty i wartosci

starting_pos = {'p_1': 50, 'p_2': 100, 'p_3': 150}
print(starting_pos['p_1'])

starting_pos.update({'p_4':300})
starting_pos.update({'p_1':350})
print(starting_pos)

