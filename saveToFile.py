from datetime import datetime
class Save():
    def saveToFile(self, data: str):
        filename = "C:/projects/myleetcode/" + datetime.now().strftime("%Y%m%d%H%M%S")+ str('.py')
        file = open(filename, "w+")
        # file.write('A=41'+"\n")
        file.write(data)
        file.close()
        return filename

sol = Save()
print(sol.saveToFile('print(A)'))
