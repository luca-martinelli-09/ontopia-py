from ...l0.Characteristic import Characteristic
from ...l0.EventOrSituation import EventOrSituation
from ...ns import *


class AddressInTime(EventOrSituation):
    __type__ = CLV["AddressInTime"]


class Identifier(Characteristic):
    __type__ = CLV["Identifier"]
