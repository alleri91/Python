import numpy as np

lista = np.arange(1,11)
try:
    print(lista[4::-1])
except:
    if IndexError:
         print('Chuj ci w dupe')

print(np.log2(lista))


x = lista.max()
print(x)