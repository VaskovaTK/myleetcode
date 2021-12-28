class Solution:
    def findDisappearedNumbers(self, nums: list) -> list:
        n = len(nums)
        nums = sorted(nums)
        array = []
        for i in range(0,len(nums)):
            if nums[i] != i+1:
                if i+1 not in nums:
                    array.append(i+1)
        return array

sol =Solution()
print(sol.findDisappearedNumbers([4,3,2,7,8,2,3,1]))
print(sol.findDisappearedNumbers([1,1]))