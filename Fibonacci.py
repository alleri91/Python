import time
liczba = int(input('Wprowadz miejsce obliczenia'))
x = [0,1,1]
i = 1
fib = 0


if liczba == 0:
    fib = []
elif liczba == 1:
    fib = [1]
elif liczba == 2:
    fib = [1,1]
elif liczba > 2:
    fib = [1,1]
    while i < liczba - 1:
        fib.append(fib[0] + fib[1])
        fib.remove(fib[0])
        y = fib[1]
        x.append(y)
        #print(fib)
        #set(x)
        print(x)
        #time.sleep(2)
        i += 1






