class Vehicle(object):
    def __init__(self, brand: str, model: str, production_date: str):
        """
        :param brand: Marka pojazdu
        :param model: Model pojazdu
        :param production_date: Data produkcji auta
        """
        self.brand = brand
        self.model = model
        self.production_date = production_date

    def podaj_typ(self):
        return "Jestem pojazdem"

    def __repr__(self):
        return self.podaj_typ()

    def to_dict(self):
        return {
            "brand": self.brand,
            "model": self.model,
            "production_date": self.production_date
        }

#
# x = Vehicle("ford", "T", "1910")
#
# print(x)

