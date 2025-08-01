
# __EXERCIȚIU__ Se dă propoziția „Pisica e in casa."

a = "Pisica e in casa"

# Să se concateneze propoziția „Cainele e in curte."

b = " Cainele e in curte"
c = a + b
print(c)

# Să se afișeze lungimea șirului.

print(len(c))

# Să se afișeze strict cuvântul „Pisica".

print(c[0:6])

# Se se afișeze rezultatul în ordinea inversă a caracterelor.

print(c[::-1])


#EXERCIȚIU_2 Un palindrom este un cuvânt care se scrie la fel și de la cap
# la coadă, și de la coadă la cap. Exemplu: apa, rotitor, elevele

# Să se definească o funcție care ia ca parametru un șir de caractere și
# returnează „True" dacă este palindrom, și „False" dacă nu.

# Să se apele funcția pe exemplele următoare:
# 1. „elefac cafele"
# 2. „elefant"
# 3. „potop"

def palindrom(cuvant):
   return cuvant == cuvant[::-1]
print(palindrom('elefac cafele'))
print(palindrom('elefant'))
print(palindrom('potop'))



# __EXERCIȚIU_ Se dă propoziția „masina mare cara fructe multe"
text = "masina mare cara fructe multe"

# Să se despartă propoziția în cuvinte.

cuvinte = text.split()
print(cuvinte)

# Să se parcurgă lista de cuvinte. Pentru fiecare cuvânt care începe cu litera
# „m", să se transforme toate caracterele sale în majuscule.

for i in range(len(cuvinte)):
    if cuvinte[i].startswith("m"):
        cuvinte[i] = cuvinte[i].upper()
print(cuvinte)

# Să se formeze la loc propoziția și să se afișeze.

propozitie_noua = " ".join(cuvinte)
print(propozitie_noua)
