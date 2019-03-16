def metoda3():

    list = [5, 10, 15, 20, 25, 30, 40, 20, 40, 50]
    print(list[1])
    list_2 = []

    list_2.append(list[0])
    list_2.append(list[-1])

    return list_2

print(metoda3())

