

class Car:
    def __init__(self, brand, model, color, production_date, is_airbag_ok, is_painting_ok, is_mechanic_ok):
        """
        :param brand: Marka samochodu
        :param model: Model samochodu
        :param color: Kolor auta
        :param production_date: Data produkcji
        :param is_airbag_ok: Okresla, czy poduszki sa sprawne
        :param is_painting_ok: Okresla, czy lakier jest oryginalny
        :param is_mechanic_ok: Okresla czy mechanika jest sprawna
        """
        self.brand = brand
        self.model = model
        self.color = color
        self.productionDate = production_date
        self.is_airbag_ok = is_airbag_ok
        self.is_painting_ok = is_painting_ok
        self.is_mechanic_ok = is_mechanic_ok

        print("airbag is ok? ", is_airbag_ok)

    def general_info(self):
        if self.is_airbag_ok and self.is_painting_ok and self.is_mechanic_ok:
            technicalEfficiency = 'Good'
        else:
            technicalEfficiency = 'Bad'
        print(15 * '*', 'General Info', 15 * '*')
        print("Car model: {} {}\t Color: {}\nProduction date: {}".format(self.brand, self.model, self.color, self.productionDate))
        print("Technical efficiency: {}".format(technicalEfficiency))
        print(44 * '*')

    def technical_info(self):
        if self.is_airbag_ok:
            airbag = 'OK'
        else:
            airbag = 'damaged or defective'

        if self.is_painting_ok:
            painting = 'OK'
        else:
            painting = 'damaged or defective'

        if self.is_mechanic_ok:
            mechanic = 'OK'
        else:
            mechanic = 'damaged or defective'

        print(14 * '*', 'Technical Info', 14 * '*')
        print("Technical efficiency:")
        print("Airbag: {}\nPainting: {}\nMechanic: {}".format(airbag, painting, mechanic))
        print(44 * '*')



car_01 = Car('Seat', 'Ibiza', 'blue', '2016', True, True, True)
car_02 = Car('Opel', 'Astra', 'green', '2014', True, False, True)





car_01.general_info()
car_01.technical_info()
car_02.general_info()
