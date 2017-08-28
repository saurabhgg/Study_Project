from sys import argv

script,file_name,name=argv

print 'Hello %s I see you want to open file %s' %(name,file_name)

file_read=open(file_name,'w')

print 'File opened successfully'
print 'Let\'s write something into the file'

file_read.write(raw_input('Please enter something which you want to write into the file '))

file_read.write('\n')
file_read.write(raw_input('Something else '))

file_read.write('\n')

file_read.write(raw_input('Something else again'))
file_read.write('\n')