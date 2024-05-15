#1 . Method 1
file1 = open('18_Test_File.txt', 'r') # remember its pointing to a directly only , r means file is read in read only
#mode = r,w,a,r+
file1.close()

#2 . Method 2
with open('18_Test_File.txt', 'r') as file1:
    reading_file = file1.read()
    print(reading_file)
    #statements
    #no need to close the file here