import numpy as np

oceny = np.array([56, 78, 98, 90, 58, 64, 67, 72, 93, 51])

max = np.max(oceny)
print(max)
min = np.min(oceny)
print(min)
avg = np.average(oceny)
print(avg)
print(np.argmax(oceny))
print(np.argmin(oceny))

sort = np.sort(oceny)
print(sort)

sort = -np.sort(-oceny)
print(sort)

zwiekszone_oceny = oceny + 10
print(zwiekszone_oceny)
dupa = np.array([0,0,0,10,20,0,0,23,0,32])
zw_oceny = np.add(oceny, dupa)
print(zw_oceny)