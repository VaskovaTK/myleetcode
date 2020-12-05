print("Heeeelo")

f= open("C:\projects\myleetcode\eee.txt","w+")
for i in range(10):
     f.write("This is line %d\r\n" % (i+1))
f.close()