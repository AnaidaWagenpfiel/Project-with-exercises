from numpy.ma.extras import average


# __EXERCIȚIU__ Să se definească o funcție „inmulteste_x( )" care ia un parametru
# și returnează o funcție de tip „closure" care adaugă o valoare dată la
# parametrul funcției.

def inmulteste_x(x):
    def inmulteste_la_y(y):
        return x * y
    return inmulteste_la_y

creste_cu_5 = inmulteste_x(5)

print(creste_cu_5(10))



# __EXERCIȚIU__ Să se definească o funcție „plural( )" care ia ca parametru
# o listă de șiruri de caractere și adaugă litera „e" la finalul fiecărui șir
# din listă. În rezolvarea problemei veți folosi o funcție imbricată pentru a
# adăuga e la finalul cuvintelor.



#__EXERCIȚIU__ Se dă dicționarul următor:
studenti = {
    "Andrei":[7,9,10],
    "Maria":[10,5,10],
    "George":[2,6,7],
    "Andra":[9,1,6],
    "Matei":[10,10,9]
}
# Să se definească o funcție care, pentru fiecare dintre studenții din
# dicționarul dat, va calcula media notelor și va afișa „Studentul [...] a
# trecut!", dacă media este peste 5, sau „Studentul [...] a picat", dacă media
# este sub 5.

# Pentru calculul mediei se va defini o funcție imbricată, care va fi apelată
# pe fiecare listă de note.



# __EXERCIȚIU__ Definește o funcție care să ia un număr variabil de valori
# întregi și să calculeze suma acestora.

def suma(*numere):
    s = 0
    for n in numere:
        s = s + n
    print(s)

suma(5,7)
suma(10,12)
suma(127,134)



# __EXERCIȚIU__ Fie dicționarul următor, care stochează dacă un client și-a
# făcut cont pe platforma noastră sau nu (True = Da, False = Nu):
clienti = {
    "Andrei": True,
    "Maria": False,
    "George": True,
    "Andra": False,
    "Matei": True}

# Să se definească o funcție care ia un număr variabil de perechi cheie valoare
# și returnează numărul clienților care au cont pe platforma noastră.
# Puteți apela funcția atât prin apel normal, cât și prin adăugarea parametrului
# **clienti la apel.

def clienti1(**conturi):
    clienti_platforma = 0
    for cheie, valoare in conturi.items():
        if valoare == True:
            clienti_platforma += 1
    print(clienti_platforma)

print(clienti1(Andrei =True, Maria= False, George=True, Andra=False, Matei=True))
clienti = {
    "Andrei": True,
    "Maria": False,
    "George": True,
    "Andra": False,
    "Matei": True
}

print(clienti1(**clienti))



# __EXERCIȚIU__ Creeați o funcție lambda care ia un parametru a și returnează
# rezultatul ridicării lui a la puterea 2. Atribuiți această funcție variabilei
# "patrat" și folosiți-o pe două exemple.

patrat = lambda a : a ** 2
print(patrat(7))
print(patrat(12))



## __EXERCIȚIU__ Creeați o funcție lambda care ia două variabile, „nume" și
# „prenume", și returnează concatenarea acestora cu spațiu între ele.
# (Ex.: "Ana","Popescu" -> "Ana Popescu")
# Atribuiți această funcție variabilei „concateneaza" și rulați următoarele
# exemple:

# concateneaza("Ana","Popescu")
# concateneaza("Gigel","Florea")

concateneaza = lambda nume, prenume : nume + " " + prenume
print(concateneaza("Ana","Popescu"))
print(concateneaza("Gigel","Florea"))


#___________MAP_____________

# __EXERICȚIU__ Se dă lista următoare:
cuvinte = ["albina", "CAInE","Pisica","LuP","CAL"]

# Să se genereze lista actualizată de animale, unde toate cuvintele sunt scrise
# cu minuscule.
print(list(map(lambda cuvant: cuvant.lower(), cuvinte)))


#_________FILTER____________

# __EXERCIȚIU__ Se dă următoarea listă de cuvinte:
cuvinte = ["Mare", "munte", "Plaja","Nisip","copaci"]

# Să se definească variabila „rezultat" care va stoca strict cuvintele care
# încep cu majusculă.

rezultat = list(filter(lambda cuvant: cuvant[0].isupper(),cuvinte))
print(rezultat)


#_____________REDUCE*__________

# Se dă lista următoare de numere:
cuvinte = ["Ana", " ","are"," ","mere","."]

# Să se concateneze, folosind funcția reduce( ), cuvintele din listă și să se
# afișeze rezultatul obținut.

from functools import reduce

rezultat = list(reduce(lambda x,y : x + y, cuvinte))

print(rezultat)



# __EXERCIȚIU__ Se dă lista următoare:

studenti = [("Andrei","prezent",9.50),("Ana","absent",7.0),("Rares","prezent",8.5)]

# Să se ordoneze lista de studenți în funcție de media studentului și să se afișeze rezultatul.
# Apoi, să se afișeze numele studentului cu media cea mai mare.

medie = sorted(studenti, key = lambda x: x[2])
print(medie)
media_cea_mai_mare = max(studenti, key=lambda x: x[2])
print(f"Media cea mai mare: {media_cea_mai_mare}")

# __EXERCIȚIU__ Se dă lista următoare:

angajati = ["Ana Popescu", "Ana Ionescu", "Albert Ioan", "Bogdan Codrea", "Ana Ursache"]

# Să se filtreze lista de angajați și să se stocheze în variabila rez1 strict
# angajații cu prenumele „Ana".

rez1 = list(filter(lambda nume: nume.startswith("Ana"), angajati))
print(rez1)

# Apoi, să se modifice scrierea cuvintelor din rez1 pentru a conține doar
# majuscule.

rez2 = list(map(lambda nume: nume.upper(),rez1))
print(rez2)