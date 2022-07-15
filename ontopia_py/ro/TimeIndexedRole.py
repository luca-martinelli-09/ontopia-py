from typing import List

from rdflib import Graph

from ..l0.Agent import Agent
from ..l0.Entity import Entity
from ..l0.EventOrSituation import EventOrSituation
from ..ns import *
from ..ti.TemporalEntity import TemporalEntity
from .declarations.Role import Role


class TimeIndexedRole(EventOrSituation):
    __type__ = RO["TimeIndexedRole"]

    forEntity: List[Entity] = None
    isRoleInTimeOf: List[Agent] = None
    withRole: List[Role] = None
    hasTemporalEntity: List[TemporalEntity] = None

    def _addProperties(self, g: Graph):
        super()._addProperties(g)

        if self.forEntity:
            for forEntity in self.forEntity:
                g.add((self.uriRef, RO["forEntity"], forEntity.uriRef))

        if self.isRoleInTimeOf:
            for isRoleInTimeOf in self.isRoleInTimeOf:
                g.add((self.uriRef, RO["isRoleInTimeOf"],
                      isRoleInTimeOf.uriRef))

        if self.withRole:
            for withRole in self.withRole:
                g.add((self.uriRef, RO["withRole"], withRole.uriRef))

        if self.hasTemporalEntity:
            for hasTemporalEntity in self.hasTemporalEntity:
                g.add(
                    (self.uriRef, TI["hasTemporalEntity"], hasTemporalEntity.uriRef))
