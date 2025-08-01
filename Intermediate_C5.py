
# __EXERCIȚIU__ Creează funcția „putere()" care ia ca parametri două
# numere și returnează calculul primului număr ridicat la cel de-al doilea.

# Testează funcția voastră în diferite situații.

# Apelează testele fiecare în parte, apoi încearcă să apelezi toate testele
# simultan folosind unittest.main() (Vezi instrucțiunile de mai sus.)

# Introdu un nou test care va garanta eșec și rulează-l.



import unittest

def putere(a,b):
    return a ** b

class TestPutere(unittest.TestCase):

    def test_putere_1(self):
        self.assertEqual(putere(3,2),9)

    def test_putere_2(self):
        self.assertNotEqual(putere(-2,2,), -4 )

    def test_putere_3(self):
        self.assertIn(putere(2,2),[1,3,5])

TestPutere().test_putere_2()

if __name__ == '__main__':
    unittest.main()



# __EXERCIȚIU__ Creează o clasă Masina care are metodele:
# 1.	start() pentru pornirea motorului.
# 2.	stop() pentru oprirea motorului.
# 3.	este_pornita() pentru a verifica dacă motorul este pornit.

# Scrie un test utilizând Given/When/Then pentru a verifica dacă:
# 1.	Motorul este pornit atunci când apelăm start().
# 2.	Motorul este oprit atunci când apelăm stop().

class Masina:
    def __init__(self, pornit):
        self.pornit = pornit

    def start(self):
        self.pornit = True

    def stop(self):
        self.pornit = False

    def este_pornita(self):
        return self.pornit == True

class TestMasina(unittest.TestCase):
    def test_start(self):
        #given
        m1 = Masina(False)

        #when
        m1.start()

        #then
        self.assertEqual(m1.este_pornita(), True)


    def test_stop(self):
        # given
        m1 = Masina(True)

        # when
        m1.stop()

        # then
        self.assertEqual(m1.este_pornita(), True)

if __name__ == '__main__':
    unittest.main()


