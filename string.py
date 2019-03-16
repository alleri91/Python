import random

lista ='a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,w,x,y,z,1,2,3,4,5,6,7,8,9,!,@,#,$,%,^,&,*,(,)'
split_lista = lista.split(',')

print(split_lista)

lista_2 = []
i = 0

def funkcja(a):
    i = 0
    while i <= a-1:
        x = random.choice(split_lista)
        lista_2.append(x)
        i+=1
    return lista_2


Imie = input('Please write your name: ')
a = int(input('How many signs, you want to make your password: \n'))
place = input('Where do you plan to use it? ')
strong = input('Do you want to make it strong password? \n ')
funkcja(a)

x = lista_2
str(x)
password = ''.join(x)

if strong == 'yes':
    true_password = password.capitalize()
else:
    true_password = password
    print("Your password will be weak")
print(true_password)

log = open('{}.txt'.format(Imie),mode='a+')
log.write('Name: {} Password : {} Place : {}\n'.format(Imie, true_password, place))
log.close()



