class Solution:
    def bfs(self,r,c,visited,grid):
        row=len(grid)
        col=len(grid[0])
        queue=deque()
        queue.append((r,c))
        visited[r][c]=1
        while queue:
            r,c=queue.popleft()
            for x,y in [(1,0),(0,1),(-1,0),(0,-1)]:
                new_r=r+x
                new_c=c+y
                if new_r>=row or new_c>=col or new_c<0 or new_r<0:
                    continue
                if visited[new_r][new_c]==1 or grid[new_r][new_c]=="0":
                    continue
                queue.append((new_r,new_c))
                visited[new_r][new_c]=1
    def numIslands(self, grid: List[List[str]]) -> int:
        row=len(grid)
        col=len(grid[0])
        visited=[[0 for _ in range(col)] for _ in range(row)]
        count=0
        for r in range(row):
            for c in range(col):
                if grid[r][c]=="1" and visited[r][c]==0:
                    count+=1
                    self.bfs(r,c,visited,grid)
        return count