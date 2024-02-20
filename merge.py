class Solution:
    def merge(self, nums1: list, m: int, nums2: list, n: int) -> None:
        saved = 0
        for i in range (len(nums1)):
            indexN2 = 0
            while saved>0 or n>0:
                if saved == 0:
                    if nums1[i]>nums2[indexN2]:
                        saved = nums1[i]
                        nums1[i] = nums2[indexN2]
                        indexN2+=1
                        n-=1
                else:
                    if nums1[i]>nums2[indexN2] and nums1[i]> saved


