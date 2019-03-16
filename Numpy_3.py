import numpy as np

list = np.arange(11)
print(list)

list[0] = 2
print(list)

list = np.append(list, [20])
print(list)

list = np.insert(list, [3], 30)
print(list)

list = np.delete(list, [0,3])
print(list)
print(list * np.cos(90))

array = np.random.randint(1,20, size=5)
array = np.sort(array,)
print(array)