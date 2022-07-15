from typing import List

from rdflib import Graph, Literal

from ..ns import *
from .d.poi import PointOfInterest, PointOfInterestCategory


class PointOfInterestCategory(PointOfInterestCategory):
    __type__ = POI["PointOfInterestCategory"]

    POIcategoryName: List[Literal] = None
    isPOICategoryFor: List[PointOfInterest] = None

    def _addProperties(self, g: Graph):
        super()._addProperties(g)

        if self.POIcategoryName:
            for POIcategoryName in self.POIcategoryName:
                g.add((self.uriRef, POI["POIcategoryName"], POIcategoryName))

        if self.isPOICategoryFor:
            for isPOICategoryFor in self.isPOICategoryFor:
                g.add(
                    (self.uriRef, POI["isPOICategoryFor"], isPOICategoryFor.uriRef))
