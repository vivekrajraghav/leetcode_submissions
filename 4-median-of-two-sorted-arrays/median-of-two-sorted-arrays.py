class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
      # Time Complexity of O(m+n)
        # n=len(nums1)
        # m=len(nums2)
        # i=0
        # j=0
        # new_list=[]
        # while n>i and m>j:
        #     if nums1[i]<=nums2[j]:
        #         new_list.append(nums1[i])
        #         i+=1
        #     elif nums1[i]>nums2[j]:
        #         new_list.append(nums2[j])
        #         j+=1
        # while i<n:
        #     new_list.append(nums1[i])
        #     i+=1
        # while j<m:
        #     new_list.append(nums2[j])
        #     j+=1
        # o=len(new_list)
        # if o%2==0:
        #     o//=2
        #     return (new_list[o-1]+new_list[o])/2
        # elif o%2!=0:
        #     o//=2
        #     return new_list[o]
        
        # Time Complexity of O(log(m+n))
        if len(nums1)>len(nums2):
            nums1,nums2=nums2,nums1
        x,y=len(nums1),len(nums2)
        low=0
        high=x
        while high>=low:
            partX=(low+high)//2
            partY=(x+y+1)//2 - partX

            maxLeftX=float("-inf") if partX==0 else nums1[partX-1]
            minRightX=float("inf") if partX==x else nums1[partX]

            maxLeftY=float("-inf") if partY==0 else nums2[partY-1]
            minRightY=float("inf") if partY==y else nums2[partY]
            if maxLeftX<=minRightY and maxLeftY<=minRightX:
                if (x+y)%2==0:
                    return (max(maxLeftX,maxLeftY)+ min(minRightX,minRightY))/2.0
                else:
                    return float(max(maxLeftX,maxLeftY))
            elif maxLeftX>minRightY:
                high=partX-1
            else:
                low=partX+1