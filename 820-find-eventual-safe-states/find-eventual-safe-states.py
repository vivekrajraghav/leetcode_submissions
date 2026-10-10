class Solution:
    # By BFS
    # def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
    #     V=len(graph)
    #     adj_list=[[] for _ in range(V)]
    #     indegree=[0 for _ in range(V)]
    #     for node in range(V):
    #         for adjNode in graph[node]:
    #             adj_list[adjNode].append(node)
    #             indegree[node]+=1
    #     queue=deque()
    #     for i in range(V):
    #         if indegree[i]==0:
    #             queue.append(i)
    #     result=[]
    #     while len(queue)!=0:
    #         curr_node=queue.popleft()
    #         result.append(curr_node)
    #         for adjNode in adj_list[curr_node]:
    #             indegree[adjNode]-=1
    #             if indegree[adjNode]==0:
    #                 queue.append(adjNode)
    #     return sorted(result)

    #  By DFS
    def dfs(self,curr_node,adj_list,visited,path,is_safe):
        visited[curr_node]=1
        path[curr_node]=1
        for adjNode in adj_list[curr_node]:
            if visited[adjNode]==0:
                ans=self.dfs(adjNode,adj_list,visited,path,is_safe)
                if ans==False:
                    return False
            elif path[adjNode]==1:
                return False
        is_safe[curr_node]=1
        path[curr_node]=0
        return True

    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        V=len(graph)
        visited=[0 for _ in range(V)]
        path=[0 for _ in range(V)]
        is_safe=[0 for _ in range(V)]
        for i in range(V):
            if visited[i]==0:
                self.dfs(i,graph,visited,path,is_safe)
        result=[]
        for i in range(V):
            if is_safe[i]==1:
                result.append(i)
        return result