class Solution:
    def solve(self,r,c,init,color,image):
        if len(image)<=r or r<0 or len(image[0])<=c or c<0 or image[r][c]!=init:
            return
        image[r][c]=color     
        self.solve(r+1,c,init,color,image)
        self.solve(r-1,c,init,color,image)
        self.solve(r,c+1,init,color,image)
        self.solve(r,c-1,init,color,image)
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        init=image[sr][sc]
        if init!=color:
            self.solve(sr,sc,init,color,image)
        return image