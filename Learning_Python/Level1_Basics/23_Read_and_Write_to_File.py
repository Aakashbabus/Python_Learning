file1= open('18_Test_File.txt', 'r+')
reading_file = file1.read()
print(reading_file)
file1.close()

file1= open('18_Test_File.txt', 'a')
writing_File = file1.write(" Mango Byte")
print(writing_File)
file1.close()
