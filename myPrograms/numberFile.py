file_name = open (r"C:\Users\npaudel\Google Drive\Programming notes\Python\CGS_5935_Introduction_to_Programming_Using_Python\rnumbers.txt","w")
for i in range (1,101):
    file_name.write(str(i)+'\n')
file_name.close()
sum = 0
file_name = open (r"C:\Users\npaudel\Google Drive\Programming notes\Python\CGS_5935_Introduction_to_Programming_Using_Python\rnumbers.txt","r")
for line in file_name:
    #line = line.rstrip('\n')
    sum += int(line)
print(sum)
file_name.close()
