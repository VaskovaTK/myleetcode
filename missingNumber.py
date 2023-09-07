class Solution:
    def missingNumber(self, nums: list) -> int:
        nums = sorted(nums)
        next = 0
        for i in range(len(nums)):
            if nums[i] !=next:
                return next
            else:
                next+=1
        return next


sol = Solution()
# print(sol.missingNumber([9,6,4,2,3,5,7,0,1]))
# print(sol.missingNumber([0,1]))
# print(sol.missingNumber([3,0,1]))
print(sol.missingNumber([0]))