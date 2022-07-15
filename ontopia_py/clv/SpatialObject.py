from typing import List

from rdflib import Graph

from ..l0.Location import Location
from ..ns import *
from ..ti.TimeInterval import TimeInterval
from .d.id import Identifier


class SpatialObject(Location):
    __type__ = CLV["SpatialObject"]

    hasIdentifier: List[Identifier] = None
    hasSOValidity: List[TimeInterval] = None

    def _addProperties(self, g: Graph):
        super()._addProperties(g)

        if self.hasIdentifier:
            for hasIdentifier in self.hasIdentifier:
                g.add(
                    (self.uriRef, CLV["hasIdentifier"], hasIdentifier.uriRef))

        if self.hasSOValidity:
            for hasSOValidity in self.hasSOValidity:
                g.add(
                    (self.uriRef, CLV["hasSOValidity"], hasSOValidity.uriRef))
