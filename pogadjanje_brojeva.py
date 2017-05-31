'''Program generira skriveni broj, koji korisnik pokušava pogoditi.
Program je napisan za Python 3.x.'''
#Generiranje slučajnog broja.
from random import randint
from random import seed
seed()
sec = randint(0, 9)
#Postavljanje brojača pokušaja na 1.
pokušaj = 1
#Uvodni spis i forma za unos broja.
print('Igra pogađanja nasumičnih brojeva od 0-9!')
x = int(input('Upiši broj od 0-9: '))
#Petlja koja uspoređuje brojeve i inkrementira pokušaje pogađanja.
while sec != x:
	x = int(input('Pokušaj ponovo: '))
	pokušaj += 1
#Ispis rezultata igre.
print('Pogodili ste broj u {}. pokušaju! Traženi broj je bio {}!'.format(pokušaj, sec))