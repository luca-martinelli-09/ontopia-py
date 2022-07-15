from ...l0.Characteristic import Characteristic
from ...l0.EventOrSituation import EventOrSituation
from ...l0.Topic import Topic
from ...ns import *
from ..PointOfInterest import PointOfInterest


class MultiplePointOfInterest(PointOfInterest):
    __type__ = CLV["Feature"]


class POINameInTime(EventOrSituation):
    __type__ = POI["POINameInTime"]


class PointOfInterestCategory(Topic):
    __type__ = POI["PointOfInterestCategory"]


class POIState(Characteristic):
    __type__ = POI["POIState"]
