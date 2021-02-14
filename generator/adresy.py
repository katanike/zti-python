import random

lista_ulic = [
    "Kościuszki",
    "Bałtycka",
    "Słabego",
    "Grunwaldzka",
    "Sikorskiego"
]

lista_miast = [
    "Gdańsk",
    "Olsztyn",
    "Gdynia",
    "Biedaszki",
    "Warszawa"
]



def generuj_liste_ulic(liczba_elementow=10):
    return [random.choice(lista_ulic) for _ in range(liczba_elementow)]


def generuj_liste_miast(liczba_elementow=10):
    return [random.choice(lista_miast) for _ in range(liczba_elementow)]


def generuj_adres(liczba_elementow=10):
    ulice = generuj_liste_ulic(liczba_elementow)
    miasta = generuj_liste_miast(liczba_elementow)

    ulica_miasto = zip(ulice, miasta)
