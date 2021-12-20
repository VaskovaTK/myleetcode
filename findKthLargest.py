class Solution:
    def findKthLargest(self, nums: list, k: int) -> int:
        nums = sorted(nums)
        newK = 0-k
        return nums[newK]



sol = Solution()
sol.findKthLargest([3,2,1,5,6,4], k = 2)
