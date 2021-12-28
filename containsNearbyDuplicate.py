class Solution:
    def containsNearbyDuplicate(self, nums: list, k: int) -> bool:
        dictionary = {}
        flag = False
        for i in range(len(nums)):
            if nums[i] not in dictionary:
                dictionary[nums[i]] =[i]
            else:
                dictionary[nums[i]].append(i)
        for key in dictionary.keys():
            array = dictionary[key]
            if len(array)>2:
                flag = self.recursion(array,k)
                if flag:
                    return True
                else:
                    continue
            elif len(array)<2:
                continue
            else:
                if abs(array[0]-array[1])<=k:
                    return True

        if flag == True:
            return True
        return False

    def recursion(self, array:list, k:int):
        for i in range(len(array)):
            for j in range(i+1,len(array)):
                if abs(array[i] - array[j]) <=k:
                    return True
                else:
                    continue
        return False


sol = Solution()
print(sol.containsNearbyDuplicate(nums = [1,2,3,1], k = 3))
print(sol.containsNearbyDuplicate([1,0,1,1], k = 1))
print(sol.containsNearbyDuplicate([1,2,3,1,2,3], k = 2))