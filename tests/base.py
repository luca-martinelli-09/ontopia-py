from __future__ import annotations

from typing import TYPE_CHECKING, List

from ..ns import *
from .Feature import Feature

if TYPE_CHECKING:
    from rdflib import Graph, Literal

    from .AddressArea import AddressArea


class Address(Feature):
    __type__ = IOT["Address"]

    listOfObj: List[Thing] = None
    obj: Thing = None
    listOfLiteral: List[Literal] = None
    literal: Literal = None

    def _addProperties(self, g: Graph):
        super()._addProperties(g)

        if self.listOfObj:
            for listOfObj in self.listOfObj:
                g.add((self.uriRef, IOT["listOfObj"], listOfObj.uriRef))

        if self.obj:
            g.add((self.uriRef, IOT["obj"], self.obj.uriRef))

        if self.listOfLiteral:
            for listOfLiteral in self.listOfLiteral:
                g.add((self.uriRef, IOT["listOfLiteral"], listOfLiteral))

        if self.literal:
            g.add((self.uriRef, IOT["literal"], self.literal))
