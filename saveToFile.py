from datetime import datetime
class Save():
    def saveResultToFile(self, retArray: list):
        filename = "C:/projects/myleetcode/" + "userResult" + datetime.now().strftime("%Y%m%d%H%M%S") + str('.txt')
        file = open(filename, "w+")
        for index in range(0, len(retArray)):
            file.write(str(index) + "\n")
        file.close()

    def saveToFile(self, data: str):
        filename = "C:/projects/myleetcode/" + datetime.now().strftime("%Y%m%d%H%M%S")+ str('.py')
        file = open(filename, "w+")
        file.write('import saveToFile'+"\n")
        file.write(data +"\n"+'save = saveToFile.Save()' + "\n")
        file.write("sol = SolutionfromUser()" + "\n")
        file.write("ret1 = sol.userFunction(10)"+ "\n")
        file.write("ret2 = sol.userFunction(20)" + "\n")
        file.write("ret3 = sol.userFunction(30)" + "\n")
        file.write("retArray = [ret1, ret2, ret3]"+ "\n")
        file.write('filePath = save.saveResultToFile(retArray)'+ "\n")
        file.close()
        return filename

