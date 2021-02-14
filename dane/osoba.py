
GENDER_FEMALE = "female"
GENDER_MALE = "male"

class Osoba:
    imie = None
    nazwisko = None
    adres = None
    sex = None
    parents = None  # (father, mother)

    def __init__(self, imie, nazwisko, sex=None, adres=None, parents=None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.sex = sex
        self.adres = adres
        self.parents = parents

    def is_male(self):
        return self.sex == GENDER_MALE

    def is_female(self):
        return self.sex == GENDER_FEMALE

    def get_father(self):
        return self.parents[0] if self.parents is not None else None

    def get_mother(self):
        return self.parents[1] if self.parents is not None else None

    def get_imie_ojca(self):
        return self.get_father().imie if self.get_father() is not None else None

    def get_imie_matki(self):
        return self.get_mother().imie if self.get_mother() is not None else None

    def get_nazwisko_matki(self):
        return self.get_mother().nazwisko if self.get_mother() is not None else None

    def __repr__(self):
        return f"Osoba(imie={self.imie},nazwisko={self.nazwisko})"
