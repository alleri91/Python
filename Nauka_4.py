
liczba_1 = input()
liczba = int(liczba_1)
print(type(liczba))


list_1 = []
y = []

x = range(1,liczba+1)

for i in x:
    if liczba % i == 0:
        lista = liczba / i
        list_1.append(lista)




print(list_1)











