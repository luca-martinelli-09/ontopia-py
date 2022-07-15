from typing import List

from rdflib import Graph

from ..ns import *
from ..Thing import Thing
from .d import Image


class Image(Image):
    __type__ = SM["Image"]

    isImageOf: List[Thing] = None

    def _addProperties(self, g: Graph):
        super()._addProperties(g)

        if self.isImageOf:
            for isImageOf in self.isImageOf:
                g.add((self.uriRef, SM["isImageOf"], isImageOf.uriRef))
