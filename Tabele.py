import random

lista_1=[]
tabela_1 = random.sample(range(100), 20)
tabela_2 = random.sample(range(100), 20)
print(tabela_1)
print(tabela_2)

a = set(tabela_1)
b = set(tabela_2)

c = a.intersection(b)
print(c)

