class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        row=len(mat)
        col=len(mat[0])
        visited=[[0 for _ in range(col)] for _ in range(row)]
        distance=[[0 for _ in range(col)] for _ in range(row)]
        queue=deque()
        for r in range(row):
            for c in range(col):
                if mat[r][c]==0:
                    queue.append([r,c,0])
                    visited[r][c]=1
        while len(queue)!=0:
            i,j,d=queue.popleft()
            distance[i][j]=d
            for x,y in [(1,0),(-1,0),(0,1),(0,-1)]:
                new_i=i+x
                new_j=j+y
                if new_i>=row or new_i<0 or new_j>=col or new_j<0:
                    continue
                if visited[new_i][new_j]==1:
                    continue
                queue.append([new_i,new_j,d+1])
                visited[new_i][new_j]=1
        return distance