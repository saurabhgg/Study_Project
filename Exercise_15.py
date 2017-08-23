from sys import argv

script_name,name,file_name=argv
# name=raw_input("What is your name sir")
# file_name=raw_input('Please enter the file that you want me to process ? ')
print 'Hello %s looks like you want me to procees %s file' %(name,file_name)
#Opening the file for reading
file_open=open(file_name)

print '%s is opened successfully %s' %(file_name,name)
#Reading the file after opening
print file_open.read()

print "Type the filename again:"
file_again = raw_input("> ")
txt_again = open(file_again)
print txt_again.read()

print ""