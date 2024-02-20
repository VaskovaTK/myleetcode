class Solution:
    def majorityElement(self, nums: list) -> int:
        maxEl = None
        count = 0
        for i in range(len(nums)):
            if maxEl == None:
                maxEl = nums[i]
                count+=1
            elif maxEl == nums[i]:
                count+=1
            else:
                count-=1
                if count == 0:
                    maxEl = None
        return maxEl







sol = Solution()
print(sol.majorityElement([1,2,2]))
print(sol.majorityElement([3,2,3]))
print(sol.majorityElement([2,2,1,1,1,2,2]))
