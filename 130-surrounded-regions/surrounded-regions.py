class Solution:
    def dfs(self,i,j,visited,board):
        if i>=len(board) or i<0 or j>=len(board[0]) or j<0 or visited[i][j]==1 or board[i][j]!="O":
            return
        visited[i][j]=1
        self.dfs(i+1,j,visited,board)
        self.dfs(i-1,j,visited,board)
        self.dfs(i,j+1,visited,board)
        self.dfs(i,j-1,visited,board)
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row=len(board)
        col=len(board[0])
        visited=[[0 for _ in range(col)] for _ in range(row)]
        for i in range(row):
            if board[i][0]=="O":
                self.dfs(i,0,visited,board)
        for j in range(col):
            if board[0][j]=="O":
                self.dfs(0,j,visited,board)
        for i in range(row):
            if board[i][col-1]=="O":
                self.dfs(i,col-1,visited,board)
        for j in range(col):
            if board[row-1][j]=="O":
                self.dfs(row-1,j,visited,board)
        for r in range(row):
            for c in range(col):
                if board[r][c]=="O" and visited[r][c]!=1:
                    board[r][c]="X"