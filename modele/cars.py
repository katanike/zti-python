from enum import Enum


class CarBrand:
    nazwa: str
    rok_zalozenia: int


def print_underline():
    print(44 * '*')


def print_title(label):
    print(15 * '*', label, 15 * '*')


class StatusEnum(Enum):
    GOOD = "GOOD"
    BAD = "BAD"

    def get_title(self):
        return self.name.title()


class ComponentStatus:
    def __init__(self, name: str, status: StatusEnum = StatusEnum.GOOD):
        self.name = name
        self.status = status

    def get_info(self):
        return "OK" if self.status == StatusEnum.GOOD else 'damaged or defective'


class CarStatus:
    def __init__(self, *component_statuses: ComponentStatus):
        self.component_statuses = component_statuses

    def get_technical_efficiency(self):
        for comp in self.component_statuses:
            if comp.status == StatusEnum.BAD:
                return StatusEnum.BAD
        return StatusEnum.GOOD

    def get_technical_info(self):
        return [comp.get_info() for comp in self.component_statuses]

    def print_general_info(self):
        technical_efficiency = self.get_technical_efficiency()
        print(f"Technical efficiency: {technical_efficiency.get_title()}")

    def print_technical_info(self):
        airbag, painting, mechanic = self.get_technical_info()

        print_title('Technical Info')
        print("Technical efficiency:")
        print("Airbag: {}\nPainting: {}\nMechanic: {}".format(airbag, painting, mechanic))
        print()


class Car:
    def __init__(self, brand: str, model: str, color: str, production_date: str, status: CarStatus):
        """
        :param brand: Marka samochodu
        :param model: Model samochodu
        :param color: Kolor auta
        :param production_date: Data produkcji auta
        :param status: Stan bieżący auta
        """
        self.brand = brand
        self.model = model
        self.color = color
        self.productionDate = production_date
        self.status = status

    def print_general_info(self):
        print_title('General Info')
        print(f"Car model: {self.brand} {self.model}"
              f"\t Color: {self.color}\n"
              f"Production date: {self.productionDate}")
        self.status.print_general_info()
        print()


CAR_STATUS_GOOD = CarStatus(ComponentStatus('airbag'), ComponentStatus('painting'), ComponentStatus('mechanic'))


car_01 = Car('Seat', 'Ibiza', 'blue', '2016', CAR_STATUS_GOOD)

car_02 = Car('Opel', 'Astra', 'green', '2014', CarStatus(ComponentStatus('airbag'),
                                                         ComponentStatus('painting', StatusEnum.BAD),
                                                         ComponentStatus('mechanic')))

car_03 = Car('Mazda', '6', 'white', '2013', CAR_STATUS_GOOD)


#car_01.technical_info()
car_01.print_general_info()
car_02.print_general_info()
car_03.print_general_info()