class Solution:
    def longestConsecutive(self, nums: list) -> int:
        nums = sorted(nums)
        savedEl= None
        countEl = 0
        maxCount = 0
        duble = None
        for i in range(len(nums)):
            if duble == None:
                duble = nums[i]
                continue
            else:
                if nums[i] == duble:
                    nums[i] = None
                else:
                    duble = nums[i]
        for i in range(len(nums)):
            if nums[i] == None:
                continue
            if savedEl == None:
                savedEl = nums[i]
                countEl +=1
                continue
            else:
                if nums[i] == savedEl+1:
                    countEl+=1
                    savedEl = nums[i]
                else:
                    savedEl = nums[i]
                    if maxCount<countEl:
                        maxCount = countEl
                    countEl = 1
        # print(max(maxCount,countEl))
        return max(maxCount,countEl)

sol = Solution()
sol.longestConsecutive([100,4,200,1,3,2])
sol.longestConsecutive([0,3,7,2,5,8,4,6,0,1])
sol.longestConsecutive([1,2,0,1])