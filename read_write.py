
'''
file_object  = open(“filename”, “mode”)
mode:
‘r’ – Read mode which is used when the file is only being read
‘w’ – Write mode which is used to edit and write new information to the file (any existing files with the same name will be erased when this mode is activated)
‘a’ – Appending mode, which is used to add new data to the end of the file; that is new information is automatically amended to the end
‘r+’ – Special read and write mode, which is used to handle both actions when working with a file
'''
'''

file = open('testfile.txt','w')

file.write('Hello World')
file.write('\nThis is our new text file')
file.write('\nand this is another line.')
file.write('\nWhy? Because we can.')

file.close()
'''
file = open('SentimentLookupTable.csv', 'r')
#print (file.read(5))
#print (file.readline())
print (file.readlines(4))

#for line in file:
 #   print(line)