from __future__ import annotations

from enum import Enum
from typing import List, Dict

from modele.vehicle import Vehicle
from utils import print_title




class CarBrand:
    nazwa: str
    rok_zalozenia: int



#############################

class StatusEnum(Enum):
    def get_title(self):
        return self.name.title()

    def is_ok(self):
        raise NotImplementedError("Not implemented")

###########################


class StatusInfo(StatusEnum):
    GOOD = "GOOD"
    BAD = "BAD"

    def is_ok(self):
        return self.name == StatusInfo.GOOD


class ComponentStatus(StatusEnum):
    OK = "OK"
    DAMAGED = "DAMAGED"
    DEFECTIVE = "DEFECTIVE"
    BURNED = "BURNED"

    def is_ok(self):
        return self.name == StatusInfo.OK


###############


class Component:
    def __init__(self, name: str, status: ComponentStatus = ComponentStatus.OK, components: List[Component] = None):
        self.name = name
        self.status = status
        self.child_components = components

    def get_info(self):
        return StatusInfo.GOOD if self.status == ComponentStatus.OK else StatusInfo.BAD


class Components:
    def __init__(self, *components: Component):
        self.components = components

    def get_info(self):
        for comp in self.components:
            if comp.get_info() == StatusInfo.BAD:
                return StatusInfo.BAD
        return StatusInfo.GOOD

    def print_general_info(self):
        technical_efficiency = self.get_info()
        print(f"Technical efficiency: {technical_efficiency.get_title()}")

    def print_technical_info(self):
        print_title('Technical Info')
        print("Technical efficiency:")
        for comp in self.components:
            print(f"\t{comp.name.title()}: {comp.get_info().get_title()}")
            if comp.child_components:
                for child in comp.child_components:
                    print(f"\t\t{child.name.title()}: {child.get_info().get_title()}")
        print()


class Car(Vehicle):
    def __init__(self, brand: str, model: str, color: str, production_date: str, components: Components = None):
        """
        :param brand: Marka samochodu
        :param model: Model samochodu
        :param color: Kolor auta
        :param production_date: Data produkcji auta
        :param components: Komponenty, z których składa się auto
        """
        super().__init__(brand, model, production_date)
        self.color = color
        self.components = components

    def print_general_info(self):
        print_title('General Info')
        self.print_basic_info()
        self.components.print_general_info()
        print()

    def print_basic_info(self):
        print(f"Car model: {self.brand} {self.model}\t Color: {self.color}\n"
              f"Production date: {self.production_date}")

    def podaj_typ(self):
        typ_super = super().podaj_typ()
        return "Jestem autem i " + typ_super

    def to_dict(self) -> Dict:
        props = super().to_dict()
        props.update({
            "color": self.color
        })
        return props



