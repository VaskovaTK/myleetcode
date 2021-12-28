class Solution:
    def searchInsert(self, nums: list, target: int) -> int:
        for i in range(len(nums)):
            if nums[i]<target:
                continue
            else:
                return i
        return len(nums)


sol = Solution()
print(sol.searchInsert(nums = [1,3,5,6], target = 5))
print(sol.searchInsert(nums = [1,3,5,6], target = 2))
print(sol.searchInsert(nums = [1,3,5,6], target = 7))