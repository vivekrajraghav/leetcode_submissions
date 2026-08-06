class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n=len(nums1)
        m=len(nums2)
        i=0
        j=0
        new_list=[]
        while n>i and m>j:
            if nums1[i]<=nums2[j]:
                new_list.append(nums1[i])
                i+=1
            elif nums1[i]>nums2[j]:
                new_list.append(nums2[j])
                j+=1
        while i<n:
            new_list.append(nums1[i])
            i+=1
        while j<m:
            new_list.append(nums2[j])
            j+=1
        o=len(new_list)
        if o%2==0:
            o//=2
            return (new_list[o-1]+new_list[o])/2
        elif o%2!=0:
            o//=2
            return new_list[o]