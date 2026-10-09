class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        indegree=[0 for _ in range(numCourses)]
        adj_list=[[] for _ in range(numCourses)]
        for u,v in prerequisites:
            adj_list[u].append(v)
            indegree[v]+=1
        queue=deque()
        result=[]
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
            return True
        return False