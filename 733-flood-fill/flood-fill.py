class Solution:
    # By DFS
    # def solve(self,r,c,init,color,image):
    #     if len(image)<=r or r<0 or len(image[0])<=c or c<0 or image[r][c]!=init:
    #         return
    #     image[r][c]=color     
    #     self.solve(r+1,c,init,color,image)
    #     self.solve(r-1,c,init,color,image)
    #     self.solve(r,c+1,init,color,image)
    #     self.solve(r,c-1,init,color,image)
    # def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
    #     init=image[sr][sc]
    #     if init!=color:
    #         self.solve(sr,sc,init,color,image)
    #     return image
    # By BFS
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        init=image[sr][sc]
        if init==color:
            return image
        r=len(image)
        c=len(image[0])
        queue=deque([(sr,sc)])
        image[sr][sc]=color
        while queue:
            i,j=queue.popleft()
            for x,y in [(-1,0),(1,0),(0,-1),(0,1)]:
                new_i=i+x
                new_j=j+y
                if r>new_i>=0 and c>new_j>=0 and image[new_i][new_j]==init: 
                    image[new_i][new_j]=color
                    queue.append((new_i,new_j))
        return image