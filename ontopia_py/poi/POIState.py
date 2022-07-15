from typing import List

from rdflib import Graph, Literal

from ..ns import *
from .d import POIState
from .PointOfInterest import PointOfInterest


class POIState(POIState):
    __type__ = POI["POIState"]

    POIstate: List[Literal] = None
    isPOIStateFor: List[PointOfInterest] = None

    def _addProperties(self, g: Graph):
        super()._addProperties(g)

        if self.POIstate:
            for POIstate in self.POIstate:
                g.add((self.uriRef, POI["POIstate"], POIstate))

        if self.isPOIStateFor:
            for isPOIStateFor in self.isPOIStateFor:
                g.add(
                    (self.uriRef, POI["isPOIStateFor"], isPOIStateFor.uriRef))
