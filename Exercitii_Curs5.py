
#_____________LISTE___________

#EXERCIȚIU_1 Creeați lista goală „clienti". Să se afișeze pe ecran mesajul
# „Câți clienți are firma dumneavoastră? " și să se citească o valoare n, număr
# natural pozitiv.
# Pentru toate numerele de la 1 la n să se afișeze pe ecran: „Introducti numele
# clientului cu numarul [...]: " și să se adauge clientul la lista „clienti".
# La final, să se printeze pe ecran „Clienții firmei dumneavoastră sunt: [...]"

clienti = []
n = int(input("Cati clienti are firma dumneavoastra?"))
for i in range (1,n+1):
    clinet = input(f"Introduceti numele clientului cu numarul {i}: ")
    clienti.append(clinet)

print(clienti)
print(f"Clientii firmei dumneavoastra sunt {clienti}")

#EXERCIȚIU_2 O firmă are două departamente:
# IT - cu angajații Rares, Radu și Cristina
# Marketing -- cu angajații Victor și Ioana
# În firmă se ține un meeting în care vor participa toți angajații.
# La acest meeting, Radu își declară demisia.

# Să se declare două liste, „it" și „marketing", fiecare cu elementele
# corespunzătoare. Să se declare apoi lista „meeting" care să conțină
# elementele ambelor liste. Să se elimine elementul „Radu" și să se
# afișeze lista finală.

# HINT: Pentru crearea listei „meeting" vom folosi metoda .extend( ).

it = ["Rares", "Radu", "Crisitna"]
marketing = ["Victor", "Ioana"]
meeting = []
meeting.extend(it)
meeting.extend(marketing)
meeting.remove("Radu")
print(meeting)

#EXERCIȚIU_3 Se dă o listă de numere [9, 4, 1 ,12, 5, 4]. Să se ordoneze
# lista crescător și să se elimine al doilea și ultimul element din listă.
# Să se afișeze pe ecran valoarea maximă și lungimea listei finale.

numere = [9, 4, 1, 12, 5, 4]
numere.sort()
numere.pop(1)
numere.pop()
print(numere)
print(max(numere))
print(len(numere))

#EXERCIȚIU_4 Generează o listă de numere de la 0 la 20. Creează o listă
# „numere_pare" care va prelua doar numerele din lista inițială care se află
# pe poziții pare. Afișați rezultatul.

numere = list(range(21))
print(numere)
numere_pare = numere[0:21:2]
print(numere_pare)



#__________TUPLURI_______________

#EXERCIȚIU_1 Generează un tuplu care să conțină trei studenți: Ana, Matei și Corina.
# Printează a doua valoare din tuplu (!).

studenti = ('Ana', 'Matei', 'Corina')
print(studenti[1])



#EXERCIȚIU_2 Fie "tuplul1" si "tuplul2" doua tupluri de date.
#Sa se concateneze cele doua tupluri si sa se testeze daca numele "Mihaela"
#se gaseste in tuplul rezultat.

tuplu1 = ("Ana", "Ion")
tuplu2 = ("Bogdan", "Mihaela")
tuplu3 = tuplu1 + tuplu2
print("Mihaela" in tuplu3)



# __EXERCIȚIU_3 Se dau două seturi.

fructe_ana = {'mere', 'pere', 'gutui'}
fructe_andrei = {'pere','cirese','struguri'}

# Afișează pe ecran:

# 1. Câte fructe are Ana
nr_fructe_ana = len(fructe_ana)
print(f"Ana are {nr_fructe_ana} fructe")

# 2. Care sunt fructele pe care le au amândoi
fructe = fructe_ana.union(fructe_andrei)
print(fructe)

# 3. Care sunt fructele pe care le are Andrei și nu le are Ana
fructe2 = fructe_andrei.difference(fructe_ana)
print(fructe2)

# 4. Un fruct la întâmplare din fructele Anei (folosind o metodă din cele prezentate)
print(fructe_ana.pop())
print(fructe_ana)



#_________________DICTIONARE_______________

#EXERCIȚIU_1 Definește un dicționar gol „comenzi_clienti", cu oricare dintre
# modalități. Adaugă, pe rând, perechile cheie:valoare de mai jos, care
# reprezintă numele clientului și numărul de comenzi pe care l-a făcut:
# Ana - 2  |  Mihai - 3  |  Marcel - 7  |  Karina - 1

comenzi_clienti = {'Ana': 2, 'Mihai': 3, 'Marcel': 7, 'Karina':1}

# Mihai plasează o nouă comandă. Crește numărul de comenzi făcute de Mihai cu 1.

comenzi_clienti['Mihai'] += 1

# Marcel pleacă de la firma noastră. Șterge-l pe Marcel din dicționar.

del comenzi_clienti['Marcel']
print(comenzi_clienti)

# Ana este curioasă câte comenzi a făcut. Printează numărul de comenzi făcute
# de Ana.

comenzi_ana = comenzi_clienti['Ana']
print(f"Ana are {comenzi_ana} comenzi.")

# Sandu este un nou client. Adăugă-l pe Sandu în dicționar cu o comandă făcută.

comenzi_clienti['Sandu'] = 1
print(comenzi_clienti)


# __EXERCIȚIU__ Creează o funcție care ia ca și parametru o listă de numere
# și returenază POZIȚIA celui mai MIC număr.
# Apelează funcția cu parametrul [12, 64, 21, 7, 323, 125] și printează
# rezultatul.

#lista = [12, 64, 21, 7, 323, 125]
#lista.sort()
#print(lista[0])
#minim = min(lista)
#print(f"Cel mai mic numar este {minim}")
#print(lista.index(min(lista)))





# __EXERCIȚIU__ Definește o funcție care să ia un număr întreg ca și parametru.
# Funcția va întoarce un string care reprezintă scrierea cu litere a fiecărei
# cifre.
# Exemplu:  112 -> unu unu doi
#           5231 -> cinci doi trei unu
# Apelează funcția cu exemplele date și afișează rezultatul pe ecran.


def tradu(x):

    traduceri = {
        0:'zero',
        1:'unu',
        2:'doi',
        3:'trei',
        4:'patru',
        5:'cinci',
        6:'sase',
        7:'sapte',
        8:'opt',
        9:'noua'
    }

    rezultat = []

    while x != 0:
        aux = x % 10
        x = x // 10
        rezultat.append(traduceri[aux])

        print(x)

    rezultat.reverse()
    rez = " "
    for i in rezultat:
        rez = rez + " " + i
    print(rezultat)

tradu(112)





















