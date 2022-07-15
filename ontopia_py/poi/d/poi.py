from ...l0.Characteristic import Characteristic
from ...l0.Entity import Entity
from ...l0.EventOrSituation import EventOrSituation
from ...l0.Topic import Topic
from ...ns import *


class PointOfInterest(Entity):
    __type__ = POI["PointOfInterest"]


class POINameInTime(EventOrSituation):
    __type__ = POI["POINameInTime"]


class PointOfInterestCategory(Topic):
    __type__ = POI["PointOfInterestCategory"]


class POIState(Characteristic):
    __type__ = POI["POIState"]
