class Solution:
    def removeElement(self, nums: list, val: int) -> int:
        count = 0
        for i in range(0, len(nums)):
            if nums[i] != val:
                count += 1
            else:
                nums[i] = None
        addIndex = 0
        for i in range(0, len(nums)):
            if nums[i] != None:
                nums[addIndex] = nums[i]
                addIndex += 1
        for i in range(count,len(nums)):
            nums[i] = None
        # print(nums)
        return count



sol = Solution()
sol.removeElement([0,1,2,2,3,0,4,2], val = 2)