
class Adres:
    miasto: None
    ulica: None
    nr_domu: None
    nr_mieszkania: None

    def __init__(self, miasto, ulica, nr_domu, nr_mieszkania=None):
        self.miasto = miasto
        self.ulica = ulica
        self.nr_domu = nr_domu
        self.nr_mieszkania = nr_mieszkania
