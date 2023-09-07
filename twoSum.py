class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        for i in range(len(nums)):
            newTarget = target-nums[i]
            for j in range(i+1,len(nums)):
                if newTarget - nums[j] == 0:
                    return [i,j]

