class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def mark_infinity(matrix,i_index,j_index):
            r=len(matrix)
            c=len(matrix[0])
            for i in range(0,r):
                if matrix[i][j_index]!=0:
                    matrix[i][j_index]=float("inf")
            for j in range(0,c):
                if matrix[i_index][j]!=0:
                    matrix[i_index][j]=float("inf")
        row=len(matrix)
        col=len(matrix[0])
        for i in range(0,row):
            for j in range(0,col):
                if matrix[i][j]==0:
                    mark_infinity(matrix,i,j)
        for i in range(0,row):
            for j in range(0,col):
                if matrix[i][j]==float("inf"):
                    matrix[i][j]=0

