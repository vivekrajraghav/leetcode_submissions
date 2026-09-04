class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i=0
        j=0
        arr=[]
        while m>i and n>j:
            if nums1[i]<=nums2[j]:
                arr.append(nums1[i])
                i+=1
            else:
                arr.append(nums2[j])
                j+=1
        while m>i:
            arr.append(nums1[i])
            i+=1
        while n>j:
            arr.append(nums2[j])
            j+=1
        nums1[:]=arr

