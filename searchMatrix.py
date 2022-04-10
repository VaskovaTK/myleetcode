class Solution:
    def searchMatrix(self, matrix:list, target: int) -> bool:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == target:
                    return True
                if matrix[i][j]>target:
                    break
        return False
