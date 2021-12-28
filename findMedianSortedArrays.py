class Solution:
    def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:
        newList = [0]*(len(nums1)+len(nums2))
        i = 0
        j = 0
        newIndex =0
        while i<len(nums1) and j <len(nums2):
            if nums1[i]<nums2[j]:
                newList[newIndex] = nums1[i]
                i+=1
                newIndex+=1
            else:
                newList[newIndex] = nums2[j]
                j += 1
                newIndex+=1
        if i<len(nums1):
            while i<len(nums1):
                newList[newIndex] = nums1[i]
                newIndex+=1
                i+=1
        else:
            while j < len(nums2):
                newList[newIndex] = nums2[j]
                newIndex += 1
                j += 1
        middle = len(nums1)+len(nums2)
        if middle %2 ==0:
            first = newList[middle//2]
            second = newList[(middle//2)-1]
            retMid = (first+second)/2
            return retMid
        else:
            first = newList[middle//2]
            return float(first)
sol = Solution()
print(sol.findMedianSortedArrays(nums1 = [1,3], nums2 = [2]))
print(sol.findMedianSortedArrays(nums1 = [1,2], nums2 = [3,4]))

