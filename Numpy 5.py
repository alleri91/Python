import numpy as np



rnd = np.random.randint(1,10,5)
rnd2 = np.random.randint(1,10,5)


matryca = np.matrix([[7,4,3,5,1],[7,4,3,5,1],[2,4,9,1,7]])
print(matryca[2,2:])
#print(np.zeros([5,5]))

print(np.average(matryca))

matryca[0] = [10, 20, 30, 40, 50]


print(np.sort(matryca))
print(matryca)

mat = matryca.transpose()
mat_1 = matryca.flatten()
print(mat)
print(mat_1)
dupa = np.matrix('1 2;2 3')

mat = np.add(matryca,matryca)
print(mat)

mat = np.matmul(dupa,dupa)
print(mat)