list = ['banan', 'jablko', 'owoc', 'mandaryna']



for i, fruit in enumerate(list):
    print (i)
    print('Sprawdzam czy jest w porzadku {}'.format(fruit))
    if fruit == 'owoc':
        continue
    print(fruit)

if "banan" and 'jablko' in list:

    print('Mamy owoc')


x = 'Hello {} {}'
y = x.format(input('Wpisz swoje imie:\n '), input('Wpisz swoje nazwisko:\n '))
print(y)