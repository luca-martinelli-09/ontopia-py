from typing import List

from rdflib import Graph

from ..ns import *
from .d import MultiplePointOfInterest
from .PointOfInterest import PointOfInterest


class MultiplePointOfInterest(MultiplePointOfInterest):
    __type__ = POI["MultiplePointOfInterest"]

    includesPOI: List[PointOfInterest] = None

    def _addProperties(self, g: Graph):
        super()._addProperties(g)

        if self.includesPOI:
            for includesPOI in self.includesPOI:
                g.add((self.uriRef, POI["includesPOI"], includesPOI.uriRef))
