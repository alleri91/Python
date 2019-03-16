
def usr_liczb():
    return int(input('Wpisz swoja liczbe: '))

def sprawdzenie(a):
    list_2 = []
    prime = False
    for i in range(1,a+1):
        if a % i == 0:
            list_2.append(i)
    #print(list_2)
    return list_2
