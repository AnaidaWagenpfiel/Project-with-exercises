
# __EXERCIȚIU_1 Creează o clasă „Laptop" care să conțină următoarele atribute
# de instanță:
# 1. furnizor
# 2. preț_net
# 3. memorie_ram

# Adaugă două metode:
# 1. calcul_pret_brut -- Calculează și returnează prețul brut prin adăugarea
# unui TVA (19%)
# 2. adaugare_ram -- Primește un parametru și adaugă numărul primit la memoria
# RAM a laptop-ului

class Laptop:
    tva = 0.19

    def __init__(self, furnizor, pret_net, memorie_ram):
        self.furnizor = furnizor
        self.pret_net = pret_net
        self.memorie_ram = memorie_ram

    def calcul_pret_brut(self):
        rezultat = self.pret_net + (self.tva * self.pret_net)
        return rezultat

    def adaugare_ram(self, ram_plus):
        self.memorie_ram += ram_plus

laptop1 = Laptop("Dell", 2500, 16)
print(laptop1.calcul_pret_brut())
laptop1.adaugare_ram(9)
print(laptop1.memorie_ram)



# __EXERCIȚIU__ Creează o clasă „Cetatean" care să conțină următoarele atribute
# de instanță (__self__):
# 1. prenume
# 2. nume_de_familie
# 3. cnp (atribut PRIVAT)

# Creează apoi următoarele atribute de clasă:
# 1. nationalitate (cu valoarea standard „romana")
# 2. numar_total_de_cetateni (cu valoarea standard 1000000)

# Creează o metodă de instanță pentru a afișa următoarea propoziție:
# „Numele complet al cetățeanului este [prenume] [nume_de_familie]"
# ! Dacă prenumele sau numele de familie nu sunt de forma standard (prima literă
# majusculă și restul minuscule), să se realizeze această modificare în
# prealabil.

# Creează o metodă de instanță pentru a afișa CNP-ul cetățeanului. (get_CNP())

# Creează următoarea metodă de clasă:
# 1. seteaza_nationalitatea - Modifică naționalitatea cetățenilor

# La final, gândește-te la un mod de a crește numărul total de cetățeni de
# fiecare dată când se creează un nou obiect de tipul Cetatean. Adaugă această
# modificare.

class Cetatean:
    nationalitate = "romana"
    numar_total_de_cetateni = 1000000

    def __init__(self, prenume, nume_de_familie, cnp):
        self.prenume = prenume
        self.nume_de_familie = nume_de_familie
        self.__cnp = cnp

    def afisare(self):
        self.prenume = self.prenume.capitalize()
        self.nume_de_familie = self.nume_de_familie.capitalize()
        return f"Numele complet al cetateanului este {self.prenume} {self.nume_de_familie}"

    def afisare_cnp(self):
        return f"CNP-ul clientului este {self.__cnp}"

    @classmethod
    def seteaza_nationalitatea(cls, nationalitate_noua):
        cls.nationalitate = nationalitate_noua


        
c1 = Cetatean("ana", "IoNEScu", 938838229)
print(c1.afisare())
print(c1.afisare_cnp())
c1.seteaza_nationalitatea("italian")
print(c1.nationalitate)




# __EXERCIȚIU__ Să se creeze clasa „Dreptunghi" cu atributele de instanță:
# 1. latime
# 2. lungime

# Creează următoarele metode:
# 1. perimetru -- Calculează perimetrul dreptunghiului (2*latime + 2*lungime)
# 2. arie -- Calculează aria dreptunghiului (latime * lungime)

# Să se creeze apoi clasa „Patrat" pornind de la premisa că orice pătrat este
# un dreptunghi dar nu orice dreptunghi este un patrat.

# Să se apele metodele „perimetru" și „arie" pe un obiect de tipul Patrat.

class Dreptunghi:

    def __init__(self, latime, lungime):
        self.latime = latime
        self.lungime = lungime

    def perimetru(self):
        calcul_perimetru = 2 * self.lungime + 2 * self.latime
        return calcul_perimetru

    def arie(self):
        calcul_arie = self.lungime * self.latime
        return calcul_arie

class Patrat(Dreptunghi):

    def __init__(self, latura):

        self.latime = latura
        self.lungime = latura

    def verificare_patrat(self):

        if self.latime == self.lungime:
            return "Este patrat."

        else:
            return "Nu este patrat. Este dreptunghi."

forma1 = Patrat(2)
print(forma1.verificare_patrat())
print(forma1.perimetru())
print(forma1.arie())

forma2 = Dreptunghi(4,3)
print(forma2.perimetru())
print(forma2.arie())
















