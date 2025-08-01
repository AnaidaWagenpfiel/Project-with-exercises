
# Exercițiu_1 Fie două variabile, a și b, numere întregi. Alegeți ce valori
# doriți.
# Să se afișeze următoarele propoziții:
# „a este mai mare decât b: [True/False]"
# „a este egal cu b: [True/False]"

# Hint: Puteți printa direct operația condițională pentru a genera valoarea de
# adevăr.

a = 30
b = 17

print("a este mai mare decat b:", a > b) # print(f"a este mai mare decat b:, {a > b}")
print("a este egal cu b", a == b)

#___________________________________________

numar = 5
if numar > 0:
    print("pozitiv")
elif numar == 0:
    print("0")
else:
    print("negativ")


# Exercițiu_2 Citește de la tastatură un număr întreg.

# Verifică dacă numărul este par.
# În cazul afirmativ, împarte numărul la 2 și printează valoarea obținută.
# În cazul negativ, afișează pe ecran „Numărul este impar!".

# HINT: Vom folosi unul din operatorii aritmetici pentru a determina paritatea.

x = input("Introdu numar intreg aici")
x = int(x)
if x % 2 == 0:
    print ("numarul este par")
    y = x / 2                    #elif x % 2 == 0 nu merge deoarece abordeaza aceeasi situatie ca if
    print(y)
else:
    print("numarul este impar")


# Exercițiu_3 FizzBuzz
# Fie n un număr citit de la tastatură. Pentru fiecare număr !!DE LA 1 LA n!!
# (inclusiv) să se facă următoarele:
# 1. Dacă numărul este divizibil cu 3, să se afișeze FIZZ pe ecran.
# 2. Dacă numarul este divizibil cu 5, să se afișeze BUZZ pe ecran.
# 3. Dacă numărul este divizibil și cu 3 și cu 5, să se afișeze FIZZBUZZ pe
# ecran.
# 4. Dacă numărul nu este divizibil nici cu 3, nici cu 5, să se afișeze numărul.

n = input("Introdu numar")
n = int(n)
for i in range(1, n+1):
    if i % 3 == 0 and i % 5 == 0: #!!! IF indeplineste o conditie unica, de aceea am inceput cu cerinta 3
        print("FIZZBUZZ")
    elif i % 3 == 0:
        print("FIZZ")
    elif i % 5 == 0:
        print("BUZZ")
    else:
        print(i)




