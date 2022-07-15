from typing import List

from rdflib import Graph, Literal

from ..ns import *
from ..ti.TimeInterval import TimeInterval
from .d.poi import PointOfInterest, POINameInTime


class POINameInTime(POINameInTime):
    __type__ = POI["POINameInTime"]

    isPOINameInTimeFor: PointOfInterest = None
    atTime: TimeInterval = None
    POIofficialName: List[Literal] = None
    POIalternativeName: List[Literal] = None

    def _addProperties(self, g: Graph):
        super()._addProperties(g)

        if self.isPOINameInTimeFor:
            g.add((self.uriRef, POI["isPOINameInTimeFor"],
                  self.isPOINameInTimeFor.uriRef))

        if self.atTime:
            g.add((self.uriRef, TI["atTime"], self.atTime.uriRef))

        if self.POIofficialName:
            for POIofficialName in self.POIofficialName:
                g.add((self.uriRef, POI["POIofficialName"], POIofficialName))

        if self.POIalternativeName:
            for POIalternativeName in self.POIalternativeName:
                g.add(
                    (self.uriRef, POI["POIalternativeName"], POIalternativeName))
