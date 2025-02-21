'''''
fw=open("/Users/gokulapriyas/Documents/Python/Untitled-1.txt","r+")
file_s=fw.read()

#print(fw)
print(file_s)
print(fw.mode)
print(fw.name)

fw.close()

#using with (automatically closes file)
with open("/Users/gokulapriyas/Documents/Python/with_ex.txt","r+") as F1:
    fs=F1.read()
    print(fs)
    print(F1.closed)

    '''

"""""
The 'readlines' method reads the file line by line and stores each line 
as an element in a list. The order of lines in the list corresponds to their
order in the file.

The 'readline' method reads individual lines from the file. It can be called
multiple times to read subsequent lines.

Once the method .read(4) is called the first 4 characters are called. If we 
call the method again, the next 4 characters are called. The output for the
following cell will demonstrate the process for different inputs to the 
method read():
"""

'''''
with open("/Users/gokulapriyas/Documents/Python/with_ex.txt","r+") as f1:
    fs=f1.readline()
    print(fs)

with open("/Users/gokulapriyas/Documents/Python/with_ex.txt","r+") as f1:
    fs=f1.readlines()
    print(fs)

    '''
'''''
with open("/Users/gokulapriyas/Documents/Python/with_ex.txt","r+") as f1:
    fs=f1.readlines()
    print(fs)
    fp=f1.seek(19)
    print(fp)
    c=f1.read(6)
    print(c)


with open("/Users/gokulapriyas/Documents/Python/with_ex.txt","r+") as f1:
    for line in  f1:
        print(line)
    #fs=f1.readlines()
    #print(fs)


'''''

'''''

#write in file:

with open("/Users/gokulapriyas/Documents/Python/write_ex.txt","w+") as f1:
    s=f1.write("Work with product managers to monitor new releases.")
    print(s)


L=["Help drive growth in usage of data\n","implement dashboards & data models\n","analyze product data to enhance features "]
with open("/Users/gokulapriyas/Documents/Python/write_ex.txt","w+") as f1:
    for line in L:
        f1.write(line)
        print("Success")


with open("/Users/gokulapriyas/Documents/Python/app_ex.txt","a+") as f1:
    s=f1.write("Work with product managers to monitor new releases.")
    print(s)

'''''

#copy contents from one file to a new one:

with open("/Users/gokulapriyas/Documents/Python/with_ex.txt","r+") as readfile:
    with open("/Users/gokulapriyas/Documents/Python/ex4.txt","w+") as writefile:

        for line in  readfile:
            writefile.write(line)
            print(writefile)
            print(writefile.tell())
            print(writefile.seek(10))
           