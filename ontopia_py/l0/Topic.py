from typing import List

from rdflib import Graph

from ..ns import *
from .d import Topic
from .d.Entity import Entity


class Topic(Topic):
    __type__ = L0["Topic"]

    isTopicOf: List[Entity] = None

    def _addProperties(self, g: Graph):
        super()._addProperties(g)

        if self.isTopicOf:
            for isTopicOf in self.isTopicOf:
                g.add((self.uriRef, L0["isTopicOf"],
                       isTopicOf.uriRef))
