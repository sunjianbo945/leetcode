import collections
from typing import *

class Solution:

    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:

        graph = self.build_graph(connections)
        visited=[False]*(n+1)
        lowest=[float('inf')]*(n+1)
        dis_from_root=[float('inf')]*(n+1)
        res = []
        self.dfs(graph, visited, lowest,dis_from_root,0,-1,0, res)
        return res

    def dfs(self,graph,visited,lowest_dis_reach,dis_from_root,cur,pre, dis,res):

        visited[cur]=True

        dis_from_root[cur],lowest_dis_reach[cur] = dis, dis

        for neighbor in graph.get(cur):
            if not visited[neighbor]:
                self.dfs(graph,visited,lowest_dis_reach,dis_from_root,neighbor,cur,dis+1,res)

            if pre>=0 and pre!=neighbor:
                lowest_dis_reach[cur] = min(lowest_dis_reach[cur],lowest_dis_reach[neighbor])

        if lowest_dis_reach[cur]>dis_from_root[pre] and pre>=0:
            res.append([pre,cur])


    def build_graph(self,connections):

        res = collections.defaultdict(list)

        for _from,_to in connections:
            res[_from].append(_to)
            res[_to].append(_from)

        return res