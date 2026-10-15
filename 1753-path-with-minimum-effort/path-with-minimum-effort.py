class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        row=len(heights)
        col=len(heights[0])
        effort=[[float("inf") for _ in range(col)] for _ in range(row)]
        effort[0][0]=0
        pqueue=[(0,0,0)]
        while len(pqueue)!=0:
            e,i,j=heapq.heappop(pqueue)
            if e>effort[i][j]:
                continue
            if i==row-1 and j==col-1:
                return e
            for x,y in [(1,0),(0,1),(-1,0),(0,-1)]:
                new_x=x+i
                new_y=y+j
                if new_x>=row or new_y>=col or new_x<0 or new_y<0:
                    continue
                new_eff=max(e,abs(heights[new_x][new_y]-heights[i][j]))
                if new_eff<effort[new_x][new_y]:
                    effort[new_x][new_y]=new_eff
                    heapq.heappush(pqueue,(new_eff,new_x,new_y))
