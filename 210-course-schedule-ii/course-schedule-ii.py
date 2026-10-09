class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        adj_list=[[] for _ in range(numCourses)]
        indegree=[0 for _ in range(numCourses)]
        queue=deque()
        result=[]
        for u,v in prerequisites:
            adj_list[v].append(u)
            indegree[u]+=1
        for i in range(numCourses):
            if indegree[i]==0:
                queue.append(i)
        while len(queue)!=0:
            curr_node=queue.popleft()
            result.append(curr_node)
            for adjNode in adj_list[curr_node]:
                indegree[adjNode]-=1
                if indegree[adjNode]==0:
                    queue.append(adjNode)
        if len(result)==numCourses:
            return result
        return []