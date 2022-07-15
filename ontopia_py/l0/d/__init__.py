from ...ns import *
from ...Thing import Thing
from ..Entity import Entity as RealEntity


class Entity(Thing):
    __type__ = L0["Entity"]


class Collection(RealEntity):
    __type__ = L0["Collection"]


class Topic(RealEntity):
    __type__ = L0["Topic"]
