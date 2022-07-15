from typing import List

from rdflib import Graph, Literal

from ..ns import *
from .declarations.UserAccount import UserAccount
from .declarations.OnlineContactPoint import OnlineContactPoint
from .SocialMedia import SocialMedia
from .Post import Post


class UserAccount(UserAccount):
    __type__ = SM["UserAccount"]

    isAccountIssuedBy: SocialMedia = None
    isUserAccountOf: OnlineContactPoint = None
    URL: Literal = None
    userAccountName: Literal = None
    isCreatorOf: List[Post] = None

    def _addProperties(self, g: Graph):
        super()._addProperties(g)

        if self.isAccountIssuedBy:
            g.add((self.uriRef, SM["isAccountIssuedBy"],
                  self.isAccountIssuedBy.uriRef))

        if self.isUserAccountOf:
            g.add((self.uriRef, SM["isUserAccountOf"],
                  self.isUserAccountOf.uriRef))

        if self.URL:
            g.add((self.uriRef, SM["URL"], self.URL))

        if self.userAccountName:
            g.add((self.uriRef, SM["userAccountName"], self.userAccountName))

        if self.isCreatorOf:
            for isCreatorOf in self.isCreatorOf:
                g.add((self.uriRef, SM["isCreatorOf"], isCreatorOf.uriRef))
