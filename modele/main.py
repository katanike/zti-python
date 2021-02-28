from modele.cars import Components, Component, Car, ComponentStatus


class AirbagComponent(Component):
    pass


CAR_COMPONENTS = Components(
    Component('airbag'),
    Component('painting'),
    Component('mechanic'))



x1 = 1
x2 = 2


c1 = Component("wheels")
c2 = Component("cockipt")

lista_liczb = [
    1,1,1,1,1,1
]

lista_komp = [
    wheels,
    wheels,
    wheels,
    wheels,
    wheels,
]


component = c1

liczba = x1





cars = [
    Car('Seat', 'Ibiza', 'blue', '2016', CAR_COMPONENTS),





    Car('Opel', 'Astra', 'green', '2014', Components(AirbagComponent('airbag'),
                                                     Component('painting', ComponentStatus.DAMAGED),
                                                     Component('mechanic'),
                                                     Component('wheels'),
                                                     Component('cockpit',
                                                               components=[
                                                                   Component('Sterring Wheel'),
                                                                   Component('Radio')
                                                               ]))),




    Car('Mazda', '6', 'white', '2013', CAR_COMPONENTS)
]



#
# for car in cars:
#     car.print_general_info()
#
# for car in cars:
#     car.print_basic_info()
#     car.components.print_technical_info()
#
















class Blacha:
    pass


class Aluminium(Blacha):
    pass


class Mosiadz(Blacha):
    pass


class MojaBlacha(Aluminium, Mosiadz):
    pass


class AluminiumExtra(Aluminium):
    pass











