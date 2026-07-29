class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n==1:
            return [[1]]
        if n==0:
            return [[]]
        top=0
        left=0
        bottom=n-1
        right=n-1
        result=[[0]*n for i in range(n)]
        element=1
        while top<=bottom and left<=right:
            for i in range(left,right+1):
                result[top][i]=element
                element+=1
            top+=1
            for i in range(top,bottom+1):
                result[i][right]=element
                element+=1
            right-=1
            if top<=bottom:
                for i in range(right,left-1,-1):
                    result[bottom][i]=element
                    element+=1
                bottom-=1
            if left<=right:
                for i in range(bottom,top-1,-1):
                    result[i][left]=element
                    element+=1
                left+=1
        return result

