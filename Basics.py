
# Exercițiu 1 Alege un film care îți place. Declară o variabilă numită
# „titlu_film" unde să memorezi titlul, apoi declară o variabilă numită „rating"
# în care să stochezi rating-ul de pe IMDB (sau un număr de la 1 la 10 cu două
# zecimale). Pe urmă, folosește o variabilă BOOL pentru a arăta dacă filmul este
# în cinema sau nu (variabila se va numi „cinema"). În final, folosește funcția
# print( ) pentru a scrie fraza: „Filmul [...] are un rating de [...]."

# OBS.: Pentru a adăuga variabile în interiorul unui string folosim conceptul de
# f-strings. Vezi exemplul de mai sus.

titlu_film = "Avatar"
rating = 9.75
cinema = True
print(f"Filmul {titlu_film} are un rating de {rating}.")



# Exercițiu 2
# Declară două variabila, a și b. Variabila a va fi un integer, iar b va fi un float (Le poți da orice valori dorești, dar să respecte
# aceste constrângeri.).

# Calculează suma dintre cele două variabile și stocheaz-o în variabila c.
# (Vezi exemplul de la Conversii implicite)

# Convertește rezultatul în string.

# Afișează cu funcția print următoarea frază:
# „Valoarea variabilei c este [...] și este de tipul [...]."

a = 12  # a = float(a) => a = 12.0
b = 37.5
c = a + b
print("Rezultatul este:", c)
c = str(c)
print(f"Valoarea variabilei c este {c} si este de tipul {type(c)}")



# Exercițiu3 Se dau două numere:
x = 11
y = ((x - 5)**2)/2

# Calculează valoarea lui y, apoi află care este restul împărțirii lui y la 9.
print(y)

# Stochează această valoare în variabila z.
z = y % 9
print(z)

# Transformă variabila z în variabilă de tip BOOLEAN.
z = bool(z)

# Printează pe ecran valoare expresiei NOT(z). Acela e răspunsul final.
print(not z)
