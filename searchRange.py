class Solution:
    def searchRange(self, nums: list, target: int) -> list:
        start =-1
        stop = -1
        for i in range(len(nums)):
            if nums[i] == target and start ==-1:
                start = i
            elif nums[i] == target:
                stop = i
        if start !=-1 and stop ==-1:
            stop = start
        return [start,stop]


