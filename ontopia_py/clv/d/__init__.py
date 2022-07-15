from ...l0.Characteristic import Characteristic
from ...l0.EventOrSituation import EventOrSituation
from ...ns import *
from ..Feature import Feature


class Address(Feature):
    __type__ = CLV["Address"]


class AddressComponent(Feature):
    __type__ = CLV["AddressComponent"]


class AddressInTime(EventOrSituation):
    __type__ = CLV["AddressInTime"]


class Identifier(Characteristic):
    __type__ = CLV["Identifier"]