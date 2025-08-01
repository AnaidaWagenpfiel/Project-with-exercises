
#EXERCIȚIU_1 Creează matricea de zerouri „test" de 4 linii și 2 coloane.
# Afișează matricea, apoi afișează numărul total de elemente și tipul de date
# al elementelor.

import numpy as np

test = np.zeros((4,2))
print(test)
print('\n')

print(test.size)
print(test.dtype)


# __EXERCIȚIU__ Să se seteze seed-ul la "123". Să se genereze o matrice de 4 pe
# 4 de numere întregi, cu valori între 4 și 8.

np.random.seed(123)
matrice = np.random.randint(4, 9, size=(4, 4))
print(matrice)

# Să se seteze seed-ul la "543" și să se repete generarea.

np.random.seed(123)
matrice = np.random.randint(4, 9, size=(4, 4))
print(matrice)
matrice2 = np.random.randint(4,9,size=(4,4))
print(matrice2)

np.random.seed(543)
matrice = np.random.randint(4, 9, size=(4, 4))
print(matrice)

# Să se printeze matricele.
# Cele două matrice ar trebui să fie diferite.


