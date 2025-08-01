
#EXERCIȚIU_1 Factorialul unui număr reprezintă produsul tuturor numerelor
# naturale de la 1 până la acel număr. Un caz special îl reprezintă factorialul
# lui 0, care în matematică este egal cu 1.

# Să se definească funcția factorial( ) care va lua un parametru x și va returna
# factorialul lui x.

# Se citesc de la tastatură două numere naturale, a și b.
# Folosiți funcția factorial( ) pentru a calcula factorialul fiecăruia dintre
# aceste numere și afișați pe ecran suma lor.

def factorial(x):

    if x < 0:
        return 0
    if x == 0:
        return 1

    produs = 1

    for i in range(x):
        produs = produs * (i+1)

    return produs

a = int(input("Introdu o valoare pentru a: "))
b = int(input("Introdu o valoare pentru b: "))

a = factorial(a)
b = factorial(b)

print(a+b)



#EXERCIȚIUL_3

# Fie trei numere mai mari decât 0: a, b, c. Puteți să le dați
# ce valori doriți.
# Să se definească funcția produs_3( ) care ia ca parametri trei
# numere și returnează produsul lor. Să se apeleze funcția cu parametri
# a, b și c și să se afișeze rezultatul pe ecran.

# produs_3(a,b,c) - apelam functia

a = 3
b = 5
c = 7
def produs_3(a,b,c):
    produs = a * b * c
    return produs
print(produs_3(a,b,c))



#EXERCIȚIU_4 Să se definească o funcție numită „conversie_kilometraj( )"
# care să primească doi parametri, „producator_masina" (string) și
# „kilometri" (float). Variabila „kilometri" va avea o valoare implicită de 0.

# Dacă kilometrajul este introdus ca parametru, va calcula distanța parcursă in
# mile (1km = 0.62mile) și va returna rezultatul.
# Dacă kilometrajul nu este introdus, va afișa textul „Mașina este nouă!" și
# va returna 0.

# Testați funcția folosind liniile de cod de mai jos:

# print("Masina are " + conversie_kilometraj("BMW", 100000) + " mile.")
# print("Masina are " + conversie_kilometraj("Mercedes Benz") + " mile.")

def conversie_kilometraj(producator_masina, kilometri=0):
    if kilometri == 0:
        print("Masina este noua")
        return str(0)
    mile = 0.62 * kilometri
    return str(mile)

print("Masina are " + conversie_kilometraj("BMW", 100000) + " mile.")
print("Masina are " + conversie_kilometraj("Mercedes Benz") + " mile.")


