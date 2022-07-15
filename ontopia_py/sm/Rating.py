from typing import List

from rdflib import Graph, Literal

from ..ns import *
from ..l0.Description import Description


class Rating(Description):
    __type__ = SM["Rating"]

    bestUserRating: List[Literal] = None
    worstUserRating: List[Literal] = None
    userRating: Literal = None

    def _addProperties(self, g: Graph):
        super()._addProperties(g)

        if self.bestUserRating:
            for bestUserRating in self.bestUserRating:
                g.add((self.uriRef, SM["bestUserRating"], bestUserRating))

        if self.worstUserRating:
            for worstUserRating in self.worstUserRating:
                g.add((self.uriRef, SM["worstUserRating"], worstUserRating))

        if self.userRating:
            g.add((self.uriRef, SM["userRating"], self.userRating))
