class Solution(object):
    # nodes = 0;
    nodes = dict()
    end = 0
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        g = self.buildGraph(graph)
        prj = self.findPaths(g)
        return prj
        
    def buildGraph(self, graph):
        d = {}
        for n,nodes in enumerate(graph):
            d[n] = nodes
        self.end = len(d) - 1
        return d
    
    def findPaths(self, dict_graph, start=0, path=[]):
        path = path + [start]
        if start == self.end:
            return [path]
        if start not in dict_graph:
            return []
        paths = []
        for node in dict_graph[start]:
            if node not in path:
                newpaths = self.findPaths(dict_graph,node,path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths
        
Solution = Solution()
c = Solution.allPathsSourceTarget([[1,2], [3], [3], []])
print(c)