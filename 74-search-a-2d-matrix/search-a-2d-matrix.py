class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # if matrix is [] or matrix is not [0]:
        #     return False
        row=len(matrix)
        col=len(matrix[0])
        low=0
        high=row*col-1
        while high>=low:
            mid=(low+high)//2
            mid_value=matrix[mid//col][mid%col]
            if mid_value==target:
                return True
            elif mid_value>target:
                high=mid-1
            elif mid_value<target:
                low=mid+1
        return False