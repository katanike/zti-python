import random


lista_przedmiotow = [
    "Programowanie w Pythonie",
    "Usługi Internetowe",
    "System Linux",
    "Bazy danych"
]

def generuj_przedmioty(liczba_elementow=10):
    return [random.choice(lista_przedmiotow) for _ in range(liczba_elementow)]
