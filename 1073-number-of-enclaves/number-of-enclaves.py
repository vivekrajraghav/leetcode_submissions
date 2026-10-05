class Solution:
    #By DFS
    # def dfs(self,r,c,visited,grid):
    #     if r>=len(grid) or c>=len(grid[0]) or r<0 or c<0 or visited[r][c]==1 or grid[r][c]==0:
    #         return
    #     visited[r][c]=1
    #     self.dfs(r+1,c,visited,grid)
    #     self.dfs(r-1,c,visited,grid)
    #     self.dfs(r,c+1,visited,grid)
    #     self.dfs(r,c-1,visited,grid)
    # def numEnclaves(self, grid: list[list[int]]) -> int:
    #     row=len(grid)
    #     col=len(grid[0])
    #     visited=[[0 for _ in range(col)] for _ in range(row)]
    #     for i in range(row):
    #         if grid[i][0]==1 and visited[i][0]!=1:
    #             self.dfs(i,0,visited,grid)
    #     for j in range(col):
    #         if grid[0][j]==1 and visited[0][j]!=1:
    #             self.dfs(0,j,visited,grid)
    #     for i in range(row):
    #         if grid[i][col-1]==1 and visited[i][col-1]!=1:
    #             self.dfs(i,col-1,visited,grid)
    #     for j in range(col):
    #         if grid[row-1][j]==1 and visited[row-1][j]!=1:
    #             self.dfs(row-1,j,visited,grid)
    #     count=0
    #     for r in range(row):
    #         for c in range(col):
    #             if grid[r][c]==1 and visited[r][c]==0:
    #                 count+=1
    #     return count
    
    #Through BFS
    def numEnclaves(self, grid: list[list[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        visited=[[0 for _ in range(col)] for _ in range(row)]
        queue=deque()
        for i in range(row):
            if grid[i][0]==1 and visited[i][0]!=1:
                visited[i][0]=1
                queue.append((i,0))
        for j in range(col):
            if grid[0][j]==1 and visited[0][j]!=1:
                visited[0][j]=1
                queue.append((0,j))
        for i in range(row):
            if grid[i][col-1]==1 and visited[i][col-1]!=1:
                visited[i][col-1]=1
                queue.append((i,col-1))
        for j in range(col):
            if grid[row-1][j]==1 and visited[row-1][j]!=1:
                visited[row-1][j]=1
                queue.append((row-1,j))
        while len(queue)!=0:
            i,j=queue.popleft()
            for x,y in [(1,0),(-1,0),(0,1),(0,-1)]:
                new_i=i+x
                new_j=j+y
                if new_i>=row or new_j>=col or new_i<0 or new_j<0:
                    continue
                if visited[new_i][new_j]==1 or grid[new_i][new_j]==0:
                    continue
                queue.append((new_i,new_j))
                visited[new_i][new_j]=1
        count=0
        for r in range(row):
            for c in range(col):
                if grid[r][c]==1 and visited[r][c]!=1:
                    count+=1
        return count        