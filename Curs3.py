
#EXERCIȚIU_1 Se citește de la tastatură un număr n, mai mare ca 0 și mai mic
# ca 20. Să se afișeze pe ecran toate numerele de la 1 la n ridicate la pătrat.

n = int(input("Introdu un numar: "))
if n > 0 and n < 20:
    for i in range(1,n+1):
        print(f"{i} la patrat este {i**2}")


#Exercițiu_2 Doi cicliști sunt într-o cursă. Primul ciclist (a) a traversat
# deja 100 metri. Al doi ciclist (b) nu a auzit fluierul și e încă la start
# (la distanța 0), însă ciclistul b se mișcă de două ori mai repede decât a.
# Ciclistul a se mișcă cu 10 m/s.
# În câte secunde îl va întrece b pe ciclistul a?

# HINT: Primul pas este să identificăm care este condiția de oprire a WHILE.
# Avem două variabile care cresc constant, și noi vrem să aflăm momentul când
# una e mai mare decât cealaltă.
# Pentru a număra pașii de execuție, puteți folosi o a treia variabilă. Valoarea
# acelei variabile va fi rezultatul.

count = 0

a = 100
b = 0
while a > b:
    a += 10
    b += 20
    count = count + 1

print(f"Ciclistul b il va intrece pe a in {count} secunde")



#Exercițiu_3 Fie variabila „parola" cu valoarea „pass123". Inițiază o buclă
# în care utilizatorului i se cere să introducă parola. Dacă a introdus-o greșit
# de 3 ori, afișează pe ecran „ACCES INTERZIS" și oprește bucla.

parola = "pass123"
incercari_maxime = 3
incercari = 0
while incercari < incercari_maxime:
    parola_introdusa = input("Introduceti parola: ")
    if parola_introdusa == parola:
        print("ACCES PERMIS")
        break
    else:
        incercari += 1
        print("Parola gresita")

if incercari == incercari_maxime:
    print("ACCES INTERZIS")



#EXERCIȚIU_4 Se citește un cuvânt w DE LA TASTATURĂ. Să se parcurgă literele
# acestui cuvânt și, dacă se găsește litera „a" sau „A", să se afișeze pe ecran
# „Am găsit!" și să se oprească parcurgerea. Dacă s-a parcurs tot cuvântul și
# nu s-a găsit, să se afișeze „Cuvântul [...] nu conține litera A / a!".

# HINT: Putem folosi operatorul de egalitate „==" în lucrul cu string-uri.

w = (input("Introdu cuvantul: "))
am_gasit = False

for caracter in w:
    if caracter == "A" or caracter == "a":
        print("Am gasit")
        am_gasit = True
        break

if not am_gasit:
    print(f"Cuvantul {w} nu contine litera A/a")



#EXERCIȚIU_5 Se citește un număr natural n > 0 de la tastatură. Pe urmă,
# utilizatorul este rugat de n ori să introducă de la tastatură câte o literă.
# După fiecare input de la utilizator, se va afișa:
# „Litera următoare în alfabet este: [...]"
# Dacă s-a introdus „z" răspunsul va fi „a", iar dacă s-a introdus „Z"
# răspunsul este „A".

# HINT: O variantă de a executa acest exercițiu este de a converti răspunsul
# primit de la utilizator în cod ASCII, să creștem codul ASCII cu o unitate și
# să convertim numărul obținut înapoi în caracter.

n = int(input("Introdu un numar: "))
if not n > 0:
    print("Numarul trebuie sa fie pozitiv")
else:
    for i in range(n):
        litera = input("Introdu o litera: ")

        if litera == "z":
            litera == "a"
            
        elif litera == "Z":
            litera == "A"

        else:
            valoare_ascii = ord(litera)
            valoare_ascii += 1
            litera = chr(valoare_ascii)

        print(f"Litera urmatoare in alfabet este: {litera}")