
#EXERCIȚIU_1 Creează o listă numită cuvinte_lungi care conține doar cuvintele
# din lista cuvinte cu mai mult de 5 litere. Concatenează cuvintele din acea
# listă folosind metoda .join( ) și printează propoziția rezultată.

cuvinte = ["ana", "robert","detine","are","mere","papagali"]

cuvinte_lungi = [x for x in cuvinte if len(x) > 5]
print(cuvinte_lungi)

propozitie = " ".join(cuvinte_lungi)
print(propozitie)



# __EXERCIȚIU__ Creează un set care conține doar primele litere ale cuvintelor
# dintr-o propoziție, INDIFERENT DE CAPITALIZARE.

propozitie = "Putem folosi Python pentru diferinte functionalitati specifice."

cuvinte = propozitie.split()
print(cuvinte)

cuvinte_modificate = {cuvant[0].lower() for cuvant in cuvinte}
print(cuvinte_modificate)

# HINT: Un mod de abordare al acestei probleme:
# 1. Împărțim propoziția în cuvinte folosind metoda .split( ).
# 2. Folosim un set comprehension să parcurgem fiecare cuvânt din lista de
# cuvinte creată și luăm doar prima literă din fiecare cuvânt (cuvant[0]) și
# o facem minusculă cu .lower( ).
# 3. Afișăm pe ecran setul creat.



# __EXERCIȚIU__ Creează un dicționar (lungime_cuvinte) care mapează fiecare
# cuvânt dintr-o listă la lungimea sa. (ex.: "telefon": 7)

cuvinte = ["calculator", "telefon", "tableta", "mouse"]

lungime_cuvinte = {cuvant: len(cuvant) for cuvant in cuvinte}
print(lungime_cuvinte)
print(lungime_cuvinte["mouse"])



# __EXERCIȚIU__ Definește o FUNCȚIE care să ia ca parametru un șir de caractere
# (def itereaza(cuvant)). Funcția va converti șirul de caractere într-o listă
# și va returna un iterator pentru acea listă. Apelează funcția și stochează
# rezultatul într-o variabilă „iterator". Printează primele trei litere folosind
# funcția next.

def itereaza(cuvant):
  lista_cuvant = list(cuvant)
  iterator_lista = iter(lista_cuvant)
  return iterator_lista

exemplu = "caine"
iterator = itereaza(exemplu)

print(next(iterator))
print(next(iterator))
print(next(iterator))