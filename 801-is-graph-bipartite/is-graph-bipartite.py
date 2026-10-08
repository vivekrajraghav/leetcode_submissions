class Solution:
    def dfs(self,curr_node,visited,graph,color):
        visited[curr_node]=color
        for adjNode in graph[curr_node]:
            if visited[adjNode]!=-1:
                if visited[adjNode]==color:
                    return False
            else:
                ans=self.dfs(adjNode,visited,graph,1-color)
                if ans==False:
                    return False
        return True
    def isBipartite(self, graph: list[list[int]]) -> bool:
        n=len(graph)
        visited=[-1]*n
        for idx in range(n):
            if visited[idx]==-1:
                ans=self.dfs(idx,visited,graph,0)
                if ans==False:
                    return False
        return True