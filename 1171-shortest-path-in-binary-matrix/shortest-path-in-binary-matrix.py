class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        if grid[0][0]==1:
            return -1
        queue=deque()
        row=len(grid)
        col=len(grid[0])
        distance=[[float("inf") for _ in range(col)] for _ in range(row)]
        queue.append([0,0,1])
        distance[0][0]=1
        while len(queue)!=0:
            i,j,d=queue.popleft()
            for x,y in [(1,0),(0,1),(-1,0),(0,-1),(-1,-1),(-1,1),(1,-1),(1,1)]:
                new_x=x+i
                new_y=y+j
                if new_x>=row or new_y>=col or new_x<0 or new_y<0 or grid[new_x][new_y]==1 or distance[new_x][new_y]!=float("inf"):
                    continue
                queue.append([new_x,new_y,d+1])
                distance[new_x][new_y]=d+1
        if distance[row-1][col-1]==float("inf"):
            return -1
        return distance[row-1][col-1]