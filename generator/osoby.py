import random


GENDER_FEMALE = "female"
GENDER_MALE = "male"


plec = [
    "żeńska",
    "męska"
]

gender = [
    GENDER_MALE, GENDER_FEMALE
]

lista_imion_zenskich = [
    "Aldona",
    "Anna",
    "Agnieszka",
    "Danuta",
    "Liudmyla",
    "Kasia",
    "Kaja",
    "Marta",
    "Sandra",
    "Zuzanna"
]

lista_imion_meskich = [
    "Andrzej",
    "Bartek",
    "Czesław",
    "Darek",
    "Krzysiek",
    "Paweł",
    "Zbyszek",
    "Piotr",
    "Kornel",
    "Stasiek"
]


lista_imion = list(lista_imion_zenskich)
lista_imion += lista_imion_meskich

slownik_imion = {
    GENDER_MALE: lista_imion_meskich,
    GENDER_FEMALE: lista_imion_zenskich
}

lista_nazwisk = [
    "Adamowicz",
    "Bernatowicz",
    "Hall",
    "Kowalski",
    "Suzin",
    "Korneluk",
    "Smith",
    "Procaj",
    "Dąbrowski",
    "Frągnowski"
]



def generuj_liste_lat(wiek_min, wiek_max, liczba_elementow=10):
    return [random.randint(wiek_min, wiek_max)
            for _ in range(liczba_elementow)]


def generuj_liste_lat_yield(wiek_min, wiek_max, liczba_elementow=10):
    for _ in range(liczba_elementow):
        yield random.randint(wiek_min, wiek_max)


def generuj_nazwiska(liczba_elementow=10):
    return [random.choice(lista_nazwisk) for _ in range(liczba_elementow)]


def generuj_nazwiska_yield(liczba_elementow=10):
    for _ in range(liczba_elementow):
        yield random.choice(lista_nazwisk)


def generuj_imiona(plec=None, liczba_elementow=10):
    assert plec in slownik_imion or plec is None, f"Plec {plec} jest nieznana."
    imiona = slownik_imion[plec] if plec in slownik_imion else lista_imion
    return [random.choice(imiona) for _ in range(liczba_elementow)]


def generuj_imiona_yield(plec=None, liczba_elementow=10):
    assert plec in slownik_imion or plec is None, f"Plec {plec} jest nieznana."
    imiona = slownik_imion[plec] if plec in slownik_imion else lista_imion
    for _ in range(liczba_elementow):
        yield random.choice(imiona)


def generuj_imie_nazwisko(plec=None, liczba_elementow=10):
    imiona = generuj_imiona_yield(plec, liczba_elementow)
    nazwiska = generuj_nazwiska_yield(liczba_elementow)
    return zip(imiona, nazwiska)

