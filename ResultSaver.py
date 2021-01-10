class ResultSaver():
    def __init__(self, now):
        self.filename = self.getResultName(now)
        self.file = open(self.filename, "w+")
        return

    @staticmethod
    def getResultName(now):
        return "C:/projects/myleetcode/userResult" + now + str('.txt')

    def appendToResultFile(self, result: str):
        self.file.write(result + "\n")

    def close(self):
        self.file.close()
