

# EXERCIȚIU_1 Definește o clasă Caine cu atribute rasa, nume și varsta.
# Creează un obiect al clasei Caine și afișează atributele acestuia.

class Caine:
    def __init__(self, rasa, nume, varsta):
        self.rasa = rasa
        self.nume = nume
        self.varsta = varsta

caine1 = Caine("Doberman", "Otto", 2)
print(f"Rasa: {caine1.rasa}, Nume: {caine1.nume}, Varsta: {caine1.varsta}")



# EXERCIȚIU_2 Adaugă o metodă descriere în clasa Caine, care returnează o
# descriere completă a câinelui. Testează metoda pe două obiecte diferite ale
# clasei.

class Caine:
    def __init__(self, nume, varsta):
        self.nume = nume
        self.varsta = varsta

    def descriere(self):
        return f"Numele cainelui este {self.nume} si are {self.varsta} ani"

    def imbatraneste(self, ani):
        self.varsta = self.varsta + ani

caine1 = Caine("Beira", 3)
caine2 = Caine("Ares", 4)
print(caine1.descriere())
print(caine2.descriere())

caine1.imbatraneste(3)
print(caine1.descriere())



# __EXERCIȚIU__
#	Creează o clasă Student cu următoarele atribute:
#   •	nume
#   •	prenume
#   •	note (o listă de note).
# Adaugă următoarele metode:
#   •	adaugare_nota pentru a adăuga o notă în listă.
#   •	calcul_medie pentru a calcula media notelor.

#	Urmează exemplele următoare pentru a testa clasa creată:
# 1. Adaugă studentul Ana Ionescu cu notele [10, 8].
# 2. Adaugă studentul Marin Iancu cu notele [7, 6, 5].
# 3. Adaugă nota 9 pentru studentul Ana Ionescu.
# 4. Adaugă nota 5 pentru studentul Ana Ionescu.
# 5. Adaugă nota 9 pentru studentul Marin Iancu.
# 6. Calculează și afișează mediile celor doi studenți.


class Student:
    def __init__(self, nume, prenume, note):
        self.nume = nume
        self.prenume = prenume
        self.note = note

    def adaugare_nota(self,nota):
        self.note.append(nota)

    def calcul_medie(self):
        return sum(self.note) / len(self.note)

    def afisare(self):
        return f"Studentul cu numele{self.nume} {self.prenume} are notele{self.note} si media {self.calcul_medie()}"

student1 = Student("Ionescu", "Ana", [10,8] )
student2 = Student("Iancu", "Marin", [7,6,5])
print(student1.afisare())
print(student2.afisare())

student1.adaugare_nota(9)
student1.adaugare_nota(5)
student2.adaugare_nota(9)

print(student1.afisare())
print(student2.afisare())



# __EXERCIȚIU__ Creează o clasă Angajat cu atributul specific „numar_ore" și
# atributele următoare:
#   •	nume complet
#   •	salariu
# Adaugă următoarea metodă:
#   •	modifica_numar_ore pentru a modifica numărul de ore de muncă ale unui
# angajat (metodă de clasă)
#  descriere() pt a afisa toate datele despre angajat
#calculati salariul angajatului pe luna

class Angajat:
    numar_ore = 8

    def __init__(self, numeComplet, salariu):
        self.numeComplet = numeComplet
        self.salariu = salariu

    @classmethod
    def modifica_numar_ore(cls, numar_ore_nou):
        cls.numar_ore = numar_ore_nou

    def descriere(self):
        return f"Numele angajatului este {self.numeComplet}, are salariul {self.salariu} lei si munceste {self.numar_ore} ore"

    def calcul_salariu(self):
        return self.salariu * self.numar_ore

angajat1 = Angajat("Sergiu Ionascu", 2500)
angajat2 = Angajat("Ioana Cozma", 5300)

print(angajat2.descriere())

Angajat.modifica_numar_ore(30)
print(angajat2.descriere())

print(angajat2.calcul_salariu())

#	Urmează exemplele următoare pentru a testa clasa creată:
# 1. Adaugă angajatul Sergiu Ionascu cu un salariu de 2500.
# 2. Adaugă angajatul Ioana Cozma cu un salariu de 5300.
# 3. Să se afișeze numărul de ore pentru angajatul Ioana Cozma.
# 4. Să se modifice numărul de ore pentru un angajat în firmă la 30.
# 5. Să se afișeze din nou numărul de ore pentru același angajat.



# __EXERCIȚIU__ Creează o clasă Matematica care include metode statice pentru:
# 	•	Calcularea pătratului unui număr.
# 	•	Verificarea dacă un număr este par.
#	 Testează metodele cu diferite valori.

class Matematica:
    @staticmethod
    def patrat(a):
        return a ** 2

    @staticmethod
    def par(a):
        return a % 2 == 0

print(Matematica.par(15))
print(Matematica.patrat(5))



#__EXERCIȚIU__ Creeaza o clasa Copil care va lua atributele nume si prenume.
#Defineste metoda salut() care va printa valorile celor 2 atribute.
#Defineste clasa Student care va modifica metoda salut().

class Copil:
    def __init__(self, nume, prenume):
        self.nume = nume
        self.prenume = prenume

    def salut(self):
        return f"Salut, {self.nume} {self.prenume}!"

class Student(Copil):
    #def __init__(self, nume, prenume)
    #super().__init__(nume,prenume)
    def salut(self):
        return f"Salut student, {self.nume} {self.prenume}!"

copil1 = Copil("Ana","Popescu")
print(copil1.salut())

student1 = Student("Ana", "Popescu")
print(student1.salut())



# __EXERCIȚIU__ Creează o clasă Angajat cu atributele:
# 	•	nume (public)
# 	•	__salariu (privat).
# 	Adaugă metode pentru a actualiza și a afișa salariul.
# 	Creează un obiect și testează funcționalitatea.

class Angajat:
    def __init__(self, nume, salariu):
        self.nume = nume
        self.__salariu = salariu

    def actualizeaza(self, suma):
        self.__salariu = suma

    def afiseaza(self):
        print(self.__salariu)

angajat1 = Angajat("Ana Ion", 3000)
angajat1.afiseaza()
angajat1.actualizeaza(5000)
angajat1.afiseaza()



# __EXERCIȚIU__	Creează o clasă Produs cu atributul privat __pret.
# Adaugă metode pentru a obține și modifica prețul. Testează funcționalitatea.

class Produs:
    def __init__(self, pret):
        self.__pret = pret

    def get_pret(self):
        return self.__pret

    def set_pret(self,pret):
        self.__pret = pret

p1 = Produs(150)
print(p1.get_pret())
p1.set_pret(300)
print(p1.get_pret())



# __EXERCIȚIU__ Creează o clasă Forma cu o metodă arie.
# Creează clase derivate Cerc și Patrat, fiecare cu propria implementare pentru
# arie.
# Creează obiecte și calculează aria pentru fiecare.

class Forma:
    def arie(self):
        return 0

class Cerc(Forma):
    def arie(self):
        return "Pi * R^2"

class Patrat(Forma):
    def arie(self):
        return "L^2"



