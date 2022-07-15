from typing import List

from rdflib import Graph, Literal

# from ..clv import Address
# from ..clv.Geometry import Geometry
from ..ns import *
# from ..sm.d import Image
from ..ti.TimeInterval import TimeInterval
from .d.poi import (POINameInTime, PointOfInterest, PointOfInterestCategory,
                    POIState)


class PointOfInterest(PointOfInterest):
    __type__ = POI["PointOfInterest"]

    hasPOICategory: List[PointOfInterestCategory] = []
    hasAddress: List = []  # Address
    hasPOINameInITime: List[POINameInTime] = None
    hasImage: List = None  # Image
    atTime: List[TimeInterval] = None
    hasGeometry = None  # Geometry
    hasPOIState: POIState = None
    isIncludedInPOI = None  # MultiplePointOfInterest
    POIofficialName: List[Literal] = None
    POIdescription: List[Literal] = None
    POIID: Literal = None

    def _addProperties(self, g: Graph):
        super()._addProperties(g)

        if self.hasPOICategory:
            for hasPOICategory in self.hasPOICategory:
                g.add(
                    (self.uriRef, POI["hasPOICategory"], hasPOICategory.uriRef))

        if self.hasAddress:
            for hasAddress in self.hasAddress:
                g.add((self.uriRef, CLV["hasAddress"], hasAddress.uriRef))

        if self.hasPOINameInITime:
            for hasPOINameInITime in self.hasPOINameInITime:
                g.add(
                    (self.uriRef, POI["hasPOINameInITime"], hasPOINameInITime.uriRef))

        if self.hasImage:
            for hasImage in self.hasImage:
                g.add(
                    (self.uriRef, SM["hasImage"], hasImage.uriRef))

        if self.atTime:
            for atTime in self.atTime:
                g.add(
                    (self.uriRef, TI["atTime"], atTime.uriRef))

        if self.hasPOICategory:
            g.add((self.uriRef, POI["hasPOICategory"],
                  self.hasPOICategory.uriRef))

        if self.hasGeometry:
            g.add((self.uriRef, CLV["hasGeometry"], self.hasGeometry.uriRef))

        if self.hasPOIState:
            g.add((self.uriRef, CLV["hasPOIState"], self.hasPOIState.uriRef))

        if self.isIncludedInPOI:
            g.add((self.uriRef, CLV["isIncludedInPOI"],
                  self.isIncludedInPOI.uriRef))

        if self.hasGeometry:
            g.add((self.uriRef, CLV["hasGeometry"], self.hasGeometry.uriRef))

        if self.POIofficialName:
            for POIofficialName in self.POIofficialName:
                g.add((self.uriRef, POI["POIofficialName"], POIofficialName))

        if self.POIdescription:
            for POIdescription in self.POIdescription:
                g.add((self.uriRef, POI["POIdescription"], POIdescription))

        if self.POIID:
            g.add((self.uriRef, POI["POIID"], self.POIID))
