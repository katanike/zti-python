from typing import Dict

from modele.bikes import Bike
from modele.cars import Components, Component, Car, ComponentStatus


class AirbagComponent(Component):
    pass


car_components = Components(
    Component('airbag'),
    Component('painting'),
    Component('mechanic'))



cars = [
    Car('Seat', 'Ibiza', 'blue', '2016', car_components),

    Car('Opel', 'Astra', 'green', '2014', Components(AirbagComponent('airbag'),
                                                     Component('painting', ComponentStatus.DAMAGED),
                                                     Component('mechanic'),
                                                     Component('wheels'),
                                                     Component('cockpit',
                                                               components=[
                                                                   Component('Sterring Wheel'),
                                                                   Component('Radio')
                                                               ]))),

    Car('Mazda', '6', 'white', '2013', car_components)
]


def stworz_nazwe(car: Car):
    return f"{car.brand}-{car.model}"


nazwy_aut = [stworz_nazwe(car) for car in cars]

print(nazwy_aut)

#
# for car in cars:
#     car.print_general_info()

# for car in cars:
#     car.print_basic_info()
#     car.components.print_technical_info()
#

# bike = Bike("romet", "wigry", "zielony", "1985")
# print(bike)


car = Car("ford", "T", "black", "1910")


print(car)


car_dict = {
    "brand": "ford",
    "model": "T",
    "color": "black",
    "production_date": "1910"
}

print(car_dict)
print(car_dict["brand"])


print(car.brand)
print(car.production_date)


# def get_car_from_dict(slownik: Dict):
#     pass
#


def get_car_from_dict(slownik: Dict) -> Car:
    return Car(
        brand=slownik["brand"],
        model=slownik["model"],
        color=slownik["color"],
        production_date=slownik["production_date"])


def get_dict_from_car(car: Car) -> Dict:
    return {
        "brand": car.brand,
        "model": car.model,
        "color": car.color,
        "production_date": car.production_date
    }




new_car_dict = get_dict_from_car(car)
print(new_car_dict)

new_car = get_car_from_dict(new_car_dict)

print(get_dict_from_car(new_car))



print(15*"*")
print(car.to_dict())


import csv

with open('cars.csv', mode='w') as csv_file:
    fieldnames = ['brand', 'model', 'production_date', 'color']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

    for car in cars:
        writer.writerow(car.to_dict())





