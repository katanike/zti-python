from modele.vehicle import Vehicle


class Bike(Vehicle):
    def __init__(self, brand: str, model: str, color: str, production_date: str):
        super().__init__(brand, model, production_date)
        self.color = color

    def podaj_typ(self):
        return "Jestem rowerem"

