#read the entire file
file1= open('18_Test_File.txt', 'r')
reading_file = file1.read()
print (reading_file)
file1.close()

# read files until a specific character length
file1= open('18_Test_File.txt', 'r')
reading_file = file1.read(6)
print (reading_file)
file1.close()

# read the first line
file1= open('18_Test_File.txt', 'r')
reading_file = file1.readline()
print (reading_file)
file1.close()

#read the lines as string
file1= open('18_Test_File.txt', 'r')
reading_file = file1.readlines()
print (reading_file)
file1.close()

with open('18_Test_File.txt', 'r') as file1:
    reading_file=file1.read()
    print(reading_file)