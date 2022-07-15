from typing import List

from rdflib import Graph

from ..ns import *
from .Entity import Entity


class Collection(Entity):
    __type__ = L0["Collection"]

    hasMember: List[Entity] = None

    def _addProperties(self, g: Graph):
        super()._addProperties(g)

        if self.hasMember:
            for hasMember in self.hasMember:
                g.add((self.uriRef, L0["hasMember"], hasMember.uriRef))
