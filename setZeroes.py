class Solution:
    def setZeroes(self, matrix: list) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    matrix[i][j] = None
                    remI = i
                    remJ = j
                    i = 0
                    j = 0
                    while i <len(matrix):
                        if matrix[i][remJ] !=0:
                            matrix[i][remJ] = None
                        i+=1

                    while j<len(matrix[remI]):
                        if matrix[remI][j] !=0:
                            matrix[remI][j] = None
                        j+=1
                    i = remI
                    j = remJ
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == None:
                    matrix[i][j] = 0
        # print(matrix)
sol = Solution()
# print(sol.setZeroes([[1,1,1],[1,0,1],[1,1,1]]))
print(sol.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))




