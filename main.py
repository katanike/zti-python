
from dane.osoba import *
from dane.adres import Adres


LICZBA_ELEMENTOW = 10
WIEK_MIN = 0
WIEK_MAX = 120


# tworzenie rodziców, czyli obiektów typu Osoba
matka = Osoba("Marianna", "Katana", GENDER_FEMALE)
ojciec = Osoba("Stanisław", "Procaj", GENDER_MALE)

rodzice = ojciec, matka

# tworzenie obiektu klasy Adres
adres = Adres("Gdańsk", "Bałtycka", 8, 3)

# tworzenie obiektu klasy Osoba
o = Osoba("Paweł", "Procaj", sex=GENDER_MALE, adres=adres, parents=rodzice)

## czytanie pól obiektu o

imie_osoby = o.imie
nazwisko_osoby = o.nazwisko

print(imie_osoby)
print(nazwisko_osoby)


# wyświetlanie imion rodziców

print("Imię ojca:", o.parents[0].imie)
print("Imię matki:", o.parents[1].imie)

# wyświetlanie obiektu o, czyli niejawne wywołanie metody o.__repr__()
print(o)
