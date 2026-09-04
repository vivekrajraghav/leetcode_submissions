from collections import Counter
class Solution:
    def solve(self,board,word,i,j,word_idx):
        if word_idx==len(word):
            return True
        if (i<0 or i>=len(board) or 
            j<0 or j>=len(board[0]) or 
            board[i][j]!=word[word_idx]):
            return False
        temp=board[i][j]
        board[i][j]="#"
        found=(
            self.solve(board,word,i+1,j,word_idx+1) or
            self.solve(board,word,i-1,j,word_idx+1) or
            self.solve(board,word,i,j+1,word_idx+1) or
            self.solve(board,word,i,j-1,word_idx+1)
        )
        board[i][j]=temp
        return found
    def exist(self, board: List[List[str]], word: str) -> bool:
        m=len(board)
        n=len(board[0])
        board_freq=Counter(char for row in board for char in row)
        word_freq=Counter(word)
        for char,count in word_freq.items():
            if board_freq[char]<count:
                return False
        if word_freq[word[0]]>board_freq[word[-1]]:
            word=word[::-1]
        word_present=False
        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0]:
                    if self.solve(board,word,i,j,0):
                        return True
        return False