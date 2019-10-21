from typing import *

class Ticket:

    def __init__(self, to):
        self.to = [to]

    def add(self, to):
        if self.to[0] > to:
            self.to.insert(0, to)
        else:
            for i in range(len(self.to)):
                if self.to[i] > to:
                    self.to.insert(i, to)


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        it_map = {}

        for _from, to in tickets:
            if _from not in it_map:
                it_map[_from] = Ticket(to)
            else:
                it_map[_from].add(to)

        start = it_map['JFK']
        res = ['JFK']

        while start and start.to:
            next = start.to.pop(0)
            res.append(next)
            start = it_map.get(next, None)

        return res


Solution().findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]])
