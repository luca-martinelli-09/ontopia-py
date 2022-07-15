from typing import List

from rdflib import Graph

from ..ns import *
from ..ti.TimeInterval import TimeInterval
from .d import Address
from .d import AddressInTime


class AddressInTime(AddressInTime):
    __type__ = CLV["AddressInTime"]

    atTime: List[TimeInterval] = None
    nextAddress: List[AddressInTime] = None
    prevAddress: List[AddressInTime] = None
    withAddress: Address = None

    def _addProperties(self, g: Graph):
        super()._addProperties(g)

        if self.atTime:
            for atTime in self.atTime:
                g.add(
                    (self.uriRef, CLV["atTime"], atTime.uriRef))

        if self.nextAddress:
            for nextAddress in self.nextAddress:
                g.add(
                    (self.uriRef, CLV["nextAddress"], nextAddress.uriRef))

        if self.prevAddress:
            for prevAddress in self.prevAddress:
                g.add(
                    (self.uriRef, CLV["prevAddress"], prevAddress.uriRef))

        if self.isAddressInTimeFor:
            for isAddressInTimeFor in self.isAddressInTimeFor:
                g.add(
                    (self.uriRef, CLV["isAddressInTimeFor"], isAddressInTimeFor.uriRef))

        if self.withAddress:
            g.add((self.uriRef, CLV["withAddress"], self.withAddress.uriRef))
