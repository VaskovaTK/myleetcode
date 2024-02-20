class Solution:
    def searchInsert(self, nums, target: int) -> int:
        for i in range(len(nums)):
            if nums[i] >= target:
                return i

        return len(nums)

s = Solution()
print(s.searchInsert([1,3,5,6],2))