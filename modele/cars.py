from enum import Enum

class Vehicle(object):
    pass


class Bike(Vehicle):
    pass




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


class Component:
    def __init__(self, name: str, status: StatusEnum = StatusEnum.GOOD):
        self.name = name
        self.status = status

    def get_info(self):
        return "OK" if self.status == StatusEnum.GOOD else 'damaged or defective'


class Components:
    def __init__(self, *components: Component):
        self.components = components

    def get_status(self):
        for comp in self.components:
            if comp.status == StatusEnum.BAD:
                return StatusEnum.BAD
        return StatusEnum.GOOD

    def print_general_info(self):
        technical_efficiency = self.get_status()
        print(f"Technical efficiency: {technical_efficiency.get_title()}")

    def print_technical_info(self):
        print_title('Technical Info')
        print("Technical efficiency:")
        for comp in self.components:
            print(f"\t{comp.name.title()}: {comp.get_info()}")
        print()


class Car(Vehicle):
    def __init__(self, brand: str, model: str, color: str, production_date: str, components: Components):
        """
        :param brand: Marka samochodu
        :param model: Model samochodu
        :param color: Kolor auta
        :param production_date: Data produkcji auta
        :param components: Komponenty, z których składa się auto
        """
        self.brand = brand
        self.model = model
        self.color = color
        self.production_date = production_date
        self.components = components

    def print_general_info(self):
        print_title('General Info')
        self.print_basic_info()
        self.components.print_general_info()
        print()

    def print_basic_info(self):
        print(f"Car model: {self.brand} {self.model}\t Color: {self.color}\n"
              f"Production date: {self.production_date}")


CAR_COMPONENTS = Components(
    Component('airbag'),
    Component('painting'),
    Component('mechanic'))


cars = [
    Car('Seat', 'Ibiza', 'blue', '2016', CAR_COMPONENTS),
    Car('Opel', 'Astra', 'green', '2014', Components(Component('airbag'),
                                                     Component('painting', StatusEnum.BAD),
                                                     Component('mechanic'),
                                                     Component('wheels'))),
    Car('Mazda', '6', 'white', '2013', CAR_COMPONENTS)
]


for car in cars:
    car.print_general_info()

for car in cars:
    car.print_basic_info()
    car.components.print_technical_info()

