class Solution:
    def rotate(self, matrix: list) -> None:
        return
    def cycle (self,matrix, jump:int, maximum: int):
        i = 0
        j = 0
        nowLenght = 0
        while nowLenght<maximum*4:
            save = matrix[i][j]
            if j<maximum:
                newJ = j + jump
                saveN = matrix[i][newJ]
                matrix[i][newJ] = save
                j = newJ








