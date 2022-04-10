
class Solution:
    def threeSum(self, nums: list) -> list:
        retList = list()
        save = [0]*3
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if i!=j and i!=k and j != k:
                        if nums[i]+nums[j]+nums[k] == 0:
                            if nums[i] >=nums[j] and nums[i]>=nums[k]:
                                save[0] = nums[i]
                                if nums[j] >=nums[k]:
                                    save[1] = nums[j]
                                    save[2] = nums[k]
                                else:
                                    save[1] = nums[k]
                                    save[2] = nums[j]
                            elif nums[i] >=nums[j] and nums[i]<=nums[k]:
                                save[1] = nums[i]
                                if nums[j] >=nums[k]:
                                    save[0] = nums[j]
                                    save[2] = nums[k]
                                else:
                                    save[0] = nums[k]
                                    save[2] = nums[j]
                            elif nums[i]<=nums[j] and nums[i]>=nums[k]:
                                save[1] = nums[i]
                                if nums[j] >=nums[k]:
                                    save[0] = nums[j]
                                    save[2] = nums[k]
                                else:
                                    save[0] = nums[k]
                                    save[2] = nums[j]
                            else:
                                save[2] = nums[i]
                                if nums[j] >=nums[k]:
                                    save[0] = nums[j]
                                    save[1] = nums[k]
                                else:
                                    save[0] = nums[k]
                                    save[1] = nums[j]
                            if save in retList:
                                continue
                            else:
                                retList.append(save)
                                save = [0]*3
        return retList
sol = Solution()
print(sol.threeSum([-1,0,1,2,-1,-4]))

