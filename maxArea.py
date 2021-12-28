class Solution:
    def maxArea(self, height: list) -> int:
        mostWater = 0
        newHeight = sorted(height)
        middle = int(len(height)/2)
        middleEl = newHeight[middle]
        for i in range(len(height)):
            if height[i] < middleEl:
                continue
            count = 0
            for j in range(i+1,len(height)):
                count+=1
                nowWater = count * min(height[i],height[j])
                if nowWater > mostWater:
                    mostWater = nowWater
        return mostWater
        #     if i == 0:
        #         maxBefore = 0
        #     else:
        #         maxBefore = max(height[i-1],maxBefore)
        #     if maxBefore >=height[i]:
        #         container = height[i]
        #     else:
        #         container = maxBefore
        #     nowWater = (i+1)*container
        #     if nowWater > mostWater:
        #         mostWater = nowWater
        # print(mostWater)
        # return mostWater

sol = Solution()
sol.maxArea([1,8,6,2,5,4,8,3,7])
sol.maxArea(height = [1,1])