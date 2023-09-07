class Solution:
    def singleNumber(self, nums: list) -> int:
        nums = sorted(nums)
        if len(nums) == 1:
            return nums[0]
        else:
            i = 0
            j = 1
            while i < len(nums) and j < len(nums):
                if nums[i] == nums[j]:
                    i=j+1
                    j=i+1
                else:
                    return nums[i]
            return nums[i]

sol = Solution()
print(sol.singleNumber([2,2,1]))
print(sol.singleNumber([4,1,2,1,2]))
