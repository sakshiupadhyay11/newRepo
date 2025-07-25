"""file1=open("MyFile1.txt",'a')
file2=open(r"/home/my/Documents/practice/MyFile2.txt","w+")
File_object.read([n])
"""

"""file1=open('myfile.txt','w')
L=["Hey how are you\n", "How was your day\n","How are you doing\n"]
file1.write("Hello \n")
file1.writelines(L)
file1.close()
file1=open("myfile.txt",'r+')
print("Output of Read function is ")
print(file1.read())
print()
file1.seek(0)
print('Output of Readline function is ')
print(file1.readline())
print()
file1.seek(0)

# to show difference bw read and readline
print("Output of Read(9) function is ")
print(file1.read(9))
print()
file1.seek(0)
print('Output of Readline(9) function is ')
print(file1.readline(9))
file1.seek(0)

#readline function output is
print("Output of Readline function is ")
print(file1.readlines())
print()
file1.close()"""

"""file =open('employee.txt','w+')
for i in range(4):
    name=input("Enter the name of employee ")
    file.write(name)
    file.write('\n')


file.seek(0)
print(file.read(80))
print('Names are entered in the file')
file.close()

"""
"""file2=open("employee1",'w+')
liss=[]
for i in range(3):
    name=input("Enter the name of the employee: ")
    liss.append(name+'\n')
file2.writelines(liss)
file2.seek(0)
print(file2.read()) 
file2.close()
print("Data is writen in the file ")   """

file3=open('myfile.txt','w')
L=["Hey how are you\n", "How was your day\n","How are you doing\n"]
file3.writelines(L)
file3.close()

file3=open('myfile.txt','a') #append
file3.write('hello'+'\n')
file3.close()

file3=open('myfile.txt','r')
print(file3.read())
file3.close()

file3=open('myfile.txt','w')
file3.write("did this overwrite \n")  # this will overwrite the present content of the 'myfile'
file3.close()

file3=open('myfile.txt','r')
print(file3.read())
file3.close()







