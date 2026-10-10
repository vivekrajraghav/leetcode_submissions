class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        V=len(graph)
        adj_list=[[] for _ in range(V)]
        indegree=[0 for _ in range(V)]
        for node in range(V):
            for adjNode in graph[node]:
                adj_list[adjNode].append(node)
                indegree[node]+=1
        queue=deque()
        for i in range(V):
            if indegree[i]==0:
                queue.append(i)
        result=[]
        while len(queue)!=0:
            curr_node=queue.popleft()
            result.append(curr_node)
            for adjNode in adj_list[curr_node]:
                indegree[adjNode]-=1
                if indegree[adjNode]==0:
                    queue.append(adjNode)
        return sorted(result)