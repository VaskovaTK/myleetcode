class Solution:
    def longestIncreasingPath(self, matrix: list) -> int:
        resList = [0]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                self.recursion(matrix,i,j,1,resList)
        return resList[0]

    def recursion (self, matrix, i, j, result,listOfResults:list):
        if i-1>=0:
            if matrix[i-1][j] > matrix[i][j]:

                self.recursion(matrix,i-1,j,result+1,listOfResults)
                if listOfResults[0]<result:
                    listOfResults[0]=result
        if i+1<=len(matrix)-1:
            if matrix[i+1][j]>matrix[i][j]:

                self.recursion(matrix, i + 1, j, result+1, listOfResults)
                if listOfResults[0] < result:
                    listOfResults[0] = result
        if j-1>=0:
            if matrix[i][j-1]>matrix[i][j]:


                self.recursion(matrix, i, j-1, result+1, listOfResults)
                if listOfResults[0] < result:
                    listOfResults[0] = result
        if j+1<=len(matrix[i])-1:
            if matrix[i][j+1]>matrix[i][j]:

                self.recursion(matrix, i, j+1, result+1, listOfResults)
        if listOfResults[0]<result:
            listOfResults[0]=result
        return listOfResults


sol = Solution()
sol.longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]])
sol.longestIncreasingPath([[3,4,5],[3,2,6],[2,2,1]])