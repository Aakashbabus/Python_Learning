# caution , existing data will be erased fully
file1=open('18_Test_File.txt', 'w')
writing_file=file1.write('Hello')
print(writing_file)
file1.close()

# this will return the number of characters written

file1 = open('18_Test_File.txt', 'r')
reading_file=file1.read()
print(reading_file)
file1.close()