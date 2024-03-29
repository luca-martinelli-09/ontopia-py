from __future__ import annotations

from typing import TYPE_CHECKING, List

from ..ns import *
from .SupportUnit import SupportUnit

if TYPE_CHECKING:
    from rdflib import Graph, Literal


class HomogeneousOrganizationalArea(SupportUnit):
    __type__ = COV["HomogeneousOrganizationalArea"]

    AOOIdentifier: Literal = None

    def _addProperties(self, g: Graph):
        super()._addProperties(g)

        if self.AOOIdentifier:
            g.add((self.uriRef, COV["AOOIdentifier"], self.AOOIdentifier))
