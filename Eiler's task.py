class Solution:
    def task(self, start, stop):
        array = list()
        sum = 0
        for i in range(start,stop):
            array.append(i)
        for i in range(len(array)):
            if array[i] % 3 == 0 or array[i] %5 == 0:
                sum+=array[i]
        return sum

sol = Solution()
print(sol.task(1,1000))
print(sol.task(1,10))


