class Solution:
    def removeDuplicates(self, nums: list[int]):
        before = None
        retArray = list()
        insIndex = 0
        lenght = 0
        for i in range (len(nums)):
            if before != None and nums[i] > before:
                retArray.append(nums[i])
                nums[insIndex] = nums[i]
                before = nums[i]
                lenght +=1
                insIndex+=1
            elif before == None:
                before = nums[i]
                insIndex+=1
        return lenght+1





sol = Solution()
print(sol.removeDuplicates(nums = [1,1,2]))


